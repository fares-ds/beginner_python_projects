import requests

# Currency available in the API
print("Currencies available: ", ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON', 'SEK', 'IDR', 'INR',
                                 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 'PLN', 'BGN', 'TRY', 'CNY', 'NOK',
                                 'NZD', 'ZAR', 'USD', 'MXN', 'ILS', 'GBP', 'KRW', 'MYR'])

# Gathering input parameters from the user
date = input("Please enter the date (in the format 'yyyy-mm-dd' or 'latest'): ")
base = input("Convert from (currency): ")
curr = input("Convert to (currency): ")
quan = float(input(f"How much {base} do you want to convert: "))

# Constructing the URL based on the user parameters and sending a request to the server
base_url = "https://api.exchangeratesapi.io"
url = f"{base_url}/{date}?base={base}&symbols={curr}"
response = requests.get(url)

# Displaying the error message, if something went wrong
if not response.ok:
    print(f"\nError {response.status_code}:")
    print(response.json()['error'])

else:
    data = response.json()
    rate = data['rates'][curr]

    result = quan * rate

    print(f"\n{quan} {base} is equal to {result:.2f} {curr}, based upon exchange rates on {data['date']}")
