// Exercise 2 

for (var i=0; i <= 15; i++) {
    if (i % 2 === 0) {
        console.log (i + ' is even')
    } else {
        console.log (i + ' is odd')
    }
}

// Exercise 3 

    // Solution 1 

var names = ["john", "sarah", 23, "Rudolf", 34]

for (let name of names) {
    if (typeof name != "string") {
        continue;
    }
    else {
        var firstLetter = name.substring(0,1)
        if (firstLetter != firstLetter.toUpperCase()) {
            var firstLetterUpper = firstLetter.toUpperCase()
            console.log(firstLetterUpper + name.substring(1))
        } 
    }
}

    // Solution 2 - Display the whole list with only capitalized names

var names = ["john", "sarah", 23, "Rudolf", 34]

for (let name of names) {
    if (typeof name != "string") {
        console.log(name);
    }
    else {
        var firstLetter = name.substring(0,1)
        if (firstLetter != firstLetter.toUpperCase()) {
            var firstLetterUpper = firstLetter.toUpperCase()
            console.log(firstLetterUpper + name.substring(1))
        } else {
            console.log(name)
        }
    }
}