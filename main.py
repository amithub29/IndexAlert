import os
from urllib.request import urlopen
from twilio.rest import Client
from re import findall
from dotenv import load_dotenv
from os import getenv

load_dotenv()
moneycontrol_url = "https://www.moneycontrol.com/stocksmarketsindia/"


def get_indices_value():
    page = urlopen(moneycontrol_url)
    html = page.read().decode("utf-8")

    nifty_pattern = "\"nifty_block_cp\">(.*)</s"
    sensex_pattern = "\"sensex_block_cp\">(.*)</s"

    nifty_val = findall(nifty_pattern, html)
    sensex_val = findall(sensex_pattern, html)

    return {"nifty": nifty_val[0], "sensex": sensex_val[0]}


def send_message(data):
    client = Client(os.getenv("account_id"), os.getenv("auth_token"))
    nifty = float(data["nifty"])
    sensex = float(data["sensex"])
    body = f'Market Update 📊📈📉\nNifty: {nifty}\nSensex: {sensex}'

    client.messages.create(body=body, from_=os.getenv("from_number"), to=os.getenv("to_number"))


values = get_indices_value()
send_message(values)
