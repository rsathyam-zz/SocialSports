from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import HomePage

application = webapp.WSGIApplication( [('/', HomePage.HomePage)],
					debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
