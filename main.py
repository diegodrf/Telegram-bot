# -*- encoding: utf-8 -*-
import requests
import json

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.baseUrl = 'https://api.telegram.org/bot' + self.token

    def setMe(self, method='/getMe'):
        res = requests.get(self.baseUrl + method)
        return res.json()

    def getUpdates(self, method='/getUpdates'):
        res = requests.get(self.baseUrl + method)
        return res.json()

    def sendMessage(self, chat_id, text, parse_mode='HTML', method='/sendMessage'):
        # chat_id = 434725102
        res = requests.get(self.baseUrl + method, params={'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode})
        return res.json()

if __name__ == '__main__':

    bot = TelegramBot('639933396:AAHeB13xSkiIm_ihkPtS-5rI4p1qcSHFb0I')
    print(bot.setMe())
    print(bot.getUpdates())
    print(bot.sendMessage('434725102', '<b>Hello</b> <i>World!</i>'))