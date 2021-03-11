######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/<mail>/books')
def bookrack(mail):
    return send_file('templates/books.html')

@app.route('/<mail>')
def addbookrack(mail):

    return send_file('templates/addbookrack.html')

@app.route('/<mail>/<number>')
def bookbloin(mail,number):

    return send_file('templates/booklogin.html')



@app.route('/index')
def index():

    return send_file('templates/index.html')

@app.route('/login')
def login():

    return send_file('templates/login.html')

@app.route('/login_callback')
def login_callback():

    return send_file('templates/oauth_callback.html')

@app.route('/register')
def register():

    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):

    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):

    return send_file('templates/change_info.html')

@app.route('/<username>/change_password')
def change_password(username):

    return send_file('templates/change_password.html')


@app.route('/<username>/topic/release')
def topic_release(username):

    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):

    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):

    return send_file('templates/detail.html')


@app.route('/test_api')
def test_api():

    return send_file('templates/test_api.html')

if __name__ == '__main__':
    app.run(debug=True)

