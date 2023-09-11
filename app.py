# start by importing flask, then importing two modules from flask
from flask import Flask, render_template
import pandas as pd
# Flask is the main module
# render_template allows us to use html

# This line is always included in Flask code
app = Flask(__name__)

#route indicates address
# '/' indicates our home page
@app.route('/')

# function name can be anything
def index():
    return render_template('base.html')
# anything in html needs a folder (templates)
#then create a base.html file under templates folder

@app.route('/about')
def about():
    return render_template('about.html')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )