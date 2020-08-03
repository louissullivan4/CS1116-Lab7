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
section = ''
firstname = ''
surname = ''
birth = ''
gender = ''
address = ''
guardian_number = ''
guardian_email = ''
guardian_fname = ''
guardian_sname = ''
sub = ''
camping = '0'
backwoods = '0'
hillwalking = '0'
pioneering = '0'
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
                    birth = escape(form_data.getfirst('birth', '')).strip()
                    gender = escape(form_data.getfirst('gender', '')).strip()
                    address = escape(form_data.getfirst('address', '')).strip()
                    guardian_fname = escape(form_data.getfirst('guardian_fname', '')).strip()
                    guardian_sname = escape(form_data.getfirst('guardian_sname', '')).strip()
                    guardian_number = escape(form_data.getfirst('guardian_number', '')).strip()
                    guardian_email = escape(form_data.getfirst('guardian_email', '')).strip()
                    subs = escape(form_data.getfirst('subs', '')).strip()
                    connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                    cursor = connection.cursor(db.cursors.DictCursor)
                    cursor.execute("""SELECT firstname, surname FROM ballygunnerscouts
                                        WHERE firstname = %s and surname = %s""", (firstname, surname))
                    if cursor.rowcount == 0:
                        cursor.execute("""INSERT INTO ballygunnerscouts (firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email, subs)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email, subs))
                        connection.commit()
                        cursor.execute("""INSERT INTO ballygunnerskills (firstname, surname, birth, camping, backwoods, hillwalking, pioneering)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s)""", (firstname, surname, birth, camping, backwoods, hillwalking, pioneering))
                        connection.commit()
                        result = '<p>Successfully added!</p>'
                    else:
                        result = '<p>Error! There is already a youth member with this firstname and surname. Pease add their middle name to the surname box.</p>'
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
                    <title>Ballygunner Database: Add Scouts</title>
                    <link rel="stylesheet" href="styles.css">
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
                            </li><li><a href="logout.py">Logout</a></li>
            			</ul>
                    </nav>
                    %s
            <form action="add_scout.py" method="post" id="add">
                <label for="firstname">Forename: </label>
                <input type="text" name="firstname" value="%s" size="50" maxlength="50" id="firstname" />
                <label for="surname">Surname: </label>
                <input type="text" name="surname" value="%s" size="50" maxlength="50" id="surname" />
                <label for="birth">Date of Birth: </label>
                <input type="date" name="birth" value="%s" id="birth" />
                <label for="gender">Gender: </label>
                <input type="text" name="gender" value="%s" size="50" maxlength="50" id="gender" />
                <label for="address">Full Address: </label>
                <input type="text" name="address" value="%s" size="50" maxlength="50" id="address" />
                <label for="guardian_fname">Next of Kin Forename: </label>
                <input type="text" name="guardian_fname" value="%s" size="50" maxlength="50" id="guardian_fname" />
                <label for="guardian_sname">Next of Kin Surname: </label>
                <input type="text" name="guardian_sname" value="%s" size="50" maxlength="50" id="guardian_sname" />
                <label for="guardian_number">Next of Kin Phone Number: </label>
                <input type="tel" name="guardian_number" value="%s" size="50" maxlength="50" id="guardian_number" />
                <label for="guardian_email">Next of Kin Email Address : </label>
                <input type="email" name="guardian_email" value="%s" size="50" maxlength="50" id="guardian_email" />
                <label for="subs">Number of Sub terms paid: </label>
                <select id="subs" name="subs">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
                <input type="submit" value="Update" id="submit"/>
            </form>
        </body>
    </html>""" % (result, firstname, surname, birth, gender, address, guardian_fname, guardian_sname, guardian_number, guardian_email))
