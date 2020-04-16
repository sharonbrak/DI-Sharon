// Alternative 1

let sentence = 'This dinner is not that bad!'
let firstNot = sentence.indexOf("not");
let firstBad = sentence.indexOf("bad");
if ((firstNot < firstBad) && (firstNot != -1) && (firstBad != -1))
{ console.log (sentence.replace(sentence.substring(firstNot,firstBad+3),"good"))
} else 
{ (console.log(sentence))
}

// Alternative 2

let sentence = 'This dinner is bad!'
let firstNot = sentence.indexOf("not");
let firstBad = sentence.indexOf("bad");
let newsentence = sentence.substring(0,firstNot) + 'good' + sentence.substring(firstBad+3);
if ((firstNot < firstBad) && (firstNot != -1) && (firstBad != -1))
{ console.log (newsentence)
} else 
{ (console.log(sentence))
}