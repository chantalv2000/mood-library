import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo
from app.models import mood, formopener
from app.models import quotes, formopener

# name of database
app.config['MONGO_DBNAME'] = 'mood-library' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:vC9xrh0zCE4JtU6q@cluster0-svmc2.mongodb.net/mood-library?retryWrites=true&w=majority' 
 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def template():
    collection= mongo.db.mood
    #Find everything in the collection and store as a dictionary in events
    mood=collection.find({})
    
    return render_template('test.html',mood=mood)

# ADD SONGS

@app.route('/add')

def add():
    # define a variable for the collection you want to connect to
    user= mongo.db.users
    # insert new data
    user.insert({'name':'Grace'})
    # return a message to the user
    
    userdata = dict(request.form)
    print (userdata)
    name = userdata['nickname']
    return render_template('template.html', name = name)

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
@app.route("/test")
def test():
    return render_template("test.html")
@app.route("/test1")
def test1():
    return render_template("test1.html")


    