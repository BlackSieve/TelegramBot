import json
import requests
from secret import money

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, amount: str, base: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты{base}')

        try:
            base_ticker = money[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base} ')

        try:
            quote_ticker = money[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote} ')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionException(f'Не удалось обработать количество {amount} ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[money[base]]


        return total_base