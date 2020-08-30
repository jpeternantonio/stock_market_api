Django Web App Stocks

OS:
    Ubuntu 18.04 running in WSL2

IDE: VS Code and Pycharm

Program used:
    python 3.8
    django 3.1
    javascript
    mysql

packages:
    mysqlclient
    djangorestframework
    request
    selenium
    chromedriver

environment = pipenv

All test were done in Django.
Functional test may not work on Windows OS.

Program Description:
    -This program will enable user to buy and sell stocks. Check history purchased
and show the return of his investment. REST api can use also to buy and sell stocks without opening
a webpage, as long as the server is running.


How to use this program.

1. Install all needed program and packages on your computer
2. Run it in localhost and do the usual migration in django
    a. Run 'python manage.py loaddata stocks.json' after migration. This will populate the data for stock models.
3. Register as superuser to add stocks. Name and price
4. Register again using web app and add your ideal balance to buy stocks.
5. Once registered, log-in and buy the stock and how many share you choose. Your balance will be deducted
after the purchased.
6. Navigate to purchased history and you can see your transaction, return of investment and selling of stocks.
7. Return of investment wil show depends on the value of stock. As of now, the stock change depends on market trends.
8. To sell, click the sell button...and sell how many share you have.

To use the api.
1. Open api_request.py, and make sure you are registered user and the server is still running.
2. Run api_request.py. The program will use the input to talk to user. Mostly using only input number.
3. The program will show your user id. Input your user id.
4. This will show your current balance and choices if you want to buy or sell stocks.
5. The program will exit once you have done your transaction.
