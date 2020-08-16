async function main() {
    const compute = require("dcp/compute");
    const wallet = require("dcp/wallet");

    let job, startTime;

    job = compute.for([10, 100, 1000, 10000, 20000, 30000, 40000, 50000], function myfunction(n) {
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


);

    job.on("accepted", function (ev) {
        console.log(`Job accepted by scheduler.`);
        console.log(`Job id: ${this.id}`);
        startTime = Date.now();
    });

    job.on("complete", function (ev) {
        console.log(
            `Finished job, runtime = ${
                Math.round((Date.now() - startTime) / 100) / 10
            }s`
        );
    });

    job.on("readystatechange", function (arg) {
        console.log(`New ready state: ${arg}`);
        if (arg == "exec") {
            console.log("Please enter your bank keystore password:");
        } else if (arg == "deploying") {
            console.log("Please enter your id keystore password:");
        } else if (arg == "authorizeHold") {
            console.log("Awaiting fee structure auth...");
        } else if (arg == "authorizeFeeStructure") {
            console.log("Awaiting scheduler job acceptance...");
        } else if (arg == "deployed") {
            console.log("Job deployed!");
            console.log("Listening for results...");
        }
    });

    job.on("result", function (ev) {
        console.log(
            `Received result (slice ${ev.sliceNumber} @ ${
                Math.round((Date.now() - startTime) / 100) / 10
            }s) : ${ev.result}`
        );
    });

    job.public.name = "example project, nodejs";
    job.public.description = "example project description";

    let ks = await wallet.get(); /* usually loads ~/.dcp/default.keystore */
    job.setPaymentAccountKeystore(ks);
    await job.exec(compute.marketValue);
}

console.log("Initializing client...");
require("dcp-client")
    .init()
    .then(main)
    .finally(() => setImmediate(process.exit));
console.log("Initialized client.");
