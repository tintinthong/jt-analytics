#!/usr/bin/env python3

URL = "https://api.etherscan.io/api?module=account&action=balance&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&tag=latest&apikey=8G84GZETGIWS5IHK2ZIUGYKG6KYDS5NE92"

import requests


class Explorer:
    def __init__(self):
        self.base_url = "https://api.etherscan.io/api"

    def get_balance(self, token_address):
        print(token_address)
        return


class Web3:
    pass
