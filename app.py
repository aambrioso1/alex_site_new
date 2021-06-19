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

@app.route('/', methods=['GET','POST'])
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

# Hockey API added to the site	
import requests, json

url = 'https://statsapi.web.nhl.com/api/v1/teams/' # URL for team data provided by the NHL
response = requests.get(url)
response.raise_for_status() # Verifies that we get a good response.

# Load json data into a Python variable.
data = json.loads(response.text)

# This creates a dictionary, new_teams_dict[int_id] = 'team_name', using the online API.
teams_dict = dict()
for i in range(1, len(data['teams'])+1):
	teams_dict[i] = data['teams'][i-1]['name']


@app.route('/API')
def API():
	return '<h1>Alex\'s Hockey API<h1></br> \
		Check if a team is in the NHL as follows:</br></br> \
		base_url/is_a_team/team_name</br></br> \
		Note the team name should be capitalized.</br> \
		For example:  Tampa Bay Lightning.'

@app.route('/API/is_a_team/<name>')
def user(name):
	print(name)
	if name in teams_dict.values():
		if name == 'Tampa Bay Lightning':
			return f'<h1>The Tampa Bay Lightning is the best team in the NHL!!!</h1>'
		else:
			return f'<h1>The {name} IS an NHL team.</h1>'
	return f'<h1>{name} is NOT an NHL team.</h1>'


@app.route('/my_book', methods=['GET','POST'])
def go_to_my_book(path='index.html'):
    return app.send_static_file(path)

"""
This SO answer was helpful:
https://stackoverflow.com/questions/14912787/sphinx-documentation-inside-a-flask-running-web-application

Note that reassigning the name of the static folder can be problematic if you are adding a sphinx 
document to an existing app.   My solution for now was to but all of the Sphinx files directly in
the static folder.
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)

