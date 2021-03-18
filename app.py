from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))


app = Flask(__name__)
# moment = Moment(app)
bootstrap = Bootstrap(app)

"""
# This configuration will make the app less hackable.
app.config["ADMIN_PASSWORD"] = os.environ.get("ADMIN_PASSWORD")
"""

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

"""
@app.route('/about')
def about():
	return render_template('about.html')
"""

"""
@app.route('/blog')
def blog():
	return render_template('blog.html')
	# return '<html><a href="http://alexambrioso.com">Go to Alex's Blog</a></html>'
"""

@app.route('/desmos')
def desmos():
	return render_template('desmos.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
