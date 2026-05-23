print("Flask app is starting...")

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_survey"]
collection = db["participants"]

# Helper function
def get_float(value):
    return float(value) if value else 0.0


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    age = int(request.form['age'])
    gender = request.form['gender']
    income = float(request.form['income'])

    expenses = {
        "utilities": get_float(request.form.get('utilities_amount')),
        "entertainment": get_float(request.form.get('entertainment_amount')),
        "school_fees": get_float(request.form.get('school_fees_amount')),
        "shopping": get_float(request.form.get('shopping_amount')),
        "healthcare": get_float(request.form.get('healthcare_amount'))
    }

    user_data = {
        "age": age,
        "gender": gender,
        "income": income,
        "expenses": expenses
    }

    # Store in MongoDB
    collection.insert_one(user_data)

    return redirect(url_for('success'))


@app.route('/success')
def success():
    return "✅ Data submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)