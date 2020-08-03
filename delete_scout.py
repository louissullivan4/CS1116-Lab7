#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
import pymysql as db
from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

form_data = FieldStorage()
guardian_email = ''
firstname = ''
result = ''
if result == '':
    if len(form_data) != 0:
        try:
            cookie = SimpleCookie()
            http_cookie_header = environ.get('HTTP_COOKIE')
            if http_cookie_header:
                cookie.load(http_cookie_header)
                if 'sid' in cookie:
                    sid = cookie['sid'].value
                    session_store = open('sess_' + sid, writeback=False)
                    if session_store.get('authenticated'):
                        guardian_email = escape(form_data.getfirst('guardian_email', '')).strip()
                        connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                        cursor = connection.cursor(db.cursors.DictCursor)
                        cursor.execute("""SELECT guardian_email FROM ballygunnerscouts
                                            WHERE guardian_email = %s""", guardian_email)
                        if cursor.rowcount != 0:
                            cursor.execute("""DELETE FROM ballygunnerscouts
                                                WHERE guardian_email = %s""", guardian_email)
                            connection.commit()
                            result = '<p>Successfully deleted!</p>'
                        else:
                            result = '<p>Error! This youth member does not exist.</p>'
                        cursor.close()
                        connection.close()
                else:
                    result = '<p>Sorry you have not logged in! Go back to the homepage</p>'
        except db.Error:
            result = '<p>Error! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
            <title>Drop Youth Member</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <header>
          <h1>19th Waterford Ballygunner: Update Youth Members</h1>
        </header>
        <body>
        <nav>
            <ul>
                <li><a href="home.py">Home</a></li>
                <li><a href="beaver.py">Beavers</a></li>
                <li><a href="cubs.py">Cubs</a></li>
                <li><a href="scouts.py">Scouts</a></li>
                <li><a href="ventures.py">Ventures</a></li>
                <li><a href="leaders.py">Leaders</a></li>
                </li><li><a href="logout.py">Logout</a></li>
            </ul>
        </nav>
                %s
            </body>
            </html>""" % (result))
