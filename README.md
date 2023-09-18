# Azure and Flask Deployment - HHA 504 Week 2

## Python Code
1. From the WK2/flaskapp_0 file, utilize the app.py, requirements.txt, and templates folders in your google shell environment
2. The app.py file uses flask to create a template for an html website:
3. Import flask and pandas


       from flask import Flask, render_template
       import pandas as pd

4. This step displays the base webpage and the about tab

       app = Flask(__name__)

          @app.route('/')
          def index():
              return render_template('base.html')

          @app.route('/about')
          def about():
              return render_template('about.html')

5. Import the data file using the pandas read_csv function

        df = pd.read_csv('ComplicationsAndDeathsNY.csv')

6. This step was edited to ensure that all data was displayed in the data tab, not just a random sample.
       
            @app.route('/data')
            def data(data=df):
                data = data
                return render_template('data.html', data=data)

        if __name__ == '__main__':
            app.run(
                debug=True,
                port=8080
            )


### HTML File
      
## Azure

## URL to Flask Application
https://riannehha504wk2.azurewebsites.net/data
