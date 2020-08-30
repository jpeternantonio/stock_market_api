import requests


def buy():
    print('Please choose stocks to buy...')

    stock_request = requests.get('http://localhost:8000/api/stocks/')
    json_stock = stock_request.json()
    print('option     ' + 'name'.ljust(15) + 'price')
    for i in json_stock:
        print(str(i['id']).ljust(10), end='')
        print(i['name'].ljust(15), end='')
        print(i['price'])

    choose_stock = input('Type the option# of the stock: ')
    request_price = requests.get(f'http://localhost:8000/api/stocks/{choose_stock}/')
    j = request_price.json()
    price = float(j['price'])
    share_count = float(input('How many shares: '))
    total = price * share_count
    print(f'That would be {total}')
    purchased_data = {'user_id': user_id, 'stock_id': choose_stock, 'share': share_count, 'price': price}
    post_purchased = requests.post('http://localhost:8000/api/buy/', auth=(username, password), json=purchased_data)
    print('Thank you for your purchased. It will deduct to your balance.')
    print('Your current balance as of now... ')
    new_balance = balance - total
    print(f'Current Balance: {new_balance}')


def sell():
    print('Please choose your stocks to sell...')
    sell_request = requests.get(f'http://localhost:8000/api/purchased/')
    json_sell = sell_request.json()
    stock_request = requests.get('http://localhost:8000/api/stocks/')
    json_stock = stock_request.json()
    print('option  ' + 'share'.ljust(12) + 'stock'.ljust(12) + 'price')
    for i in json_sell:
        if i['user_id'] == user_id:
            print(str(i['id']).ljust(10), end='')
            print(str(i['share']).ljust(10), end='')
            # add invalid choice
            for x in json_stock:
                if i['stock_id'] == x['id']:
                    print(x['name'].ljust(12), end='')
                    print(str(x['price']).ljust(12))

    option = int(input('Type the option number: '))
    price = 0
    share = 0
    for i in json_sell:
        if i['id'] == option:
            share = i['share']
            stock = i['stock_id']
            for x in json_stock:
                if stock == x['id']:
                    price = x['price']

    share_count = float(input('How many shares: '))
    total_sell = float(price) * int(share)
    print(f'That would be {total_sell}')
    sell_data = {'share': share_count, 'user_id': user_id, 'price': price, 'id': option}
    post_purchased = requests.put('http://localhost:8000/api/sell/', auth=(username, password), json=sell_data)
    print('Thank you for your purchased.')
    print('Your added it to your balance, and as of now... ')
    new_balance = balance + total_sell
    print(f'Your Current Balance: {new_balance}')


username = ''
password = ''
if username == '' or password == '':
    print('please fill in your username, and password')
    print('once you filled your username and password, run this program and will show you your id')
    exit()

user_id_request = requests.get('http://localhost:8000/api/users/')
json_user_id = user_id_request.json()
print('user_id  ' + 'username'.ljust(12))

for i in json_user_id:
    print(str(i['id']).ljust(10), end='')
    print(str(i['username']).ljust(10))

user_id = int(input('Please type your user id: '))
print(f'Welcome {username} !!!')
user_request = requests.get(f'http://localhost:8000/api/users/{user_id}')
json_user = user_request.json()
balance = json_user['balance']
print(f'Here is your current balance: {balance}')

choice = int(input('Type 1 to Buy and 2 to sell: '))
if choice == 1:
    buy()
elif choice == 2:
    sell()
else:
    print('You type the wrong input. Try again.')







