import requests
import os 

service_uri = 'http://localhost:8000/api/'
h_close = {'Connection': 'Close'}


def check_server(cid=None) -> bool:
    uri = 'http://localhost:8000/'

    if cid:
        uri += str(cid)

    try:
        res = requests.head(uri, headers=h_close)
    except requests.exceptions.RequestException:
        return False

    return res.status_code == requests.codes.ok


def stock_id_choice() -> int: # Check invalid input
    ok = False

    while not ok:

        try:
            answer = int(input(f"Enter your choice {stock_id}: "))
        except ValueError:
            print('Not a valid option. Come back again.')
            exit()

        ok = answer in stock_id

        if ok:
            return answer
        print("Not a valid stock option!")

def buy() -> bool: # Purchased a stock
    print('Please choose stocks to buy...')
    stock_request = requests.get(f'{service_uri}stocks/')
    json_stock = stock_request.json()
    print('option     ' + 'name'.ljust(15) + 'price')
    global stock_id
    stock_id = []

    for i in json_stock:
        stock_id.append(i['id'])
        print(str(i['id']).ljust(10), end='')
        print(i['name'].ljust(15), end='')
        print(i['price'])

    choose_stock = stock_id_choice()
    request_price = requests.get(f'{service_uri}stocks/{choose_stock}/')
    json_price = request_price.json()
    price = float(json_price['price'])

    try:
        share_count = int(input('How many shares: '))
    except ValueError:
        print('Not a valid option. Come back again.')
        exit()

    total = price * share_count

    if total > balance:
        print('You do not have enough balance. Come back again.')
        exit()

    print(f'That would be {total}')

    purchased_data = {
                    'user_id': user_id, 
                    'stock_id': choose_stock, 
                    'share': share_count, 
                    'price': price
                    }

    post_purchased = requests.post(f'{service_uri}buy/', auth=(username, password), json=purchased_data)

    print('Thank you for your purchased. It will deduct to your balance.')
    print('Your current balance as of now... ')

    new_balance = balance - total

    print(f'Current Balance: {new_balance}')


def sell_id_choice() -> int: # Check invalid input
    ok = False

    while not ok:

        try:
            answer = int(input(f"Enter your choice {sell_id}: "))
        except ValueError:
            print('Not a valid option. Come back again.')
            exit()
        ok = answer in sell_id

        if ok:
            return answer
        print("Not a valid stock option!")


def sell() -> bool:
    print('Please choose your stocks to sell...')
    sell_request = requests.get(f'{service_uri}purchased/')
    json_sell = sell_request.json()
    stock_request = requests.get(f'{service_uri}stocks/')
    json_stock = stock_request.json()

    print('option  ' + 'share'.ljust(12) + 'stock'.ljust(12) + 'price')

    global sell_id
    sell_id = []

    for i in json_sell:
        sell_id.append(i['id'])
        if i['user_id'] == user_id:
            print(str(i['id']).ljust(10), end='')
            print(str(i['share']).ljust(10), end='')
            for x in json_stock:
                if i['stock_id'] == x['id']:
                    print(x['name'].ljust(12), end='')
                    print(str(x['price']).ljust(12))

    if sell_id == []:
        print('You did not purchase a stock. Come back again.')
        exit()

    option = sell_id_choice()
    price = 0
    share = 0

    for i in json_sell:
        if i['id'] == option:
            share = i['share']
            stock = i['stock_id']
            for x in json_stock:
                if stock == x['id']:
                    price = x['price']

    try:
        share_count = int(input('How many shares: '))
    except ValueError:
        print('Not a valid option. Come back again.')
        exit()

    if share_count > share:
        print('You do not have enough shares. Come back again.')
        exit()

    total_sell = float(price) * int(share)

    print(f'That would be {total_sell}')

    sell_data = {
        'share': share_count, 
        'user_id': user_id, 
        'price': price, 
        'id': option
        }

    post_purchased = requests.put(f'{service_uri}api/sell/', auth=(username, password), json=sell_data)

    print('Thank you for your purchased.')
    print('Your added it to your balance, and as of now... ')

    new_balance = balance + total_sell

    print(f'Your Current Balance: {new_balance}')


def read_user_choice() -> int:

    ok = False

    while not ok:
        answer = input("Enter your choice, 1 = BUY Stocks or 2 = SELL Stocks: ")
        ok = answer in ['1', '2']

        if ok:
            return answer
        print("Not a valid choice!")



def user_id_option() -> int:

    ok = False

    while not ok:
        user_id = int(input('Please type your user id: '))
        user_id_request = requests.get(f'{service_uri}users/')
        json_user_id = user_id_request.json()
        print('USER ID  ' + 'USERNAME'.ljust(12))

        for i in json_user_id:
            print(str(i['id']).ljust(10), end='')
            print(str(i['username']).ljust(10))
        
        user_request = requests.get(f'{service_uri}users/{user_id}')
        json_user_request = user_request.json()
        check_user_name = json_user_request['username']

        if username != check_user_name:
            print(f'This user id "{user_id}" is not yours.')
            print('Try Again.')
        else:
            ok = True
            return user_id


def welcome() -> bool:
    print("+---------------------------------------+")
    print("|  Welcome to API Django Stock Trading  |")
    print("+---------------------------------------+")

    user_id_request = requests.get(f'{service_uri}users/')
    json_user_id = user_id_request.json()

    print('USER ID  ' + 'USERNAME'.ljust(12))

    for i in json_user_id:
        print(str(i['id']).ljust(10), end='')
        print(str(i['username']).ljust(10))

    global user_id
    user_id = int(user_id_option())
    print(f'Welcome {username} !!!')
    user_request = requests.get(f'{service_uri}users/{user_id}')
    json_user = user_request.json()
    global balance
    balance = json_user['balance']
    print(f'Here is your current balance: {balance}')


# This start the program flow
username = os.environ.get('api_user') # hidden inside os environment
password = os.environ.get('api_pass')

if username == '' or password == '':
    print('please fill in your username, and password')
    print('once you filled your username and password, run this program and it will show you your id')
    exit()

if not check_server():
    print("Server is not responding - quitting!")
    exit()

print(f'Connecting to {service_uri}...')

welcome()

choice = int(read_user_choice())

if choice == 1:
    buy()
elif choice == 2:
    sell()
  
    







