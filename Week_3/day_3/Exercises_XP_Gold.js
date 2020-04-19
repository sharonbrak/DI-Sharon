
// Exercise 1

let family = {
    father: "Maurice",
    mother: "Elisabeth",
    daughter: "Sharon",
    littledaughter: "Eleonore",
    son: "David"
  };

for (let x in family) {
    console.log(x);
}

for (let x in family) {
    console.log(family[x]);
}

// Exercise 2

var building = {
    "number_levels" : 4,
    "number_of_apt_by_level" : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    "name_of_tenants" : ["Sarah", "Dan", "David"],
    "number_of_rooms_and_rent":  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

    //1.
console.log(building["number_levels"]);

    //2.
var flats1 = building["number_of_apt_by_level"]["1"];
var flats3 = building["number_of_apt_by_level"]["3"];
console.log(flats1);
console.log(flats3);
var flatstotal = flats1 + flats3;
console.log(flatstotal);

    //3.   

var tenants = building["name_of_tenants"];
var tenantSecond = tenants[1]
console.log(tenantSecond);

var roomsrent = building["number_of_rooms_and_rent"];
console.log(roomsrent);
console.log(roomsrent[tenantSecond][0])

var rentSarah = roomsrent["Sarah"][1];
var rentDavid = roomsrent["David"][1];
var sumRent = rentSarah + rentDavid;
var rentDan = roomsrent["Dan"][1];

if (sumRent > rentDan) {
    alert('You are idiot!!! Increase Dan please');
    building["number_of_rooms_and_rent"]["Dan"][1] = sumRent;
}

console.log(building);


// Exercise 3

var person1 = {
    "FullName": "Mathias", 
    "Mass": 80,
    "Height": 1.87,
    "BMI": function() {
        return this["Mass"]/(this["Height"]*this["Height"]);
    }
}

person1.BMI();
console.log(person1["BMI"]());

var person2 = {
    "FullName": "Sharon", 
    "Mass": 60,
    "Height": 1.64,
    "BMI": function() {
        return this["Mass"]/(this["Height"]*this["Height"]);
}
}

person2.BMI();


function fattest() {
    if ( person1["BMI"]() > person2["BMI"]() ) {
        alert(person1["FullName"] + ' you are the fattest!');
    } else {
        alert(person2["FullName"] + ' you are the fattest!');
    }
}

fattest();
