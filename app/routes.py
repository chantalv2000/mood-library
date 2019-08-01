import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo
from app.models import mood, formopener
from app.models import quotes, formopener

# name of database
app.config['MONGO_DBNAME'] = 'database' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:v04NIkH7GUrqmjy9@cluster0-kwjfj.mongodb.net/database?retryWrites=true&w=majority'
 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index',methods=["GET","POST"])
def template():
    users= mongo.db.users
    #Find everything in the collection and store as a dictionary in events
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.insert({'username': username,'password': password,'playlist': []})
    return render_template('test.html',users=users)

# ADD SONGS

@app.route('/signup')
def signup():
    user = mongo.db.users
    users = user.find({})
    print(users)
    return render_template('signup.html')

@app.route('/login')
def login():
    user = mongo.db.users
    users = user.find({})
    return render_template('login.html')

@app.route("/mood",methods=["GET", "POST"])
def new_quote():
    #mooddb = mongo.db.mood
    userdata = dict(request.form)
    print (userdata)
    
    
    if request.method == "GET":
        return "Use the Form!"
    else:
        nickname = userdata['nickname']
        moodd = request.form['mood']
        genre = request.form['genre']
        recommendation = mood.moodCalculator(moodd, genre)
        print (mood, genre, recommendation)
        
        return render_template('test1.html', mood = mood, recommendation = recommendation, genre = genre, nickname = nickname)

@app.route("/quotes",methods=["GET", "POST"])
def new_quotes():
    #mooddb = mongo.db.quotes
    userdata = dict(request.form)
    print (userdata)
    
    
    if request.method == "GET":
        return render_template('quotes.html')
    else:
        nickname = userdata['nickname']
        moodd = request.form['mood']
        quote = quotes.quotesCalculator(moodd)
        print (mood, quote)
        
        return render_template('quotes1.html', mood = mood, quote=quote, nickname = nickname)       
@app.route("/playlist", methods=['GET'])
def playlist():
    pl= mongo.db.playlist
    pl = pl.find({})
    return render_template("playlist.html",pl = pl)
@app.route("/test1")
def test1():
    return render_template("test1.html")


    