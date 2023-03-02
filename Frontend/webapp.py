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
    result = None
    totalEnergy = None

    if request.method == 'POST':
        result = request.form
        # totalEnergy = energy.getEnergyForState(result.statesSelect)
        print(result)

        # Here is where you would call one or more database methods with the form data.
    

    
    return render_template('the_data.html', result = result, totalEnergy = totalEnergy)

@app.route('/aboutTheData')
def aboutTheData():
    
    return render_template('about_the_data.html')

# @app.route('/helloAgain')
# def templateHome():
#     '''
#     Demonstration of rendering an HTML template on the fly, with no variables.
#     '''
#     return render_template('hello.html')

# @app.route('/fancyHello')
# def fancyHome():
#     '''
#     Demonstration of rendering an HTML template on the fly, where the HTML template 
#     contains a stylesheet and an image
#     '''
#     return render_template('fancyHello.html')

# @app.route('/greet/<person>/')
# def greet(person):
#     '''
#     Demonstration of passing a parameter into a template.
#     '''
#     return render_template('greet.html',
#                            person=person)

# @app.route('/bigGreet/', methods=['GET'])
# def greetAgain():
#     '''
#     Demonstration of passing multiple parameters into a template.
#     '''
#     person = request.args.get('person')
#     year = request.args.get('classYear')
#     major = request.args.get('major')
#     return render_template('biggerGreet.html',
#                            person=person, year=year, major = major)

# @app.route('/form')
# def homeWithForm():
#     '''
#     Demonstration of rendering a simple form.
#     '''
#     return render_template('index.html')    



'''
Run the program by typing 'python3 localhost [port]', where [port] is one of 
the port numbers you were sent by my earlier this term.
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
