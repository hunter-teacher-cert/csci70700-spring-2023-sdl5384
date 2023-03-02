from flask import Flask
from flask import render_template
import random as r
from flask import session, request

app = Flask(__name__)
app.secret_key="random nonsense"

@app.route('/')
def welcomePage():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] = session["count"] + 1
    return render_template("welcome_page.html",session=session)

@app.route('/login/',methods=['GET','POST'])
def logInToPage():
    if "todo_list" not in session:
        session["todo_list"] = []
    

    if request.form['submit'] == 'doit':
        l = session["todo_list"]
        l.append(item)
        session["todo_list"] = l

    else:
        session["todo_list"] = []
        
    return render_template("login_html",todos=session["todo_list"])

@app.route('/rollTheDice/')
def rollTheDice():
    # msg = "The numbers you rolled are the following: "
    # die = []
    # for i in range(0,15):
    #     die.append(r.randint(1,6))
    #     msg = msg + "2 " + session["die3"] + session["die4"] + session["die5"] + str(die[i])

    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] = session["count"] + 1

    if "diceAvg" not in session:
        session["diceAvg"] = 0

    if "die1" not in session or "die2" not in session or "die3" not in session or "die4" not in session or "die5" not in session:
        session["die1"] = 0
        session["die2"] = 0
        session["die3"] = 0
        session["die4"] = 0
        session["die5"] = 0
    else:
        session["die1"] = r.randint(1,6)
        session["die2"] = r.randint(1,6)
        session["die3"] = r.randint(1,6)
        session["die4"] = r.randint(1,6)
        session["die5"] = r.randint(1,6)

        session["diceAvg"] = session["diceAvg"] + 1
        
    return render_template("diceSimulation.html",session=session)

app.run(host='0.0.0.0', port=5000)