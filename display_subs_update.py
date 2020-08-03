#!/usr/local/bin/python3

from cgitb import enable
enable()

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
                cursor.execute("""SELECT guardian_email, subs
                                  FROM ballygunnerscouts
                                  WHERE subs < 4
                                  ORDER BY birth DESC""")
                if cursor.rowcount == 0:
                    result = '<p>Sorry. There are no youth members at present.</p>'
                else:
                    options = ''
                    for row in cursor.fetchall():
                        options += '<option value="%s">%s</option>' % (row['guardian_email'], row['guardian_email'])
                    result = """<form action="subs_due.py" method="post" id="subs-update">
                                <label for="guardian_email">Parent/Guardian Email: </label>
                                <select name="guardian_email">%s</select>
                                <label for="subs">Number of Sub terms paid: </label>
                                <select id="subs" name="subs">
                                    <option value="0">0</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                </select>
                                <input type="submit" value="Update" id="submit">
                                </form>""" % (options)
                cursor.close()
                connection.close()
        else:
            result = '<p>Sorry you have not logged in! Go back to the homepage</p>'
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Update Subscriptions</title>
                <link rel="stylesheet" href="styles.css" />
            </head>
            <header>
              <h1>19th Waterford Ballygunner: Update Subs</h1>
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
