#!/usr/local/bin/python3

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
result = '<p>Sorry you have not logged in! Go back to the homepage</p>'
if result == '<p>Sorry you have not logged in! Go back to the homepage</p>':
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
                        firstname = escape(form_data.getfirst('firstname', '')).strip()
                        surname = escape(form_data.getfirst('surname', '')).strip()
                        camping = escape(form_data.getfirst('camping', '')).strip()
                        backwoods = escape(form_data.getfirst('backwoods', '')).strip()
                        hillwalking = escape(form_data.getfirst('hillwalking', '')).strip()
                        pioneering = escape(form_data.getfirst('pioneering', '')).strip()
                        connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                        cursor = connection.cursor(db.cursors.DictCursor)
                        cursor.execute("""SELECT * FROM ballygunnerskills
                                                    WHERE firstname = %s and surname = %s""", (firstname, surname))
                        if cursor.rowcount == 0:
                            result = '<p>Error! This scout does not exist.</p>'
                        else:
                            cursor.execute("""UPDATE ballygunnerskills
                                                SET camping = %s
                                                WHERE firstname = %s and surname = %s""", (camping, firstname, surname))
                            connection.commit()
                            cursor.execute("""UPDATE ballygunnerskills
                                                SET backwoods = %s
                                                WHERE firstname = %s and surname = %s""", (backwoods, firstname, surname))
                            connection.commit()
                            cursor.execute("""UPDATE ballygunnerskills
                                                SET hillwalking = %s
                                                WHERE firstname = %s and surname = %s""", (hillwalking, firstname, surname))
                            connection.commit()
                            cursor.execute("""UPDATE ballygunnerskills
                                                SET pioneering = %s
                                                WHERE firstname = %s and surname = %s""", (pioneering, firstname, surname))
                            connection.commit()
                            result = '<p>Successfully updated skills!</p>'
                        cursor.close()
                        connection.close()
        except db.Error:
            result = '<p>Error! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
            <title>Update Subscriptions</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <body>
        <nav>
            <ul>
                <li><a href="home.py">Home</a></li>
                <li><a href="skills.py">Adventure Skills</a></li>
                <li><a href="update_skills.py">Update Skills</a></li>
                </li><li><a href="logout.py">Logout</a></li>
            </ul>
        </nav>
                %s
            </body>
            </html>""" % (result))
