import json
from pprint import pprint

with open('../01fetchAPI/output.json') as f:
    data = json.load(f)

currency_list = ['EUR', 'USD', 'JPY', 'CAD', 'GBP', 'NZD','INR']
filtered_data = {}
# pprint(data)
for date in data['rates']:
    filtered_data[date] = {}
    for currency, currency_value in data['rates'][date].items():
        if currency in currency_list:
            filtered_data[date][currency] = currency_value

with open('filtered_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)
