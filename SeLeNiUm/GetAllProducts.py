import requests

url = 'https://www.advantageonlineshopping.com/catalog/api/v1/categories/all_data'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data
else:
    print('Error: Failed to retrieve data from API')
print(data)