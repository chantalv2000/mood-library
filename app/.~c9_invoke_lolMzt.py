import os
from app import app
from flask import render_template, request, redirect, session
from flask_pymongo import PyMongo
from app.models import mood, formopener
from app.models import quotes, formopener

# name of database
app.config['MONGO_DBNAME'] = 'database' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:v04NIkH7GUrqmjy9@cluster0-kwjfj.mongodb.net/database?retryWrites=true&w=majority'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

mongo = PyMongo(app)


# INDEX

@app.route('/')

@app.route('/index',methods=["GET","POST"])
def template():
    users= mongo.db.users
    #Find everything in the collection and store as a dictionary in events
    if request.method == 'POST':
        username = request.form['username']
        session['username']=request.form['username']
        password = request.form['password']
        users.insert({'username': username,'password': password,'playlist': []})
    return render_template('test.html',users=users)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' : request.form['password']})
            session['username'] = request.form['username']
            return redirect('/')
        return 'That username already exists! Try logging in.'
    return render_template('signup.html')   
@app.route('/login', methods=['GET'])
def send_to_login():
    return render_template('login.html')
    
@app.route('/login/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    # print (login_user)
    if login_user:
        # print(login_user['password'])
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            #collection = mongo.db.events
            #eventsDB = collection.find({})
            #return render_template('page1.html', events = eventsDB)
            return render_template('test.html')
            

    return render_template('signup.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
# ADD SONGS


@app.route('/add/<recommendation>', methods=['GET',"POST"])
def add(recommendation):
    if request.method=="GET":
        return "go to home"
    else:
        pl= mongo.db.users
        pl = pl.find_one({'username':session['username']})
        print (pl)
    # myquery = { "address": "Valley 345" }
    # newvalues = { "$set": { "address": "Canyon 123" } }
    # pl.update_one(username, newvalues)
    return render_template("playlist.html",pl = pl)
    
@app.route("/mood",methods=["GET", "POST"])
def new_quote():
    #mooddb = mongo.db.mood
    userdata = dict(request.form)
    print (userdata)

    if request.method == "GET":
        return render_template('test1.html')
    else:
        nickname = userdata['nickname']
        moodd = request.form['mood']
        genre = request.form['genre']
        recommendation = mood.moodCalculator(moodd, genre)
        print (mood, genre, recommendation)
        
        return render_template('test1.html', moodd = moodd, recommendation = recommendation, genre = genre, nickname = nickname)

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
    print ("hi")
    return render_template("playlist.html",pl = pl)
    
@app.route("/test1")
def test1():
    return render_template("test1.html")

@app.route("/feedback", methods=['GET'])
def feedback():
    userdata = dict(request.form)
    print (userdata)
    if request.method == "GET":
        return render_template("feedback1.html")
    else:
        name = userdata['name']
        return render_template("feedback1.html", name=name)

@app.route("/quotesfeedback", methods=['GET'])
def quotesfeedback():
    userdata = dict(request.form)
    print (userdata)
    if request.method == "GET":
        return render_template("feedback2.html")
    else:
        name = userdata['name']
        return render_template("feedback2.html", name=name)
