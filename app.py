import os
from xml.dom.expatbuilder import ElementInfo
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Database Setup
#################################################

# Create the engine to connect to local server
# engine = (create_engine(f'postgresql://postgres:' +
#           db_key+f'@localhost:5432/Project_2'))

# # reflect an existing database into a new model
# Base = automap_base()

# # reflect the tables
# Base.prepare(engine, reflect=True)
# engine.table_names()

# # Save references to each table
# incident_details = Base.classes.incident_details
# injured_person_details = Base.classes.injured_person_details
# injury_details = Base.classes.injury_details
# company_details = Base.classes.company_details

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################


@app.route("/")
def welcome():
    return render_template("index.html")
    """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"-------------------------------<br/>"
    #     f"/api/v1.0/incident_details<br/>"
    #     f"/api/v1.0/injury_details</br>"
    #     f"/api/v1.0/company_details"
    # )

# @app.route("/api/v1.0/incident_details")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all incident details"""

#     # Query all incident details
#     results = session.query(incident_details.mine_id, incident_details.incident_activity, incident_details.incident_category,
#                             incident_details.incident_day, incident_details.incident_month, incident_details.incident_type, incident_details.incident_year).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all incidents
#     incident_test = []

#     for mine_id, incident_activity, incident_category, incident_day, incident_month, incident_type, incident_year in results:

#         incident_test_dict = {}

#         incident_test_dict["mine_id"] = mine_id
#         incident_test_dict["incident_activity"] = incident_activity
#         incident_test_dict["incident_category"] = incident_category
#         incident_test_dict["incident_day"] = incident_day
#         incident_test_dict["incident_month"] = incident_month
#         incident_test_dict["incident_type"] = incident_type
#         incident_test_dict["incident_year"] = incident_year

#         incident_test.append(incident_test_dict)

#     return jsonify(incident_test)

# Create


# @app.route("/incident_prediction")
# def Results(Sex, Age, Occupation, Operational Process):

#     # Binary values for Sex
#     if Sex == 'Female':
#         Sex_Female = 1
#         Sex_Male = 0

#     # Binary values for Age
#     if Age == 'Age_<20':
#         Age_<20 = 1
#         Age_20 - 29 = 0
#         Age_30 - 39 = 0
#         Age_40 - 49 = 0 
#         Age_50 - 59 = 0
#         Age_60 - 69 = 0
#         Age_70 - 79 = 0
#         Age_80 - 89 = 0

#     elif Age == 'Age_20 - 29':
#         'Age_<20' = 0
#         'Age_20 - 29' = 1
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 0

#     elif Age == 'Age_30 - 39':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 1
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 0      
        
#     elif Age == 'Age_40 - 49':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 1
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 0           

#     elif Age == 'Age_50 - 59':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 1
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 0

#     elif Age == 'Age_60 - 69':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 1
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 0

#     elif Age == 'Age_70 - 79':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 1
#         'Age_80 - 89' = 0

#     elif Age == 'Age_80 - 89':
#         'Age_<20' = 0
#         'Age_20 - 29' = 0
#         'Age_30 - 39 '= 0
#         'Age_40 - 49' = 0 
#         'Age_50 - 59' = 0
#         'Age_60 - 69' = 0
#         'Age_70 - 79' = 0
#         'Age_80 - 89' = 1

#     # Binary values for Occupation
#     if Occupation == 'Occupation_Apprentice or Trainee Roles':
#         'Occupation_Apprentice or Trainee Roles' = 1
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0	
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0
        
#     elif Occupation == 'Occupation_Driller and Support Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 1
#         'Occupation_Explosives Roles' = 0	
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Explosives Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 1
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Fixed Plant Operatorand Support Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 1
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Fixed Plant Operator and Support Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 1
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Labourer Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 1
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Maritime Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 1
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Mine Supervisory and Management Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 1
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Mobile Plant Operator Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 1
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Other Role':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 1
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 1
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Trades Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 1
#         'Occupation_Underground Miner and Support Roles' = 0

#     elif Occupation == 'Occupation_Underground Miner and Support Roles':
#         'Occupation_Apprentice or Trainee Roles' = 0
#         'Occupation_Driller and Support Roles' = 0
#         'Occupation_Explosives Roles' = 0
#         'Occupation_Fixed Plant Operator and Support Roles' = 0
#         'Occupation_Labourer Roles' = 0
#         'Occupation_Maritime Roles' = 0
#         'Occupation_Mine Supervisory and Management Roles' = 0
#         'Occupation_Mobile Plant Operator Roles' = 0
#         'Occupation_Other Role' = 0
#         'Occupation_Technical Services (Geology, Survey, Engineer, Lab. Tech, OHS etc.)' = 0
#         'Occupation_Trades Roles' = 0
#         'Occupation_Underground Miner and Support Roles' = 1





