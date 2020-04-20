
var operator = ['+', '-', '*', '/'];
var number1 = 0
var number2 = 0
var op = ''
var numberfull = []


function my_f(choice) {
    if (typeof choice === 'number') {
        if (op === '') {
            numberfull.push (choice);
            number1 = Number(numberfull.join(""));
        } else {
            numberfull.push (choice);
            number2 = Number(numberfull.join(""));
        }
    }
    
    else if (operator.indexOf(choice) >=0) {
       op = choice;
       numberfull = [];
    } 

    else if (choice === '=') {
        if (op ==='+') {
            alert(number1 + number2);
            number1 = 0;
            number2 = 0;
            op = '';
            numberfull = [];
        } else if (op ==='-') {
            alert(number1 - number2);
            number1 = 0;
            number2 = 0;
            op = '';
            numberfull = [];
        } else if (op ==='*') {
            alert(number1 * number2);
            number1 = 0;
            number2 = 0;
            op = '';
            numberfull = [];
        } else if (op ==='/') {
            alert(number1 / number2);
            number1 = 0;
            number2 = 0;
            op = '';
            numberfull = [];
        }
    
    }

}

function clearcal() {
    number1 = 0
    number2 = 0
    op = ''
    numberfull = []
    alert('Your calculator is now clean!')
}

