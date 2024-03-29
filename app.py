from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
import os

app = Flask(__name__, static_url_path='/', static_folder='static/html')
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
	return render_template('main_index.html', image_file = image_file)
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

# Redo this root for presentations:  https://github.com/aambrioso1/presentations
@app.route('/desmos')
def desmos():
	return render_template('desmos.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

"""
@app.route('/pyscript')
def pyscript():
	return render_template('compute_pi_script.html')
"""

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


@app.route('/index', methods=['GET','POST'])
def go_to_my_book(path='index.html'):
    return app.send_static_file(path)


@app.route('/pyscript')
def pyscript(path='compute_pi_script.html'):
	return app.send_static_file(path)
"""

@app.route('/pyscript')
def pyscript():
	return f'<head> \
    	<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> \
   		<script defer src="https://pyscript.net/alpha/pyscript.js"></script> \
		</head> \
		<body> \
      	<py-script> \
		print("Let\'s compute π:") \
		def wallis(n): \
    		pi = 2 \
    		for i in range(1,n): \
        		pi *= 4 * i ** 2 / (4 * i ** 2 - 1) \
    		return pi \
		pi = wallis(100) \
		s = f"π is approximately {pi:.3f}" \
		print(pi) \
      	</py-script> \
  		</body>'
"""
"""
This SO answer was helpful:
https://stackoverflow.com/questions/14912787/sphinx-documentation-inside-a-flask-running-web-application

Need to resolve the issue with the table of contents page of book
"""

if __name__ == '__main__':
    app.run(debug=True, port=5001)