#     elif Edu == "High School diploma":
#         none = 0
#         High_School = 1
#         Uni = 0
#         Masters = 0

#     elif Edu == "Tertiary education":
#         none = 0
#         High_School = 0
#         Uni = 1
#         Masters = 0

#     elif Edu == "Master's or Doctorate":
#         none = 0
#         High_School = 0
#         Uni = 0
#         Masters = 1

#     # binary of employment status before first baby

#     if Emp == "unemployed":
#         unemployed = 1
#         casual = 0
#         part_time = 0
#         full_time = 0

#     elif Emp == "Casual":
#         unemployed = 0
#         casual = 1
#         part_time = 0
#         full_time = 0

#     elif Emp == "Part-time":
#         unemployed = 0
#         casual = 0
#         part_time = 1
#         full_time = 0

#     elif Emp == "Full-time":
#         unemployed = 0
#         casual = 0
#         part_time = 0
#         full_time = 1

#     # partnerd binary

#     if Par == "Single":
#         Single = 1
#         Partnered = 0

#     elif Par == "Partnered":
#         Single = 1
#         Partnered = 0

#     # maternity eligabiluty binary

#     if Mat == "None":
#         none_1 = 1
#         Yes_paying = 0
#         Yes_unpaid = 0

#     elif Mat == "Yes - and we are paying!":
#         none_1 = 0
#         Yes_paying = 1
#         Yes_unpaid = 0

#     elif Mat == "Yes - but unpaid":
#         none_1 = 0
#         Yes_paying = 0
#         Yes_unpaid = 1

#     # Css eligability binary

#     if Css == "Yes":
#         css_Yes = 1
#         css_No = 0

#     elif Css == "No":
#         css_Yes = 0
#         css_No = 1

#     # Help binary
#     if Help == "No":
#         Hel_Yes_sc = 0
#         Hel_Yes_need = 0
#         Help_no = 1

#     elif Help == "Yes-Scheduled":
#         Hel_Yes_sc = 1
#         Hel_Yes_need = 0
#         Help_no = 0

#     elif Help == "Yes- As needed":
#         Hel_Yes_sc = 0
#         Hel_Yes_need = 1
#         Help_no = 0


# User_Response_List = [sex, age, occupation, operational process]

# print(Help_no)


# @app.route("/api/v1.0/injury_details")
# def names2():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all injury details"""

#     # Query all injury details
#     results = session.query(injury_details.mine_id, injury_details.injury_body_part, injury_details.injury_nature,
#                             injury_details.injury_classification, injury_details.injury_days_lost).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all injuries
#     injury_details_test = []

#     for mine_id, injury_body_part, injury_nature, injury_classification, injury_days_lost in results:

#         injury_details_dict = {}

#         injury_details_dict["mine_id"] = mine_id
#         injury_details_dict["injury_body_part"] = injury_body_part
#         injury_details_dict["injury_nature"] = injury_nature
#         injury_details_dict["injury_classification"] = injury_classification
#         injury_details_dict["injury_days_lost"] = injury_days_lost

#         injury_details_test.append(injury_details_dict)

#     return jsonify(injury_details_test)


# @app.route("/api/v1.0/company_details")
# def names3():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all company details"""

#     # Query all company details
#     results = session.query(company_details.mine_id, company_details.company_mine_type, company_details.company_name, company_details.company_address,
#                             company_details.company_city, company_details.company_injury_count, company_details.company_underground_surface).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all companies
#     company_details_test = []

#     for mine_id, company_mine_type, company_name, company_address, company_city, company_injury_count, company_underground_surface in results:

#         company_details_dict = {}

#         company_details_dict["mine_id"] = mine_id
#         company_details_dict["company_mine_type"] = company_mine_type
#         company_details_dict["company_name"] = company_name
#         company_details_dict["company_address"] = company_address
#         company_details_dict["company_city"] = company_city
#         company_details_dict["company_injury_count"] = company_injury_count
#         company_details_dict["company_underground_surface"] = company_underground_surface

#         company_details_test.append(company_details_dict)

#     return jsonify(company_details_test)


if __name__ == '__main__':
    app.run()
