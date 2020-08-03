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
firstname = ''
surname = ''
gender = ''
address = ''
contact = ''
email = ''
garda_vetted = ''
training_level = ''
result = ''

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
                    gender = escape(form_data.getfirst('gender', '')).strip()
                    address = escape(form_data.getfirst('address', '')).strip()
                    contact = escape(form_data.getfirst('contact', '')).strip()
                    email = escape(form_data.getfirst('email', '')).strip()
                    garda_vetted = escape(form_data.getfirst('garda_vetted', '')).strip()
                    training_level = escape(form_data.getfirst('training_level', '')).strip()


                    connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                    cursor = connection.cursor(db.cursors.DictCursor)
                    cursor.execute("""SELECT email FROM ballygunnerleaders
                                        WHERE email = %s""", email)
                    if cursor.rowcount == 0:
                        cursor.execute("""INSERT INTO ballygunnerleaders (firstname, surname, gender, address, contact, email, garda_vetted, training_level)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (firstname, surname, gender, address, contact, email, garda_vetted, training_level))
                        connection.commit()
                        result = '<p>Successfully added!</p>'
                    else:
                        result = '<p>Error! This leader has already been entered.</p>'
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
                    <meta charset="utf-8" />
                    <title>Ballygunner Database: Add Leaders</title>
                    <link rel="stylesheet" href="styles.css">
                </head>
                <header>
                  <h1>19th Waterford Ballygunner: Update Leaders</h1>
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
                        <form action="add_leader.py" method="post" id="add">
                        <label for="firstname">Forename: </label>
                        <input type="text" name="firstname" value="%s" size="50" maxlength="50" id="firstname" />
                        <label for="surname">Surname: </label>
                        <input type="text" name="surname" value="%s" size="50" maxlength="50" id="surname" />
                        <label for="gender">Gender: </label>
                        <input type="text" name="gender" value="%s" size="50" maxlength="50" id="gender" />
                        <label for="address">Full Address: </label>
                        <input type="text" name="address" value="%s" size="50" maxlength="50" id="address" />
                        <label for="contact">Contact Number: </label>
                        <input type="tel" name="contact" value="%s" size="50" maxlength="50" id="contact" />
                        <label for="email">Email Address : </label>
                        <input type="email" name="email" value="%s" size="50" maxlength="50" id="email" />
                        <label for="garda_vetted">Date of Garda Vetting:  </label>
                        <input type="date" name="garda_vetted" value="%s" id="garda_vetted" />
                        <label for="training_level">Training Complete: </label>
                        <select name="training_level">
                            <option value="Gilwell Woggle">Gilwell Woggle</option>
                            <option value="Wood Badge Pin">Wood Badge Pin</option>
                            <option value="Wood Badge Beads">Wood Badge Beads</option>
                        </select>
                        <input type="submit" value="Update" id="submit"/>
                    </form>
            </body>
    </html>""" % (result, firstname, surname, gender, address, contact, email, garda_vetted))
