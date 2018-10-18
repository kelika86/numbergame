from flask import Flask, render_template, request, redirect, session
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def number():
    session['number']=random.randrange(0,101)
    print (session['number'])
    return render_template('numbergame.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess=int(request.form["guess"])
    print (guess)
    if guess<session['number']:
        check="low"
    elif guess > session['number']:
        check="high"
    else: 
        check="correct"
        session.clear()
    return render_template('guess.html', check=check)




app.run(debug=True)