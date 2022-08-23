
//Age Group 

var ageGroup = ["Under 20", "20 - 29", "30 - 39", "40 - 49","50 - 59","60 - 69", "70 - 79", "80 - 89"]

// Populate dropbox with Age Ranges
ageGroup.forEach((par) => {
   var DDpar = d3.select("#AgeGroup");
   var newoption = DDpar.append("option");
   newoption.attr("value", par);
   newoption.text(par);
   Par = DDpar.node().value;
}); 

// Persons Gender 

var gender = ["Male", "Female"]

// Populate dropbox with Gender
gender.forEach((num) => {
   var DDkids = d3.select("#EmployeeGender");
   var newoption = DDkids.append("option");
   newoption.attr("value", num);
   newoption.text(num);
   NumofKids = DDkids.node().value;
}); 



// Employee Occupation 

var occupation = ["Apprentice/Trainee", "Driller and Support Roles", "Explosives Roles", "Fixed Plant Operator and Support Roles", "Laborer Roles", "Maritime Roles", "Supervisory/Management Roles", "Mobile Plant Operators", "Other Roles", "Technical Services", "Trade Roles", "Underground Mine and Support"]

// Populate dropbox with Occupation 
occupation.forEach((edu) => {
   var DDedu = d3.select("#Occupation");
   var newoption = DDedu.append("option");
   newoption.attr("value", edu);
   newoption.text(edu);
   Edu = DDedu.node().value;
}); 




// Operational Process 

var operationalProcess  = ["Crushing or Processing", "Coal Mining Culm Banks activities", "Dredging Acvitites", "Non Mine Workshops and Yards", "Office Activites", "Other Surface Facility", "Surface Mining Operations", "Underground Workshops/Yards","Underground Mining Operations" ]

// Populate dropbox with Operational Processes 
operationalProcess.forEach((emp) => {
   var DDemp = d3.select("#OpProcess");
   var newoption = DDemp.append("option");
   newoption.attr("value", emp);
   newoption.text(emp);
   Emp = DDemp.node().value;
}); 


