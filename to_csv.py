import csv
import sys
import json

json_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

keys = [
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
]

with open(csv_file_name, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=keys, delimiter=',', lineterminator='\n')
    csv_writer.writeheader()
    with open(json_file_name, 'r') as json_file:
        json_data = json.loads(json_file.read())
        for currency in json_data:
            csv_writer.writerow(currency)
