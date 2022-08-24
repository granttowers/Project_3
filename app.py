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

    elif sex == 'Male':
        Sex_Female = 0
        Sex_Male = 1

    # Binary values for Age
    if age == 'Under 20':
        Age_Under_20 = 1
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '20 - 29':
        Age_Under_20 = 0
        Age_20_29 = 1
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '30 - 39':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 1
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '40 - 49':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 1
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '50 - 59':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 1
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '60 - 69':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 1
        Age_70_79 = 0
        Age_80_89 = 0

    elif age == '70 - 79':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 1
        Age_80_89 = 0

    elif age == '80 -89':
        Age_Under_20 = 0
        Age_20_29 = 0
        Age_30_39 = 0
        Age_40_49 = 0
        Age_50_59 = 0
        Age_60_69 = 0
        Age_70_79 = 0
        Age_80_89 = 1

    # Binary values for Occupation
    if occupation == 'Apprentice or Trainee':
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
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif occupation == 'Driller and Support Roles':
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

    elif occupation == 'Explosives Roles':
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
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif occupation == 'Fixed Plant Operator and Support Roles':
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
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif occupation == 'Labourer Roles':
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

    elif occupation == 'Maritime Roles':
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

    elif occupation == 'Supervisory and Management Roles':
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

    elif occupation == 'Mobile Plant Operators':
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

    elif occupation == 'Other Roles':
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
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif occupation == 'Technical Services':
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
        Occupation_Trades_Roles = 0
        Occupation_Underground_Miner_and_Support_Roles = 0

    elif occupation == 'Trade Roles':
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

    elif occupation == 'Underground Mine and Support':
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
    if operational_process == 'Crushing or Processing':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 1
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Coal Mining Culm Banks Activities':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 1
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Dredging Acvitites':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 1
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Non Mine Workshops and Yards':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 1
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Office Activites':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 1
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Other Surface Facility':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 1
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Surface Mining Operations':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 1
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Underground Workshops and Yards':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 1
        Operational_Process_Underground_Mining_Operations = 0

    elif operational_process == 'Underground Mining Operations':
        Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0
        Operational_Process_Dredging_Activities = 0
        Operational_Process_Non_Mine_Workshops_and_Yards = 0
        Operational_Process_Office_Located_on_Mine = 0
        Operational_Process_Other_Surface_Facility = 0
        Operational_Process_Surface_Mining_Operations = 0
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0
        Operational_Process_Underground_Mining_Operations = 1

    # Import Machine Learning Models - Nature of Injury (NOI), Injured Body Part (IBP), Source of Injury (SOI) and Activity (ACT)
    NOI_model = 'NOI_rf.pickle'
    NOI_loaded_model = pickle.load(open(NOI_model, 'rb'))

    IBP_model = 'IBP_rf.pickle'
    IBP_loaded_model = pickle.load(open(IBP_model, 'rb'))

    SOI_model = 'SOI_rf.pickle'
    SOI_loaded_model = pickle.load(open(SOI_model, 'rb'))

    ACT_model = 'ACT_rf.pickle'
    ACT_loaded_model = pickle.load(open(ACT_model, 'rb'))

    # Full response table to collate the response values
    response = [Sex_Male, Sex_Female, Age_Under_20, Age_20_29, Age_30_39, Age_40_49, Age_50_59, Age_60_69, Age_70_79, Age_80_89, Occupation_Apprentice_or_Trainee_Roles, Occupation_Driller_and_Support_Roles, Occupation_Explosives_Roles, Occupation_Fixed_Plant_Operator_and_Support_Roles, Occupation_Labourer_Roles, Occupation_Maritime_Roles, Occupation_Mine_Supervisory_and_Management_Roles, Occupation_Mobile_Plant_Operator_Roles, Occupation_Other_Role, Occupation_Technical_Services_Roles, Occupation_Trades_Roles,
                Occupation_Underground_Miner_and_Support_Roles, Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards, Operational_Process_Culm_Banks_Activities_Coal_Mining_Only, Operational_Process_Dredging_Activities, Operational_Process_Non_Mine_Workshops_and_Yards, Operational_Process_Office_Located_on_Mine, Operational_Process_Other_Surface_Facility, Operational_Process_Surface_Mining_Operations, Operational_Process_Underground_Mine_Surface_Workshops_and_Yards, Operational_Process_Underground_Mining_Operations]

    # Clear the results list
    results_list = []

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

    # Render the 'Answer.html' file, and pass the variable results to be called onto the page.
    return render_template("Answer.html", sex=sex, age=age, occupation=occupation, operational_process=operational_process, NOI_prediction=NOI_prediction[0], IBP_prediction=IBP_prediction[0], SOI_prediction=SOI_prediction[0], ACT_prediction=ACT_prediction[0])

if __name__ == '__main__':
    app.debug = True
    app.run()
