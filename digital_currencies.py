from urllib.request import urlopen
from datetime import datetime
from json import loads

__AUTHOR__ = 'MohammadHossein Bagheri KheirAbadi'
__GITHUB__ = 'https://github.com/PyBagheri/api-collection'
__LICENSE__ = 'GPL-3.0'


BASE_URL = 'https://digiarz.com/webservice/api/'


DIGITAL_CURRENCIES_NAME = [
    ('BTC', 'Bitcoin'),
    ('ETH', 'Ethereum'),
    ('ETC', 'Ethereum classic'),
    ('XMR', 'Monero'),
    ('XRP', 'Ripple'),
    ('ZEC', 'Z-cash'),
    ('FCT', 'Factom'),
    ('LTC', 'Litecoin'),
    ('DOGE', 'Dogecoin'),
    ('DASH', 'Digital cash')
]

CURRENCIES_NAME = [
    ('USD', 'United States Dollars'),
    ('TMN', 'Iranian Toman')
]


class Currencies:
    class __Currency:
        def __init__(self, tmn, usd, currency_name):
            self.TMN = tmn
            self.USD = usd
            self.currency_name = currency_name

    @staticmethod
    def __jsonize(response):
        return loads(response.read().decode(response.info().get_content_charset('utf-8')))

    @staticmethod
    def __compute_time(time_string):
        return datetime.strptime(time_string, '%d-%m-%Y %H:%M:%S')

    def __get_price_class(self, json, currency):
        currency_group = json[currency]['rates']
        return self.__Currency(tmn=currency_group['TMN']['rate'],
                               usd=currency_group['USD']['rate'],
                               currency_name=dict(DIGITAL_CURRENCIES_NAME)[currency])

    def __init__(self):
        __result = self.__jsonize(urlopen(BASE_URL))
        self.datetime = self.__compute_time(time_string=__result['time'])
        self.BTC = self.__get_price_class(json=__result, currency='BTC')
        self.ETH = self.__get_price_class(json=__result, currency='ETH')
        self.ETC = self.__get_price_class(json=__result, currency='ETC')
        self.XMR = self.__get_price_class(json=__result, currency='XMR')
        self.XRP = self.__get_price_class(json=__result, currency='XRP')
        self.ZEC = self.__get_price_class(json=__result, currency='ZEC')
        self.FCT = self.__get_price_class(json=__result, currency='FCT')
        self.LTC = self.__get_price_class(json=__result, currency='LTC')
        self.DOGE = self.__get_price_class(json=__result, currency='DOGE')
        self.DASH = self.__get_price_class(json=__result, currency='DASH')










