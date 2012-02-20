from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import os

class Login(webapp.RequestHandler):
    def get(self):
	path = os.path.join(os.path.dirname(__file__), "html/login.html")
	self.response.out.write(template.render(path,{}))
