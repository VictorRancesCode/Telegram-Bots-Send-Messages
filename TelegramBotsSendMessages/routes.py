import urllib3
import certifi
from flask import redirect
from flask import render_template
from flask import request


def send(message):
    bot_id = "Your Token"
    chat_id = "ID Chat Telegram"

    try:
        https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = https.request('GET', 'https://api.telegram.org/bot'
                          + bot_id + '/sendMessage?chat_id='
                          + chat_id + '&text=' + message)
    except urllib3.exceptions.SSLError as err:
        pass


def home_page():
    return render_template('index.html')


def sendmessage():
    message = request.form['message']
    send(message)
    return redirect('/')
