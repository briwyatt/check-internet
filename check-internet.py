from requests import get, exceptions

def checkInternetConnection():
    try:
        get('http://www.google.com', timeout=3)
        print('internet is connected!! :) ')
    except exceptions.ConnectionError:
        print('internet not connected :((( ')

checkInternetConnection()