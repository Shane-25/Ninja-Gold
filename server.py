from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)  
app.secret_key = 'Mellon'

@app.route('/')   
def index():
    if 'money' not in session:
            session['money'] = 0
    if 'counter' not in session:
            session['counter'] = 0
    if 'tracker' not in session:
            session['tracker'] = []
    return render_template("index.html", act=session['tracker'], len_act=len(session['tracker'])
)  

@app.route('/process_money', methods=["POST"])   
def money():
    time = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')
    x = request.form['which_form']
    if x == 'cave' and session['counter'] < 15 and session['money'] < 500:
        session['x'] = x
        new_value = random.randint(5,10)
        session['money'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    elif x == 'farm' and session['counter'] < 15 and session['money'] < 500:
        session['x'] = x
        new_value = random.randint(10,20)
        session['money'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    elif x == 'house' and session['counter'] < 15 and session['money'] < 500:
        session['x'] = x
        new_value = random.randint(2,5)
        session['money'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    elif x == 'casino' and session['counter'] < 15 and session['money'] < 500:
        session['x'] = x
        new_value = random.randint(-50,50)
        session['money'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    elif x == 'reset' or session['counter'] >= 15 or session['money'] > 500:
        session.clear()
    return redirect('/') 


if __name__=="__main__":   
    app.run(debug=True)   