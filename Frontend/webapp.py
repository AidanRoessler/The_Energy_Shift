
import flask
from flask import render_template, request
import sys
sys.path.append('../Backend/')
from api import EnergyProductionAPI

# invokes Flask (creates an instance)
app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    '''
    Renders the Home template which is a homepage that tells the user about the purpose of our
    site and allows them to navigate to theData page
    '''
    return render_template('home.html')


@app.route('/theData', methods=['POST', 'GET'])
def theData():
    '''
    Renders The Data template which queries data about a given state and displays visualizations
    based off their results
    '''

    energy = EnergyProductionAPI()

    #Initialize all relevant variables as none so flask knows not to render the results portion of the page
    selectedState = None
    selectedStateFullName = None
    totalEnergy = None
    totalRenewableEnergy = None
    totalEnergyByMonth = None
    totalEnergyByCategory = None
    categories = None
    categoryValue = None
    
    #Getting data from form
    if request.method == 'POST':
        selectedState = request.form["statesSelect"]

        #Call the api with the data retrieved
        totalEnergy = energy.getEnergyForState(selectedState)
        totalRenewableEnergy = energy.getTotalRenewableEnergyByState(selectedState)
        totalEnergyByMonth = energy.getTotalEnergyForStateByMonth(selectedState)
        totalEnergyByCategory = energy.getEnergyByCategoryForState(selectedState)
        selectedStateFullName = energy.convertAbbreviationToFullState(selectedState)

        #Parse the dictionary totalEnergyByCategory returns
        categories = list(totalEnergyByCategory.keys())
        categoryValue = list(totalEnergyByCategory.values())
    
    return render_template('theData.html', selectedState = selectedState, totalEnergy = totalEnergy, 
    totalRenewableEnergy = totalRenewableEnergy, totalEnergyByMonth = totalEnergyByMonth, 
    categories = categories, categoryValue = categoryValue, selectedStateFullName = selectedStateFullName)


@app.route('/aboutTheData')
def aboutTheData():
    '''
    Renders the About the Data template which provides the user information about our data,
    it's source and the process of choosing and working with this data
    '''
    return render_template('aboutTheData.html')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
