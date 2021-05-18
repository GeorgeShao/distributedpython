
var a = [1, 10, 100, 1000, 10000, 100000]

function myfunction(num) {
    var factorial;
    factorial = 1;
    for (var i = 1; i <= num; i += 1) {
        factorial *= i;
    }
    return `${num}! = ${factorial}`;
}

for (var i = 0; i < 6; i += 1) {
    console.log(myfunction(a[i]))
}