import json
from pprint import pprint

with open('../01fetchAPI/output.json') as f:
    data = json.load(f)

currency_list = ['EUR', 'USD', 'JPY', 'CAD', 'GBP', 'NZD','INR']
filtered_data = []
# pprint(data)
for date in data['rates']:
    for currency, currency_value in data['rates'][date].items():
        if currency in currency_list:
            # filtered_data[date][currency] = currency_value
            dictObj = {}
            dictObj['date'] = date
            dictObj['currencyId'] = str( currency_list.index(currency) + 1 )
            dictObj['value'] = currency_value
            filtered_data.append(dictObj)

with open('filtered_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)
