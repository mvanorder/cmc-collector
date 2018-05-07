import csv
import sys
import json

json_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

keys = (
    "id",
    "name",
    "symbol",
    "rank",
    "price_usd",
    "price_btc",
    "24h_volume_usd",
    "market_cap_usd",
    "available_supply",
    "total_supply",
    "max_supply",
    "percent_change_1h",
    "percent_change_24h",
    "percent_change_7d",
    "last_updated"
)

# csv_file is only valid inside the with block.
with open(csv_file_name, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=keys, delimiter=',', lineterminator='\n')
    csv_writer.writeheader()
    with open(json_file_name, 'r') as json_file:
        json_data = json.loads(json_file.read())
        for currency in json_data:
            csv_writer.writerow(currency)
"""
# csv_file is valid anywhere after this line.
csv_file = open(csv_file_name, 'w')
csv_writer = csv.DictWriter(csv_file, fieldnames=keys, delimiter=',', lineterminator='\n')
csv_writer.writeheader()
json_file = open(json_file_name, 'r')
json_data = json.loads(json_file.read())
for currency in json_data:
    csv_writer.writerow(currency)

# This is like the one above but using csv_file.write rather than th csv module.
with open(csv_file_name, 'w') as csv_file:
    headers_row = ','.join(keys)
    csv_file.write(headers_row)
    csv_file.write('\n')
    with open(json_file_name, 'r') as json_file:
        json_data = json.loads(json_file.read())
        for currency in json_data:
            row = ','.join((currency[key] or '' for key in keys))
            csv_file.write(row)
            csv_file.write('\n')
"""
