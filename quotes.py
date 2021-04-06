from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:1.21gigowatt@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://oheclgqnhrqunx:d19ab7a33881f081a7d9ac430768d5f6fd9505480c7e419a542aaf17e06ff48f@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d3so1kt5rki95o'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        author = db.Column(db.String(30))
        quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
