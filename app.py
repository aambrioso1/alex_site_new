from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
import os

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

@app.route('/', methods=['GET'])
def index():
	image_file = url_for('static', filename='img/first_algorithm.jpg')
	return render_template('index.html', image_file = image_file)

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
