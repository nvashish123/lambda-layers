import requests as req
from requests.exceptions import HTTPError


def cust_fun():
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            response = req.get(url)

        # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
    print("Hello Vegas from the deep layers!!")
    return 1
