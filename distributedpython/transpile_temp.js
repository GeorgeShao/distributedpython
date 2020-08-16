function myfunction(n) {
    var i, prime_numbers, status;
    prime_numbers = [2, 3];
    i = 3;
    while (true) {
        i += 1;
        status = true;
        for (var j = 2, _pj_a = (Number.parseInt((i / 2)) + 1); (j < _pj_a); j += 1) {
            if (((i % j) === 0)) {
                status = false;
                break;
            }
        }
        if ((status === true)) {
            prime_numbers[prime_numbers.length] = i;
        }
        if ((prime_numbers.length === n)) {
            break;
        }
    }
    progress();
    return `${n}th Prime Number is: ${prime_numbers[(n - 1)]}`;
}

//# sourceMappingURL=transpile_temp.js.map
