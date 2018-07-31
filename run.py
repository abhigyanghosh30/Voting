from flask import Flask, session, render_template, request, redirect, url_for, Response, json, g, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(67)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
db = SQLAlchemy(app)

class Votes(db.Model):
	__tablename__ = 'votes'

	name = db.Column(db.String(100), primary_key=True, nullable=False)
	votes = db.Column(db.Integer, nullable=False, default=0)



@app.route('/home')
@app.route('/')
def main():
	try:
		if session['vote']:
			pass
		else:
			pass
	except:
		session['vote'] = True
	finally:
		return render_template('voting.html',vote=session['vote'])

@app.route('/team1',methods=['POST'])
def team1():
	if session['vote']:
		session['vote'] = False
		team1 = Votes.query.filter_by(name="Team 1").first()
		team1.votes += 1
		db.session.commit()
	return redirect('/home')

@app.route('/team2',methods=['POST'])
def team2():
	if session['vote']:
		session['vote'] = False
		team1 = Votes.query.filter_by(name="Team 2").first()
		team1.votes += 1
		db.session.commit()
	return redirect('/home')

@app.route('/team3',methods=['POST'])
def team3():
	if session['vote']:
		session['vote'] = False
		team1 = Votes.query.filter_by(name="Team 3").first()
		team1.votes += 1
		db.session.commit()
	return redirect('/home')


if __name__ == "__main__":
	app.run(port=80,debug=True)