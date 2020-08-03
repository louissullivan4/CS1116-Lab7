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

form_data = FieldStorage()
section = ''
section_list = ["beavers","cubs","scouts","ventures"]
today = datetime.datetime.today()
beavernew = today.year - 5
beaverold = today.year - 8
beaverage1 = today.replace(beavernew)
beaverage2 = today.replace(beaverold)
cubnew = today.year - 8
cubold = today.year - 12
cubage1 = today.replace(cubnew)
cubage2 = today.replace(cubold)
scoutnew = today.year - 12
scoutold = today.year - 15
scoutage1 = today.replace(scoutnew)
scoutage2 = today.replace(scoutold)
venturenew = today.year - 15
ventureold = today.year - 18
ventureage1 = today.replace(venturenew)
ventureage2 = today.replace(ventureold)
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
                result = '<p>Please select a section</p>'
                section = escape(form_data.getfirst('section', '').strip())
                connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
                cursor = connection.cursor(db.cursors.DictCursor)
                if len(form_data) == 0:
                    result = ''
                else:
                    if section not in section_list:
                        result = '<p>Error! This does not exist.</p>'
                    else:
                        if section == 'beavers':
                            cursor.execute("""SELECT firstname, surname, birth, camping, backwoods, hillwalking, pioneering
                                              FROM ballygunnerskills
                                              WHERE birth <= %s AND birth >= %s
                                              ORDER BY birth DESC """, (beaverage1, beaverage2))
                            result = "<h2>Adventure Skills: Beavers</h2>"
                            result += '<table id="skills-table"><tr><th>Firstname</th><th>Surname</th><th>Camping</th><th>Backwoods</th><th>Hillwalking</th><th>Pioneering</th></tr>'
                            for row in cursor.fetchall():
                                result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['camping'], row['backwoods'], row['hillwalking'], row['pioneering'])
                            result += '</table>'
                        elif section =='cubs':
                            cursor.execute("""SELECT firstname, surname, birth, camping, backwoods, hillwalking, pioneering
                                              FROM ballygunnerskills
                                              WHERE birth <= %s AND birth >= %s
                                              ORDER BY birth DESC """, (cubage1, cubage2))
                            result = "<h2>Adventure Skills: Cubs</h2>"
                            result += '<table id="skills-table"><tr><th>Firstname</th><th>Surname</th><th>Camping</th><th>Backwoods</th><th>Hillwalking</th><th>Pioneering</th></tr>'
                            for row in cursor.fetchall():
                                result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['camping'], row['backwoods'], row['hillwalking'], row['pioneering'])
                            result += '</table>'
                        elif section =='scouts':
                            cursor.execute("""SELECT firstname, surname, birth, camping, backwoods, hillwalking, pioneering
                                              FROM ballygunnerskills
                                              WHERE birth <= %s AND birth >= %s
                                              ORDER BY birth DESC """, (scoutage1, scoutage2))
                            result = "<h2>Adventure Skills: Scouts</h2>"
                            result += '<table id="skills-table"><tr><th>Firstname</th><th>Surname</th><th>Camping</th><th>Backwoods</th><th>Hillwalking</th><th>Pioneering</th></tr>'
                            for row in cursor.fetchall():
                                result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['camping'], row['backwoods'], row['hillwalking'], row['pioneering'])
                            result += '</table>'
                        elif section =='ventures':
                            cursor.execute("""SELECT firstname, surname, birth, camping, backwoods, hillwalking, pioneering
                                              FROM ballygunnerskills
                                              WHERE birth <= %s AND birth >= %s
                                              ORDER BY birth DESC """, (ventureage1, ventureage2))
                            result = "<h2>Adventure Skills: Ventures</h2>"
                            result += '<table id="skills-table"><tr><th>Firstname</th><th>Surname</th><th>Camping</th><th>Backwoods</th><th>Hillwalking</th><th>Pioneering</th></tr>'
                            for row in cursor.fetchall():
                                result += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (row['firstname'], row['surname'], row['camping'], row['backwoods'], row['hillwalking'], row['pioneering'])
                            result += '</table>'
                        else:
                            result = '<p>Error! Please enter a valid section from the list.</p>'
                cursor.close()
                connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>Ballygunner Database: Adventure Skills</title>
                <link rel="stylesheet" href="styles.css">
            </head>
            <body>
                <header>
                  <h1>19th Waterford Ballygunner: Adventure </h1>
                </header>
        		<nav>
        			<ul>
        				<li><a href="home.py">Home</a></li>
        				<li><a href="beaver.py">Beavers</a></li>
        				<li><a href="cubs.py">Cubs</a></li>
        				<li><a href="scouts.py">Scouts</a></li>
                        <li><a href="ventures.py">Ventures</a></li>
                        <li><a href="logout.py">Logout</a></li>
        			</ul>
                </nav>
                <form action="skills.py" method="post">
                <select id="section" name="section">
                    <option value="beavers">Beavers</option>
                    <option value="cubs">Cubs</option>
                    <option value="scouts">Scouts</option>
                    <option value="ventures">Ventures</option>
                </select>
            <input type="submit" value="Find" id="submit"/>
        </form>
        %s
        <nav id="update">
            <ul>
                <li><a href="update_skills.py">Update Skills</a></li>
            </ul>
        </nav>
    </body>
</html>""" % (result))
