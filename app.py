from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    salary = request.form['salary']
    
    # Ensure inputs are valid
    if age and salary:
        age = int(age)
        salary = int(salary)
        
        # Make prediction
        prediction = model.predict([[age, salary]])[0]
        
        # Render template with prediction
        return render_template('Home.html', prediction=prediction)
    else:
        return render_template('Home.html', prediction="Invalid input")

if __name__ == "__main__":
    app.run(debug=True)
