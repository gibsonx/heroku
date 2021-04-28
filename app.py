#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/Pickle_RL_Model.pkl', 'rb') as f:
    logistic = pickle.load(f)

def get_predictions(req_model, age, sex, cp, trestbps, fbs):
    mylist = [age, sex, cp, trestbps, fbs]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        fbs = request.form['fbs']

        req_model = request.form['req_model']

        target = get_predictions(req_model, age, sex, cp, trestbps, fbs)

        if target==1:
            type = 'Patient has this disease'
        else:
            type = 'Patient has not this disease'

        return render_template('home.html', target = target, type = type)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)