
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

var occupation = ["Apprentice/Trainee", "Driller and Support Roles", "Explosives Roles", "Fixed Plant "]

// Populate dropbox with Occupation 
occupation.forEach((edu) => {
   var DDedu = d3.select("#Occupation");
   var newoption = DDedu.append("option");
   newoption.attr("value", edu);
   newoption.text(edu);
   Edu = DDedu.node().value;
}); 




//level of employment before first kids

var prekidEmp = ["unemployed", "Casual", "Part-time", "Full-time"]

// Populate dropbox with level of employment 
prekidEmp.forEach((emp) => {
   var DDemp = d3.select("#empLevel");
   var newoption = DDemp.append("option");
   newoption.attr("value", emp);
   newoption.text(emp);
   Emp = DDemp.node().value;
}); 


function optionChanged() {
  

  // Age 
var age_input = d3.select("input")
var age = age_input.property('value');


// Number of kids 
var DDkids = d3.select("#selNumKids");

NumofKids = DDkids.node().value;

console.log(age, NumofKids); 


// level of education

var DDedu = d3.select("#education");
Edu = DDedu.node().value;

switch (Edu){
    case "none":
      none = 1,
      High_School = 0,
      Uni = 0,
      Masters = 0
    
      break; 

    case "High School diploma": 
    none = 0,
    High_School = 1,
    Uni = 0,
    Masters = 0
  
    break; 

    case "Tertiary education": 
    none = 0,
    High_School = 0,
    Uni = 1,
    Masters = 0
  
    break; 

    case "Master's or Doctorate": 
    none = 0,
    High_School = 0,
    Uni = 0,
    Masters = 1
  
    break; 

  }

  console.log(Edu); 
  console.log(High_School, Masters, none, Uni)



  //level of employment before first kids
  var DDemp = d3.select("#empLevel");
  Emp = DDemp.node().value;

    switch (Emp){
    case "unemployed":
      unemployed = 1,
      casual = 0,
      part_time = 0,
      full_time = 0
    
      break; 

    case "Casual": 
    unemployed = 0,
    casual = 1,
    part_time = 0,
    full_time = 0
  
    break; 

    case "Part-time": 
    unemployed = 0,
    casual = 0,
    part_time = 1,
    full_time = 0
  
    break; 

    case "Full-time": 
    unemployed = 0,
    casual = 0,
    part_time = 0,
    full_time = 1
  
    break; 
  }

  console.log(Emp); 
  console.log(unemployed, casual, part_time, full_time)

  // partnered
  var DDpar = d3.select("#partner");
  Par = DDpar.node().value;

    switch (Par){
    case "Single":
      Single = 1,
      Partnered = 0
    
      break; 

    case "Partnered": 
    Single = 1,
    Partnered = 0
  
    break; 
   }

   console.log(Par); 
   console.log(Single, Partnered)


   // mat leave eligability
   var DDmat = d3.select("#matleave");
   Mat = DDmat.node().value;


     switch (Mat){
    case "None":
      None = 1,
      Yes_paying = 0,
      Yes_unpaid = 0
    
      break; 

    case "Yes - and we are paying!": 
    None = 0,
    Yes_paying = 1,
    Yes_unpaid = 0
  
    break; 

    case "Yes - but unpaid": 
    None = 0,
    Yes_paying = 0,
    Yes_unpaid = 1
  
    break; 
   }

   console.log(Mat); 
   console.log(None, Yes_paying, Yes_unpaid)

   // css eligability

   var DDcss = d3.select("#cssElig");
   Css = DDcss.node().value;

  switch (Css){
    case "Yes":
      Yes = 1,
      No = 0
    
      break; 

    case "No": 
    Yes = 0,
    No = 1
  
    break; 

   }

   console.log(Css); 
   console.log(Yes, No)
   //help 

    var DDhel = d3.select("#help");
    Help = DDhel.node().value;

   switch (Help){
    case "Yes-Scheduled":
      Yes = 1,
      No = 0
    
      break; 

    case "Yes - As needed": 
    Yes = 0,
    No = 1
  
    break; 

    case "No": 
    Yes = 0,
    No = 1
  
    break; 

}; 


console.log(Help); 
console.log(Yes, No)


var results = ( `${age}=${NumofKids}=${Edu}=${Emp}=${Par}=${Mat}=${Css}=${Help}`)


 
console.log(results)


d3.select("#clicked").attr("href", `answers=${results}`).html;
// Css = DDcss.node().value;

console.log(text)
 

};
 


var button= d3.select("#clicked");

button.on("click", optionChanged); 