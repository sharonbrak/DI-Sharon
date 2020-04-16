// Exercise 1 : Your favorite colors

var colors = ["Blue", "Red", "Yellow", "Purple"];
    
for (let x of colors) {
    console.log ('My #' + (colors.indexOf(x)+1) + ' color is ' + x);
}

// Exercise 2 

var num = 0
while (num < 10) {
    num = Number(prompt('Give me a number baby'))
}


// Exercise 3

var people = ["Greg", "Mary", "Devon", "James"];
for (let i of people) {
    console.log (i);
}
people.shift();
people.pop();
people.push("Jason");
people.push ("Sharon");

for (let i of people) {
    console.log (i);
}

people.slice(0,1);

people.indexOf('Mary');
console.log(people.indexOf('Mary'));

people.indexOf('Foo');
console.log(people.indexOf('Foo'));

var lengthpeople = people.length;
var last = people[people.length-1];

// Exercise 4

    // 1. 

var age = [20,5,12,43,98,55,10];

var sum = 0;
for (let x of age) {
    sum = sum + x
}
console.log(sum);

    // 2.

var age = [20,5,12,43,98,55,10];

var sum = 0;
for (let x of age) {
    if (x%2 === 0) {
        sum = sum +x;
    } else {
        continue;
    }
}
console.log(sum);

    //3.

var age = [20,5,12,43,98,55,10];

var big = age[0];
for (let x of age) {
    if (x > big) {
        big = x;
    } 
}
console.log(big);
