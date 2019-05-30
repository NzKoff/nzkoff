
from flask import render_template, request, redirect, session, flash, url_for,Flask
from handlers.forms import RegForm, LoginForm
from api.db_handle import *


app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # login = request.form['username']
    # password = request.form['password']
    # if db_cmp_passwd(login, password):
    #     session['log_in'] = True
    # else:
    #     flash('Неправильный пароль')
    return render_template('index.html',form = form)
#
# @app.route("/favicon.ico",methods = ["GET"])
# def favicon():
#     pass
import json
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == "POST" :
        data = request.form.to_dict()
        print(request.form.to_dict())
        db_add_user(data)
        # login = request.form['username']
        # password = request.form['password']
        # firstname = request.form['firstname']
        # secondname = request.form['secondname']
        # bday = request.form['bday']
        # sex = request.form['sex']
        # hobby = request.form['sex']
        # social_link = request.form['social_link']
        # print(login, password, firstname, secondname, bday, sex, hobby, social_link)

        # if db_cmp_passwd(login, password):
        #     db_add_user(login, password, firstname, secondname, bday, sex, hobby, social_link)
        #     redirect('/events')
        # return redirect(url_for('login'))
    return render_template('register.html', form=form)
import requests
@app.route("/login/",methods=["POST"])
def auth():
    data = request.form.to_dict()
    print(data)
    id = (get_id_user(data).get("id"))
    print("http://localhost:5000/getTable/"+ str(id))
    return requests.get("http://localhost:5000/getTable/"+ str(id)).text


@app.route("/getTable/<int:id>",methods=["GET", 'OPTION'])
def getTable(id):
    print(id)

    # if request.method == 'option':
    #     return {}, 200, {'Access-Control-Allow-Origin': '*'}
    json.dumps(get_info())
    return render_template("table_test.html",datas = get_info(),id_user = id), 200, {'Access-Control-Allow-Origin': '*'}

@app.route('/logout')
def logout():
    session['log_in'] = False
    redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)


