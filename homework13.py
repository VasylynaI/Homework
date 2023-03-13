# Підключіться до API НБУ (документація тут https://bank.gov.ua/ua/open-data/api-dev),
# отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S.не забувайте про DRY, KISS, SRP та перевірки


import requests
import datetime


def get_exchange_rates():
    # Make a request to the API
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError()

    # Parse the JSON response
    data = response.json()

    # Create a list of currency exchange rates
    rates = []
    for item in data:
        name = item['txt']
        rate = item['rate']
        rates.append((name, rate))

    return rates


def write_to_file(rates):
    # Write the exchange rates to a text file
    now = datetime.datetime.now()
    filename = f"exchange_rates_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as f:
        f.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}]\n")
        for i, (name, rate) in enumerate(rates, start=1):
            f.write(f"{i}. {name} to UAH: {rate}\n")



