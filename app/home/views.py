from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
@login_required
def homepage():
	"""
		Render the homepage template on the / route
	"""
	return render_template("home/a_homepage.html", title="Welcome")


@home.route("/a_homepage")
@login_required
def a_homepage():
	"""
		Render the dashboard template on the /dashboard route
	"""

	return render_template('home/a_homepage.html', title="Homepage Admin")
