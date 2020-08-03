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
                cursor.execute("""SELECT *
                                  FROM ballygunnerskills
                                  ORDER BY firstname ASC""")
                if cursor.rowcount == 0:
                    result = '<p>Sorry. There are no youth members at present.</p>'
                else:
                    option1 = ''
                    option2 = ''
                    for row in cursor.fetchall():
                        option1 += '<option value="%s">%s</option>' % (row['firstname'], row['firstname'])
                        option2 += '<option value="%s">%s</option>' % (row['surname'], row['surname'])
                    result = """<form action="run_skills.py" method="post" id="update">
                                <label for="firtname">Firstname: </label>
                                <select name="firstname">%s</select>
                                <label for="surname">Surname: </label>
                                <select name="surname">%s</select>
                                <label for="camping">Camping Level: </label>
                                <select id="camping" name="camping">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                    <option value="8">8</option>
                                    <option value="9">9</option>
                                </select>
                                <label for="backwoods">Backwoods Level: </label>
                                <select id="backwoods" name="backwoods">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                    <option value="8">8</option>
                                    <option value="9">9</option>
                                </select>
                                <label for="hillwalking">Hillwalking Level: </label>
                                <select id="hillwalking" name="hillwalking">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                    <option value="8">8</option>
                                    <option value="9">9</option>
                                </select>
                                <label for="pioneering">Pioneering Level: </label>
                                <select id="pioneering" name="pioneering">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                    <option value="6">6</option>
                                    <option value="7">7</option>
                                    <option value="8">8</option>
                                    <option value="9">9</option>
                                </select>
                                <input type="submit" value="Update" id="submit">
                                </form>""" % (option1, option2)
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
                <title>Update Skills</title>
                <link rel="stylesheet" href="styles.css" />
            </head>
            <header>
              <h1>19th Waterford Ballygunner: Update Adventure Skills</h1>
            </header>
            <body>
            <nav>
                <ul>
                    <li><a href="home.py">Home</a></li>
                    <li><a href="skills.py">Adventure Skills</a></li>
                    <li><a href="leaders.py">Leaders</a></li>
                    </li><li><a href="logout.py">Logout</a></li>
                </ul>
            </nav>
                %s
            </body>
            </html>""" % (result))
