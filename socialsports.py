from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import homepage
import login

application = webapp.WSGIApplication( [('/', homepage.HomePage)],
				      [('/login', login.Login)])

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
