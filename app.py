# start by importing flask, then importing two modules from flask
from flask import Flask, render_template
import pandas as pd
import random
from faker import Faker
import random_address

faker = Faker()

# Flask is the main module
# render_template allows us to use html

# This line is always included in Flask code
app = Flask(__name__)

#route indicates address
# '/' indicates our home page
@app.route('/')

# function name can be anything
def mainpage():
    return render_template('base.html')
# anything in html needs a folder (templates)
#then create a base.html file under templates folder

@app.route('/about')
def aboutpage():
    return render_template('about.html')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_504_2023/main/WK1/data/113243405_StonyBrookSouthamptonHospital_StandardCharges.csv')
@app.route('/data')
def data(data=df):
    data = data.sample(15)
    return render_template('data.html', data=data)

@app.route('/random')
def randomnumber():
    number_var = random.randint(1,10000)
    fake_address = faker.random_address()

    return render_template('randomn.html', single_number = number_var, single_address = fake_address)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8081
    )


    # Run python app.py in the CLI
    # Click on the IP address for the link to the website
    # Curly brackers {} allow python to be inserted into html


    # az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1> 
    #add groupname ; appname' python 3.9 ; sku is the size can put B1 or free or F1?
    # resource group links to billing 

    #az webapp up --resource-group Rianne504 --name HHA504_Flask_RBonitto --runtime PYTHON:3.9 --sku B1 

    #to push updates az webapp up