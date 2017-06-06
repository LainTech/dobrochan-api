import requests
import json


class API:
    @staticmethod
    def get_user_info():
        url = 'http://dobrochan.com/api/user.json'
        cookies = dict(hanabira_temp='ffb56b51c0e802e72792d2bdbdc0c6aab98643678dde25e184c84831902e888e51906524')
        r = requests.get(url, cookies=cookies)
        print(r.json())
