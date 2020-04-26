
var operator = ['+', '-', '*', '/'];
var number1 = 0;
var number2 = 0;
var op = '';
var numberfull = [];
var display = document.getElementById("display");


function calcul(x,y) {
    if (op ==='+') {
        return x+y;
    } else if (op ==='-') {
        return x-y;
    } else if (op ==='*') {
        return x*y;
    } else if (op ==='/') {
        return x/y;
    }
}

function my_f(choice) {
    if (typeof choice === 'number') {
        if (op === '') {
            numberfull.push (choice);
            number1 = Number(numberfull.join(""));
            document.getElementById("display").value = number1;
        } else {
            numberfull.push (choice);
            number2 = Number(numberfull.join(""));
            document.getElementById("display").value = number2;
        }
    }
    
    else if (operator.indexOf(choice) >=0) {
       op = choice;
       numberfull = [];
       document.getElementById("display").value = op;
    } 

    else if (choice === '=') {
        display.value = calcul(number1,number2);
        number1 = 0;
        number2 = 0;
        op = '';
        numberfull = [];
    }
}

function clearcal() {
    number1 = 0
    number2 = 0
    op = ''
    numberfull = []
    document.getElementById("display").value = 0;
}




