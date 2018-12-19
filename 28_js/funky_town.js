var next_fib = (a, b, n) => {
    if (n == 0) {
        return a;
    } else {
        return next_fib(b, a + b, n - 1);
    }
};

var fib = (n) => {
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

