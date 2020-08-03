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


result = """<p>Sorry you have not logged in! Go back to the homepage or Login</p>
            <p id="login"><a href="home.py">Home</a></p>
            <p id="login"><a href="login.py">Login</a></p>"""
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                result = """
                <body>
            		<nav>
            			<ul>
                              <li><a href="beaver.py">Beavers</a></li>
                              <li><a href="cubs.py">Cubs</a></li>
                              <li><a href="scouts.py">Scouts</a></li>
                              <li><a href="ventures.py">Ventures</a></li>
                              <li><a href="leaders.py">Leaders</a></li>
            			</ul>
            		</nav>
            		<main>
            		<section>
            			<h2>Introduction</h2>
            				<p>
                                  Welcome to the 19th Waterford Ballygunner Scout Group Database.
                                  Click on the login above.
                                  DON'T FORGET TO LOGOUT!!
            				</p>
            		</section>
                <aside>
                  <section>
                    <figure>
                        <img src="camp.jpg" title="Wood"
                            alt="A tent in the background with a row of timber in front of it." />
                    </figure>
                  </section>
                </aside>
            	</main>"""
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Ballygunner Database</title>
            <link rel="stylesheet" href="styles.css" />
        </head>
        <header>
          <h1>19th Waterford Ballygunner Database</h1>
        </header>
        <body>
        %s
    	</body>
    </html>""" % (result))
