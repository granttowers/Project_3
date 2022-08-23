from flask import Flask, render_template, redirect, jsonify, request
import pandas as pd
import os
import pickle
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

###################################################
# Flask Routes
###################################################

# Route to render the home page template
@app.route("/")
def home():
    return render_template("index.html")

# Route to the project page template
@app.route("/project.html")
def project():
    return render_template("project.html")

# Route to the questions page template
@app.route("/questions.html")
def questions():
    return render_template("questions.html")

# Route to the visualisations page template
@app.route("/Visualisations.html")
def visualisations():
    return render_template("Visualisations.html")

# Route to the incident prediction page template
@app.route("/Answer=<sex>=<age>=<occupation>=<operational_process>")
def answers(sex, age, occupation, operational_process):

# Binary values for Sex
    if sex == 'Female':
        Sex_Female = 1
        Sex_Male = 0

    # Binary values for Age
    if age == 'Age_Under_20':
        Age_Under_20 = 1
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_20_29':
        Age_Under_20 = 0
        Age_20_29 = 1
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_30_39':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 1
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_40_49':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 1
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_50_59':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 1
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_60_69':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 1
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == 'Age_70_79':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 1
        Age_80_89 = 0

    elif age == 'Age_80_89':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 1

    # Binary values for Occupation
    if occupation == 'Occupation_Apprentice_or_Trainee_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 1
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles	= 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Driller_and_Support_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 1
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Explosives_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 1
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles	= 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Fixed_Plant_Operator_and_Support_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 1
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles	= 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Labourer_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 1
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Maritime_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 1
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Mine_Supervisory_and_Management_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 1
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Mobile_Plant_Operator_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 1
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Other_Role':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 1
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles	= 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Technical_Services_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 1
        Occupation_Trades_Roles	= 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Trades_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 1
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif age == 'Occupation_Underground_Miner_and_Support_Roles':
        Occupation_Apprentice_or_Trainee_Roles = 0
        Occupation_Driller_and_Support_Roles = 0
        Occupation_Explosives_Roles = 0
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0
        Occupation_Labourer_Roles = 0
        Occupation_Maritime_Roles = 0
        Occupation_Mine_Supervisory_and_Management_Roles = 0
        Occupation_Mobile_Plant_Operator_Roles = 0
        Occupation_Other_Role = 0
        Occupation_Technical_Services_Roles = 0
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 1

# Binary values for Operational Process
    if operational_process == 'Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 1
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Culm_Banks_Activities_Coal_Mining_Only':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 1
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Dredging_Activities':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 1
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Non_Mine_Workshops_and_Yards':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 1
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Office_Located_on_Mine':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 1
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Other_Surface_Facility':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 1
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Surface_Mining_Operations':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 1
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Underground_Mine_Surface_Workshops_and_Yards':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 1
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Operational_Process_Underground_Mining_Operations':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities	= 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 1


    # Import Machine Learning Models - Nature of Injury (NOI), Injured Body Part (IBP), Source of Injury (SOI) and Activity (ACT)
    NOI_model = '/Working Documents/NOI_rf.pickle'
    NOI_loaded_model = pickle.load(open(NOI_model, 'rb'))

    IBP_model = '/Working Documents/IBP_rf.pickle'
    IBP_loaded_model = pickle.load(open(IBP_model, 'rb'))

    SOI_model = '/Working Documents/SOI_rf.pickle'
    SOI_loaded_model = pickle.load(open(SOI_model, 'rb'))

    ACT_model = '/Working Documents/ACT_rf.pickle'
    ACT_loaded_model = pickle.load(open(ACT_model, 'rb'))

    # Full response table to collate the response values
    response = [Sex_Male, Sex_Female, Age_Under_20, Age_20_29, Age_30_39, Age_40_49, Age_50_59, Age_60_69, Age_70_79, Age_80_89, Occupation_Apprentice_or_Trainee_Roles, Occupation_Driller_and_Support_Roles, Occupation_Explosives_Roles, Occupation_Fixed_Plant_Operator_and_Support_Roles, Occupation_Labourer_Roles, Occupation_Maritime_Roles, Occupation_Mine_Supervisory_and_Management_Roles, Occupation_Mobile_Plant_Operator_Roles, Occupation_Other_Role, Occupation_Technical_Services_Roles, Occupation_Trades_Roles, Occupation_Underground_Miner_and_Support_Roles, Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards, Operational_Process_Culm_Banks_Activities_Coal_Mining_Only, Operational_Process_Dredging_Activities, Operational_Process_Non_Mine_Workshops_and_Yards, Operational_Process_Office_Located_on_Mine, Operational_Process_Other_Surface_Facility, Operational_Process_Surface_Mining_Operations, Operational_Process_Underground_Mine_Surface_Workshops_and_Yards, Operational_Process_Underground_Mining_Operations]

    # Clear the results list
    results_list =[]

    # Append the new response values to the results_list list
    for item in response:
        results_list.append(float(item))

    new_value = np.array(results_list)
    new_value = np.expand_dims(new_value, 0)

    # Use the new value to generate a predictions for each model to new variable
    NOI_prediction = NOI_loaded_model.predict(new_value)
    IBP_prediction = IBP_loaded_model.predict(new_value)
    SOI_prediction = SOI_loaded_model.predict(new_value)
    ACT_prediction = ACT_loaded_model.predict(new_value)

    # Variables to store the predictions
    NOI_prediction
    IBP_prediction
    SOI_prediction
    ACT_prediction

    # Unsure about this bit...
    return render_template("answers.html")
    # f"Summary of Feedback Provided:<br>"
    # f"Gender: {sex}<br>"
    # f"Age: {age}<br>"
    # f"Occupation: {occupation}<br>"
    # f"Operational Process: {operational_process}<br>"
    # f"<br>"
    # f"<br>"
    # f"<h1>Your Results Are..."
    # f"The predicted Nature of Injury will be:   {NOI_prediction}<br>"
    # f"The predicted Injured Body Part will be:   {IBP_prediction}<br>"
    # f"The predicted Source of Injury will be:   {SOI_prediction}<br>"
    # f"The predicted Activity will be:   {ACT_prediction}<br>"

if __name__ == "__main__":
    app.run(debug=True)
