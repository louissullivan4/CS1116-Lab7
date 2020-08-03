#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db

form_data = FieldStorage()
username = ''
result = ''
if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password = escape(form_data.getfirst('password', '').strip())
    if not username or not password:
        result = '<p>Error: user name and password are required</p>'
    else:
        sha256_password = sha256(password.encode()).hexdigest()
        try:
            connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s
                              AND password = %s""", (username, sha256_password))
            if cursor.rowcount == 0:
                result = '<p>Error! The username or password you entered is incorrect.</p>'
            else:
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                <nav>
                   <ul>
                        <li><a href="home.py">Home</a></li>
                        <li><a href="beaver.py">Beavers</a></li>
                       <li><a href="cubs.py">Cubs</a></li>
                       <li><a href="scouts.py">Scouts</a></li>
                       <li><a href="ventures.py">Ventures</a></li>
                       <li><a href="leaders.py">Leaders</a></li>
                       <li><a href="logout.py">Logout</a></li>
                   </ul>
                  </nav>
                  <p>Login Successful!</p>"""
                print(cookie)
            cursor.close()
            connection.close()
        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Ballygunner Login</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <header>
          <h1>19th Waterford Ballygunner: Login</h1>
        </header>
        <body>
            %s
            <form action="login.py" method="post" id ="login-form">
                <label for="username">Username: </label>
                <input type="text" name="username" id="username" value="%s" />
                <label for="password">Password: </label>
                <input type="password" name="password" id="password" />
                <input type="submit" value="Login" id="submit" />
            </form>
        </body>
    </html>""" % (result, username))
