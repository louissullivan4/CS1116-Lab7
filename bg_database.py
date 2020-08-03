#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
import pymysql as db
import datetime
from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

today = datetime.date.today()
new = today.year - 7
age = today.replace(new)
result = '<p>Sorry you have not logged in! Go back to the homepage</p>'
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                cursor = connection.cursor(db.cursors.DictCursor)
                cursor.execute("""SELECT firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email
                                  FROM ballygunnerscouts
                                  WHERE birth >= %s AND birth <= %s """, (age, today))
                result = '<table><tr><th>Forename</th><th>Surname</th><th>Date of Birth</th><th>Gender</th><th>Address</th><th>Parent/Guardian Forename</th><th>Parent/Guardian Surname</th><th>Parent/Guardian Number</th><th>Parent/Guardian Email</th></tr>'
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['birth'], row['gender'], row['address'], row['guardian_fname'], row['guardian_sname'], row['guardian_number'], row['guardian_email'])
                result += '</table>'
                cursor.close()
                connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Ballygunner Database: Beavers</title>
            </head>
            <body>
                %s
            </body>
            </html>""" % (result))
