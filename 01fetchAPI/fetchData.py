import requests
import sys

start_date = sys.argv[1]
end_date = sys.argv[2]
url = 'https://api.exchangeratesapi.io/history?start_at=' + start_date + '&end_at=' + end_date
print(url)
response = requests.get(url, stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with open('output.json', 'wb') as handle:
    for block in response.iter_content(1024):
        handle.write(block)

