'''
A simple sample web application using Flask. Demonstrates the basics of routes, as well
as how to use forms with Flask.

CS 257, Winter 2023
'''

import flask
from flask import render_template, request
import json
import sys
sys.path.append('../Backend/')
from api import EnergyProductionAPI


app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    '''
    Simplest example: print something in the browser
    '''
    return render_template('home.html')

@app.route('/theData', methods=['POST', 'GET'])
def theData():
    '''
    
    '''
    energy = EnergyProductionAPI()
    selectedState = None
    totalEnergy = None
    totalRenewableEnergy = None
    totalEnergyByMonth = None
    totalEnergyByCategory = None
    categories = None
    categoryValue = None
    

    if request.method == 'POST':
        #Getting data from form
        selectedState = request.form["statesSelect"]

        #Call the api with the data retrieved
        totalEnergy = energy.getEnergyForState(selectedState)
        totalRenewableEnergy = energy.getTotalRenewableEnergyByState(selectedState)
        totalEnergyByMonth = energy.getTotalEnergyForStateByMonth(selectedState)
        totalEnergyByCategory = energy.getEnergyByCategoryForState(selectedState)

        categories = totalEnergyByCategory.keys()
        categoryValue = totalEnergyByCategory.values()
        
        
    
    return render_template('the_data.html', selectedState = selectedState, totalEnergy = totalEnergy, 
    totalRenewableEnergy = totalRenewableEnergy, totalEnergyByMonth = totalEnergyByMonth, categories = categories, categoryValue = categoryValue)

@app.route('/aboutTheData')
def aboutTheData():
    
    return render_template('about_the_data.html')

"""Code can be run with 'python3 webapp.py perlman.mathcs.carleton.edu [ port# ]'"""
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
