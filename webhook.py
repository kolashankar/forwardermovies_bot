from flask import Flask, request
from telegram import Update
from bot.main import bot

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    bot.process_new_updates([update])
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)

