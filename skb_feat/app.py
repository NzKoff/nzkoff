from flask import Flask

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'ftLplK5FA8GZ'


import main
