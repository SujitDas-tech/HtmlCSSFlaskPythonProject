# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:21:36 2021

@author: 938306
"""

from flask import Flask,render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///my.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class My(db.Model):
	sno=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(20),nullable=False )
	name=db.Column(db.String(20),nullable=False)
	date_create=db.Column(db.DateTime, default=datetime.utcnow)
	def __repr__(self)-> str:
		return f"{self.sno}-{self.email}"
@app.route('/',methods=['GET','POST'])
def home():
	if request.method=="POST":
		email=request.form['Email']
		name=request.form['name']
		my = My(email=email,name=name)
		db.session.add(my)
		db.session.commit()
	allmy=My.query.all()
	return render_template("index.html",allmy=allmy)
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost')