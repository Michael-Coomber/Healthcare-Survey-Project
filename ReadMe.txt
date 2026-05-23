Healthcare Survey Project

1. Overview
This project is a web-based survey application developed using Flask. The system collects participants' demographic and financial information, including age, gender, income, and various expense categories.
The collected data is stored in a MongoDB database, exported into a CSV file, and analyzed using Jupyter Notebook. The analysis generates visual insights that support decision-making for a healthcare product launch.

2. Features

Web application built using Flask
User data collection through HTML forms
MongoDB database for storage
Data processing using Python
CSV export functionality
Data visualization using Matplotlib
Exported charts for presentation use


3. Technologies Used

Python
Flask
MongoDB
PyMongo
Pandas
Matplotlib
Jupyter Notebook


4. System Workflow
The system follows a structured data pipeline:

Users enter data through a Flask web form
Data is sent to the backend server
Data is stored in MongoDB
Data is extracted and saved as a CSV file
The CSV file is analyzed in Jupyter Notebook
Charts are generated and saved for reporting


5. How to Run the Application
Step 1: Start MongoDB
Ensure MongoDB is running locally:
mongosh


Step 2: Run the Flask Application
python app.py

Open your browser and go to:
http://127.0.0.1:5000


Step 3: Submit Survey Data
Fill in the form with the following details:

Age
Gender
Total Income
Expenses (Utilities, Entertainment, School Fees, Shopping, Healthcare)

Click Submit.

Step 4: Export Data to CSV
Run:
python export_csv.py

This will create:
survey_data.csv


Step 5: Perform Data Analysis
Open the Jupyter Notebook file:
notebooks/analysis.ipynb

Run all cells to generate charts.

6. Data Visualization
The project produces the following visualizations:

Ages with Highest Income
Gender Spending Distribution

These charts are saved in the charts folder:
charts/age_income.png  
charts/gender_spending.png


7. Use of Python User Class
A Python class named User is implemented to structure participant data. This improves organization, readability, and supports data processing operations such as exporting to CSV.

8. Project Structure
HEALTHCARE-SURVEY-PROJECT/

charts/
notebooks/
static/
templates/
    index.html

app.py
export_csv.py
user.py
survey_data.csv
requirements.txt
README.txt


9. AWS Deployment

The Flask application is prepared for deployment on AWS EC2 for online access.

The application can be hosted using an Ubuntu EC2 instance with Python, MongoDB, and Gunicorn.

Planned/Deployment URL:

http://16.170.201.230:5000

Typical deployment steps include:

1. Launch an EC2 instance using Ubuntu.
2. Configure the EC2 security group to allow:
   - SSH on port 22
   - Flask/Gunicorn app access on port 5000
3. Install Python, pip, virtual environment tools, Docker, and Git.
4. Configure MongoDB locally on the EC2 instance or use MongoDB Atlas.
5. Clone the project repository from GitHub.
6. Install project dependencies using:
   pip install -r requirements.txt



10. Conclusion
This project demonstrates an end-to-end data pipeline, including:

Web-based data collection
Database storage using MongoDB
Data processing using Python
Data analysis and visualization using Jupyter

The insights generated can support strategic decisions in healthcare product development.

11. Author
Michael Dauda Coomber

