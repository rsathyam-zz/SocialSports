import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class HomePage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
		<!DOCTYPE html>
          	<html lang="en">
		<head>
		<meta charset="utf-8" />
		<title>SocialSports</title>
	   	<link rel="stylesheet" href="HomePage.css" type="text/css" />
		</head>
		<body id="index" class="home">
			<header id="banner" class="body">
			<h1><a href="#">Social Sports!</a></h1>
			<nav>
			  <ul> 					    
			   <li class="active"><a href="#">Create/Edit a League</a></li>  
		           <li><a href="#">Signup for a League Game</a></li> 
			  </ul>
                        </nav>  
			</header><!-- /#banner -->
		</body>
                </html>""")
