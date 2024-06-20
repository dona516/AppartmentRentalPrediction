from flask import Flask, request, jsonify, render_template
import locale
import pickle
import numpy as np

app = Flask(__name__)

# Set locale to German
locale.setlocale(locale.LC_ALL, 'de_DE')

# Load the pickled model
with open('rent_prediction_modelrf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def predict_rent():
    prediction = None

    if request.method == 'POST':
        # Get the form data
        newlyConst = request.form['newlyConst']
        balcony = request.form['balcony']
        hasKitchen = request.form['hasKitchen']
        noRoomsRange = int(request.form['noRoomsRange'])
        livingSpace = int(request.form['livingSpace'])
        geo_plz = int(request.form['geo_plz'])
        typeOfFlat = int(request.form['typeOfFlat'])

        print(newlyConst,balcony,hasKitchen,noRoomsRange,livingSpace,geo_plz,typeOfFlat)

        # Convert yes/no responses to 0 and 1
        newlyConst = 1 if newlyConst.lower() == 'yes' else 0
        balcony = 1 if balcony.lower() == 'yes' else 0
        hasKitchen = 1 if hasKitchen.lower() == 'yes' else 0

        # Create feature array
        features = [
            newlyConst, balcony, hasKitchen, livingSpace, typeOfFlat, geo_plz, noRoomsRange
        ]
        
        # Convert features to numpy array and reshape
        features_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features_array)[0]

        # Format prediction as currency
        prediction = locale.currency(prediction, grouping=True)

    # Render the HTML template with prediction
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
