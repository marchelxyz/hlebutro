from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, static_folder='static', static_url_path='')

# 🔑 Вставь свой Telegram Bot токен и Chat ID
BOT_TOKEN = "7556364550:AAGRuzHVOK_5d8T2pr0oIA6o9UqHcH_z98k"
CHAT_ID = "727331113"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form.get('name')
    address = request.form.get('address')
    time = request.form.get('time')

    # 📩 Сообщение для отправки
    message = f"📦 Новый заказ из ХлебУтро:\n\n👤 Имя: {name}\n🏠 Адрес: {address}\n⏰ Время: {time}"

    # 🛠 Отправка в Telegram
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(telegram_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "<h2>Спасибо! Ваш заказ принят 🥖</h2><a href='/'>Вернуться</a>"

if __name__ == '__main__':
app.run(host="0.0.0.0", port=5000, debug=True)

