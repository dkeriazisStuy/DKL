var next_fib = (a, b, n) => {
    if (n == 0) {
        return a;
    } else {
        return next_fib(b, a + b, n - 1);
    }
};

var fib = (n) => {
    if (n < 0) {
        return -1;
    }
    return next_fib(0, 1, n);
};

var gcd = (a, b) => {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
};

var students = [
    'adayR', 'aschJ', 'belkebirI', 'chenJ', 'chowdhuryJ', 'cwalinaP',
    'gondalA', 'guptaS', 'hasanA', 'johalP', 'keriazisD', 'liK', 'linJ',
    'linV', 'liuA', 'luW', 'maiJ', 'mohriC', 'narangA', 'ngR', 'onishiR',
    'peciR', 'petersT', 'rachlevskyM', 'wongT', 'wuR', 'yeJ', 'zhangI',
    'zhaoM', 'zhouQ',
];

var randomStudent = () => {
    return students[Math.floor(Math.random() * students.length)];
};

var fibButton = document.getElementById('fibButton');
var fibOut = document.getElementById('fibOut');
fibButton.addEventListener(
    'click',
    () => {
        var fibVal = document.getElementById('fibVal').value|0;
        if (isNaN(fibVal)) {
            return;
        }
        var result = fib(fibVal);
        console.log(
            'Called fib with', fibVal, 'and got', result
        );
        fibOut.setAttribute('value', result);
    }
);

var gcdButton = document.getElementById('gcdButton');
var gcdOut = document.getElementById('gcdOut');
gcdButton.addEventListener(
    'click',
    () => {
        var gcdVal1 = document.getElementById('gcdVal1').value|0;
        var gcdVal2 = document.getElementById('gcdVal2').value|0;
        if (isNaN(gcdVal1) || isNaN(gcdVal2)) {
            return;
        }
        var result = gcd(gcdVal1, gcdVal2);
        console.log(
            'Called gcd with', gcdVal1, 'and', gcdVal2, 'and got', result
        );
        gcdOut.setAttribute('value', result);
    }
);

var studentsButton = document.getElementById('studentsButton');
var studentsOut = document.getElementById('studentsOut');
studentsButton.addEventListener(
    'click',
    () => {
        var result = randomStudent();
        console.log(
            'Called randomStudent and got', result
        );
        studentsOut.setAttribute('value', result);
    }
);

