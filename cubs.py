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
new = today.year - 8
old = today.year - 12
age1 = today.replace(new)
age2 = today.replace(old)
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
                cursor.execute("""SELECT firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email, subs
                                  FROM ballygunnerscouts
                                  WHERE birth <= %s AND birth >= %s
                                  ORDER BY birth DESC """, (age1, age2))
                result = '<table id="scout-table"><tr><th>Forename</th><th>Surname</th><th>Date of Birth</th><th>Gender</th><th>Address</th><th>Parent/Guardian Forename</th><th>Parent/Guardian Surname</th><th>Parent/Guardian Number</th><th>Parent/Guardian Email</th><th>Subs Period Paid(out of 4): </th></tr>'
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['birth'], row['gender'], row['address'], row['guardian_fname'], row['guardian_sname'], row['guardian_number'], row['guardian_email'], row['subs'])
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
                <title>Ballygunner Database: Cubs</title>
                <link rel="stylesheet" href="styles.css">
            </head>
            <header>
              <h1>19th Waterford Ballygunner: Cubs</h1>
            </header>
            <body>
        		<nav>
        			<ul>
        				<li><a href="home.py">Home</a></li>
        				<li><a href="beaver.py">Beavers</a></li>
        				<li><a href="scouts.py">Scouts</a></li>
                        <li><a href="ventures.py">Ventures</a></li>
                        <li><a href="leaders.py">Leaders</a>
                        </li><li><a href="logout.py">Logout</a></li>
        			</ul>
                </nav>
                <nav id="update">
                    <ul>
                        <li><a href="skills.py">Adventure Skills</a></li>
                        <li><a href="display_subs_update.py">Subscription Due</a></li>
                    </ul>
                </nav>
                %s
                <nav id="update">
                    <ul>
                        <li><a href="add_scout.py">Add Cubs</a></li>
                        <li><a href="drop_scout.py">Delete Cubs</a></li>
                    </ul>
                </nav>
            </body>
        </html>""" % (result))
