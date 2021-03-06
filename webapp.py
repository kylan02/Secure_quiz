import os
from flask import Flask, url_for, render_template, request, Markup
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #SECRET_KEY is an environment variable.  
                                         #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    print(session)
    session.clear()
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    #TODO: delete everything from the session
    session.clear()
    return redirect('/')

@app.route('/page1')
def renderPage1():
  return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    #TODO: save the first and last name in the session
    if "question_1" not in session:
      session["question_1"]= request.form["question1"]
    return render_template('page2.html')
  
@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #TODO: save the first and last name in the session
    if "question_2" not in session:
      session["question_2"]= request.form["question2"]
    return render_template('page3.html')
  
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    #TODO: save the first and last name in the session
    if "question_3" not in session:
      session["question_3"]= request.form["question3"]
    return render_template('page4.html')

@app.route('/finalPage',methods=['GET','POST'])
def renderFinalPage():
    #TODO: save the favorite color in the session
    if "question_1" not in session:
      return render_template('finalPage.html', response = "you cannot access your old scores, please restart")
    if "question_4" not in session:
      session["question_4"]= request.form["question4"]
    return render_template('finalPage.html', response = score())
  
def score():
  answers= {"Broccoli" : session["question_1"], "Q": session["question_2"], "5" : session["question_3"], "1300000": session["question_4"]}
  totalCorrect=0
  feedback=""
  for a in answers:
    feedback+=   Markup("<p>"+ questionScoreDisplay(answers[a], a) + "</p>")
    if a == answers[a]:
      totalCorrect+=1
  feedback += Markup("<p>"+ "Total score: " + str(totalCorrect) + "/4" + "</p>")
  return feedback
  
def questionScoreDisplay(yourAnswer, correctAnswer):
  toReturn = "You Answered: " + yourAnswer
  if yourAnswer!=correctAnswer:
    toReturn+= ". That is incorrect, the correct answer is " + correctAnswer + ".\n "
    return toReturn
  toReturn+= ". That is correct!"
  return toReturn
  
    
if __name__=="__main__":
    app.run(debug=False)