function optionChanged() {



// Age Group Switching
var DDpar = d3.select("#AgeGroup");
Par = DDpar.node().value;

switch (Par){
    case "Under 20":
      Age_Under_20 = 1,
      Age_20_29 = 0
      Age_30_39 = 0
      Age_40_49 = 0
      Age_50_59 = 0
      Age_60_69 = 0
      Age_70_79 = 0
      Age_80_89 = 0
    break;

    case "20 - 29":
      Age_Under_20 = 0,
      Age_20_29 = 1,
      Age_30_39 = 0,
      Age_40_49 = 0,
      Age_50_59 = 0,
      Age_60_69 = 0,
      Age_70_79 = 0,
      Age_80_89 = 0
    break; 

    case "30 - 39":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 1,
      Age_40_49 = 0,
      Age_50_59 = 0,
      Age_60_69 = 0,
      Age_70_79 = 0,
      Age_80_89 = 0  
    break; 

    case "40 - 49":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 0,
      Age_40_49 = 1,
      Age_50_59 = 0,
      Age_60_69 = 0,
      Age_70_79 = 0,
      Age_80_89 = 0
    break; 

    case "50 - 59":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 0,
      Age_40_49 = 0,
      Age_50_59 = 1,
      Age_60_69 = 0,
      Age_70_79 = 0,
      Age_80_89 = 0
    break; 

    case "60 - 69":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 0,
      Age_40_49 = 0,
      Age_50_59 = 0,
      Age_60_69 = 1,
      Age_70_79 = 0,
      Age_80_89 = 0
    break; 

    case "70 - 79":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 0,
      Age_40_49 = 0,
      Age_50_59 = 0,
      Age_60_69 = 0,
      Age_70_79 = 1,
      Age_80_89 = 0
    break;

    case "80 - 89":
      Age_Under_20 = 0,
      Age_20_29 = 0,
      Age_30_39 = 0,
      Age_40_49 = 0,
      Age_50_59 = 0,
      Age_60_69 = 0,
      Age_70_79 = 0,
      Age_80_89 = 1
    break;
  }
  
  console.log(Par); 
  console.log(Age_Under_20, Age_20_29, Age_30_39, Age_40_49, Age_50_59, Age_60_69, Age_70_79, Age_80_89)

// Gender
var DDkids = d3.select("#EmployeeGender");
NumofKids = DDkids.node().value;

  switch (NumofKids){
    case "Female":
        Sex_Female = 1,
        Sex_Male = 0
    break; 

    case "Male":
        Sex_Female = 0,
        Sex_Male = 1
    break; 
}

console.log(DDkids); 
console.log(Sex_Female, Sex_Male)

  // Occupation Group Switching
var DDedu = d3.select("#Occupation");
Edu = DDedu.node().value;

  switch (Edu) {
    case "Apprentice/Trainee":
      Occupation_Apprentice_or_Trainee_Roles = 1,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Driller and Support Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 1,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Explosives Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 1,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Fixed Plant Operator and Support Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 1,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Labourer Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 1,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Maritime Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 1,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Supervisory/Management Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 1,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Mobile Plant Operators":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 1,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Other Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 1,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Technical Services":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 1,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Trade Roles":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 1,
        Occupation_Underground_Miner_and_Support_Roles = 0
      break;

    case "Underground Mine and Support":
      Occupation_Apprentice_or_Trainee_Roles = 0,
        Occupation_Driller_and_Support_Roles = 0,
        Occupation_Explosives_Roles = 0,
        Occupation_Fixed_Plant_Operator_and_Support_Roles = 0,
        Occupation_Labourer_Roles = 0,
        Occupation_Maritime_Roles = 0,
        Occupation_Mine_Supervisory_and_Management_Roles = 0,
        Occupation_Mobile_Plant_Operator_Roles = 0,
        Occupation_Other_Role = 0,
        Occupation_Technical_Services_Roles = 0,
        Occupation_Trades_Roles = 0,
        Occupation_Underground_Miner_and_Support_Roles = 1
      break;
  }

  console.log(DDedu);
  console.log(Occupation_Apprentice_or_Trainee_Roles, Occupation_Driller_and_Support_Roles, Occupation_Explosives_Roles, Occupation_Fixed_Plant_Operator_and_Support_Roles, Occupation_Labourer_Roles, Occupation_Maritime_Roles, Occupation_Mine_Supervisory_and_Management_Roles, Occupation_Mobile_Plant_Operator_Roles, Occupation_Other_Role, Occupation_Technical_Services_Roles, Occupation_Trades_Roles, Occupation_Underground_Miner_and_Support_Roles)
  
  
  // Operational Processing Group
  var DDemp = d3.select("#OpProcess");
  Emp = DDemp.node().value;

  switch (Emp) {
    case "Crushing or Processing":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 1,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Coal Mining Culm Banks activities":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 1,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Dredging Acvitites":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 1,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Non Mine Workshops and Yards":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 1,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Office Activites":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 1,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Other Surface Facility":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 1,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Surface Mining Operations":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 1,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Underground Workshops/Yards":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 1,
        Operational_Process_Underground_Mining_Operations = 0
      break;

    case "Underground Mining Operations":
      Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards = 0,
        Operational_Process_Culm_Banks_Activities_Coal_Mining_Only = 0,
        Operational_Process_Dredging_Activities = 0,
        Operational_Process_Non_Mine_Workshops_and_Yards = 0,
        Operational_Process_Office_Located_on_Mine = 0,
        Operational_Process_Other_Surface_Facility = 0,
        Operational_Process_Surface_Mining_Operations = 0,
        Operational_Process_Underground_Mine_Surface_Workshops_and_Yards = 0,
        Operational_Process_Underground_Mining_Operations = 1
      break;
  }
  console.log(DDemp);
  console.log(Operational_Process_Crushing_or_Processing_Facility_Incl_Associated_Workshops_and_Yards, Operational_Process_Culm_Banks_Activities_Coal_Mining_Only, Operational_Process_Dredging_Activities, Operational_Process_Non_Mine_Workshops_and_Yards, Operational_Process_Office_Located_on_Mine, Operational_Process_Other_Surface_Facility, Operational_Process_Surface_Mining_Operations, Operational_Process_Underground_Mine_Surface_Workshops_and_Yards, Operational_Process_Underground_Mining_Operations)

var results = ( `${NumofKids}=${Edu}=${Emp}=${Par}`)


 
console.log(results)


d3.select("#clicked").attr("href", `Answers=${results}`).html;
// Css = DDcss.node().value;

console.log(text)
 

};
 


var button= d3.select("#clicked");

button.on("click", optionChanged); 