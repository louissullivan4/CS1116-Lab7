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
                cursor.execute("""SELECT firstname, surname, gender, address, contact, email, garda_vetted, training_level
                                  FROM ballygunnerleaders
                                  ORDER BY garda_vetted ASC """)
                result = '<table id="leaders-table"><tr><th>Forename</th><th>Surname</th><th>Gender</th><th>Address</th><th>Contact</th><th>Email</th><th>Garda Vetting Date</th><th>Training Status</th></tr>'
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['gender'], row['address'], row['contact'], row['email'], row['garda_vetted'], row['training_level'])
                result += '</table>'
                cursor.close()
                connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Ballygunner Database: Leaders</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <header>
          <h1>19th Waterford Ballygunner: Leaders</h1>
        </header>
        <body>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="beaver.py">Beavers</a></li>
                    <li><a href="cubs.py">Cubs</a></li>
                    <li><a href="scouts.py">Scouts</a></li>
                    <li><a href="ventures.py">Ventures</a></li>
                    </li><li><a href="logout.py">Logout</a></li>
                </ul>
            </nav>
            %s
            <nav id="update">
                <ul>
                    <li><a href="add_leader.py">Add Leaders</a></li>
                    <li><a href="drop_leaders.py">Delete Leaders</a></li>
                </ul>
            </nav>
        </body>
    </html>""" % (result))
