import pickle
from flask import Flask, request, render_template # Import flask libraries
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Initialize the flask class and specify the templates directory
app = Flask(__name__)



def classify(itemName):
    print(itemName)
    prediction= loaded_model.predict([itemName])
    precentage= (loaded_model.predict_proba([itemName]).max())*100
    return prediction, precentage




# Default route set as 'home'
@app.route('/')
def home():
    return render_template('home.html') # Render home.html
	
	
# Route 'classify' accepts GET request
@app.route('/classify/',methods=['POST'])
def classify_type():
    try:
        product = request.form.get('product') # Get parameters for product
        print(product)

        # Get the output from the classification model
        category, precentage = classify(product)

        # Render the output in new HTML page
        return render_template('output.html', variety1=category,variety2= precentage)
    except:
        return 'Error'
		
		
		
		
# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=False)