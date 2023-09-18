# Azure and Flask Deployment - HHA 504 Week 2

## Python Code
1. From the WK2/flaskapp_0 file, utilize the app.py, requirements.txt, and templates folders in the google shell environment

   The app.py file uses flask to create a template for an html website
2. Import flask and pandas


       from flask import Flask, render_template
       import pandas as pd

3. This step displays the base webpage and the about tab

       app = Flask(__name__)

          @app.route('/')
          def index():
              return render_template('base.html')

          @app.route('/about')
          def about():
              return render_template('about.html')

4. Import the data file using the pandas read_csv function

        df = pd.read_csv('ComplicationsAndDeathsNY.csv')

5. This step was edited to ensure that all data was displayed in the data tab, not just a random sample.
       
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
1. There are three html files included in the templates folder: about.html, base.html and data.html. Click into the base.html file
2. Edit the title of the base html file. This changes what is displayed as the title of the page.

              <!DOCTYPE html>
              <html lang="en">

              <head>
                  <meta charset="UTF-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1.0">
                  <title> New York Hospitals - Complications and Deaths </title>
    
                  <!-- Tailwind CSS via CDN -->
                  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
              </head>

              <body class="bg-white-200">


  3. Change the header and footer colors to green, and change the nane of the header and footer of the page to match the application

                  <header class="bg-green-600 text-white p-4">
                      <h1 class="text-2xl">Welcome to The New York Hospitals Complications and Deaths Application</h1>
                      <nav>
                          <ul class="flex space-x-4">
                              <li><a href="/" class="hover:underline">Home</a></li>
                              <li><a href="/about" class="hover:underline">About</a></li>
                              <li><a href="/data" class="hover:underline">Data</a></li>
                          </ul>
                      </nav>
                  </header>

                  <main class="p-4">

                      {% block content %}{% endblock %}

                  </main>

                  <footer class="bg-green-600 text-white p-4 mt-6">
                      <p>© 2023 The New York Hospitals Complications and Deaths Application. All Rights Reserved.</p>
                  </footer>
              </body>

              </html>


4. In the about.html tab, change the color of the header to gray, and change the text under the "About" header to match the new application description

          {% extends "base.html" %} 

          {% block content %}

          <header class="bg-gray-600 text-white p-4">
                 <section class="mb-6">
                      <h2 class="text-xl mb-2">About</h2>
                        <p>This application displays the complications and deaths in New York hospitals as reported by CMS.</p>
    
                  </section>


5. In the about.html tab, change the color of the header to gray, and change the text under the "Features" header to match the new application

                  <section>
                      <h2 class="text-xl mb-2">Features</h2>
                      <ul class="list-disc pl-5">
                          <li>Comparisons between hospitals by city </li>
                          <li>Comparisons to the National Rate</li>

                      </ul>
   
                  </section>
       

              {% endblock %}

6. In the data.html file, change the names of the columns displayed from the dataframe

              {% extends "base.html" %} 

              {% block content %}

                  <section>
                      <h2 class="text-xl mb-2"> New York Hospital Complications and Deaths: A CMS Dataset </h2>
                      <table class="table-auto">
                          <thead>
                              <tr>
                                  <th class="px-4 py-2">FacilityName</th>
                                  <th class="px-4 py-2">CityTown</th>
                                  <th class="px-4 py-2">MeasureID</th>
                                  <th class="px-4 py-2">MeasureName</th>
                                  <th class="px-4 py-2">ComparedToNational</th>
                                  <th class="px-4 py-2">Denominator</th>
                                  <th class="px-4 py-2">Score</th>
                                  <th class="px-4 py-2">LowerEnd</th>
                                  <th class="px-4 py-2">HigherEnd</th>

                              </tr>

7. Change the location, for example data[1], of the column to match the new column names in from the data file
                
                          </thead>
                          <tbody>
                              {% for data in data.values %}
                              <tr>
                                  <td class="border px-4 py-2">{{ data[1] }}</td>
                                  <td class="border px-4 py-2">{{ data[3] }}</td>
                                  <td class="border px-4 py-2">{{ data[8] }}</td>
                                  <td class="border px-4 py-2">{{ data[9] }}</td>
                                  <td class="border px-4 py-2">{{ data[10] }}</td>
                                  <td class="border px-4 py-2">{{ data[11] }}</td>
                                  <td class="border px-4 py-2">{{ data[12] }}</td>
                                  <td class="border px-4 py-2">{{ data[13] }}</td>
                                  <td class="border px-4 py-2">{{ data[14] }}</td>
                              </tr>
                              {% endfor %}
                          </tbody>
                      </table>
                  </section>

              {% endblock %}
   


## Azure
### Azure installation in google shell
1. Within the google shell environment's CLI, type in:

            curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

2. When the installation is finished, type in Az to access the Azure CLI
3. To access your azure account, type in:


           az login --use-device-code 

4. To connect to the appropriate resource group enter in this format:

            az webapp up --resource-group (enter resource group) --name (enter name) --runtime PYTHON:3.9 --sku F1

5. Enter az webapp up to push any updates to the Azure webpage. The weblink is located in the az CLI.

## URL to Flask Application
https://riannehha504wk2.azurewebsites.net/data
