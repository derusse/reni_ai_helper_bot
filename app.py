from flask import Flask, request
import requests

app = Flask(__name__)
TOKEN = '7543863102:AAFVRM2OZdp8zzmKRGrrKtE3txPiUI03aro'
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    return 'RENI Telegram Bot работает! ✅'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        requests.post(f'{TELEGRAM_URL}/sendMessage', json={{
            'chat_id': chat_id,
            'text': '✅ Бот получил сообщение: ' + text
        }})
    return {{'ok': True}}

if __name__ == '__main__':
    app.run()
