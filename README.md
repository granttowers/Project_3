# Project 3 - Final Project: 

Project Leads and Key Contacts:
- Nicholas Mcmahon – Data Analyst
- Grant Towers – Data Analyst


# Project Background:

We want to develop a series of visualisations depicting elements of the incident data within the US, then create a number of Machine Learning model.

The Model will use the 'Sex', 'Age' and 'Occupation' column data which will be grouped (into smaller number of values to simplify the data model). The website will require require the end user to select a value for their situation, and then the site will predict:

1. The 'Activity' the person will most likely be injured doing.
2. The 'Body Part Injured' of the person that will be injured.
3. The 'Nature of Injury' that will be incurred.
4. The 'Source of Injury' that will cause the injury. 

These will all be shown to the visitor as fields on the Website.


# Project Steps and Activity Plan:

Data Preparation:
- Complete Significant Data Cleanup and Grouping as required (Complete).
- Identify the 'target' data for our Machine Learning Models (Complete).
- Identify the output 'results' that we want to present on the website - "Project_3\Working Documents\Import Data to Postgress" (Complete).


Database/Hosting:
- Create the RDS Server to house the Postgress DB (Complete).
- Create the S3 Bucket to store the incident file (Complete).
- Upload the incident data file to the existing data into the S3 bucket (Complete).
- Deploy a Heroku Instance and connect to GitHub Repo (Complete).
- Heroku Website (https://grantnickproj3.herokuapp.com/)


Data Migration (ETL):
- Complete initial data cleanup against initial incident file, then using Google Colab, then push that data into the Postgress DB (Complete).


Initial Visualisations:
- Connect the 'clean' (revised) incident data output to Tableau Public to create visualisation (to be completed).
- Save these visualisations to the repo (as attachment) and so that we can use them in our Website (to be completed).
- Key Indicators would include the 'Incident Counts by Age', 'Incident Ratio by Age' and 'Incident Summary by Occupation' (our 3 key values) (to be completed). 

Machine Learning:
- Using the 'Sex', 'Age', 'Occupation' and "Operational Process" column data, create the data models we want to predict ('Activity', 'Body Part Injured', 'Nature of Injury' and 'Source of Injury') (Complete).

Flask App:
- to be confirmed...

HTML Page
- Build Home Page Details
- Append the Tableau Images, Create Text etc.
- What to do about predictive...?

Presentation:
- Basically a summary of the steps above... (to be completed)
- Use Same Template as last project? 
