async function main() {
  const compute = require('dcp/compute')
  const wallet  = require('dcp/wallet')

  let job, startTime

  job = compute.for(["red", "orange", "yellow", "green", "blue", "purple"], 
    function(colour){
        console.log(colour)
        progress()
        return colour
    }
)

  job.on('accepted',
         function(ev) {
           console.log(`Job accepted by scheduler.`)
           console.log(`Job id: ${this.id}`)
           startTime = Date.now()
         })

  job.on('complete',
         function(ev) {
           console.log(`Finished job, total runtime = ${Math.round((Date.now() - startTime) / 100)/10}s`)
         })

  job.on('readystatechange',
         function(arg) {
           console.log(`New ready state: ${arg}`)
         })
  
  job.on('result',
         function(ev) {
           console.log(`Received result for slice ${ev.sliceNumber} at ${Math.round((Date.now() - startTime) / 100)/10}s`)
           console.log(`Result: ${ev.result}`);
         })

  job.public.name = 'example project, nodejs';
  job.public.description = 'example project description';

  let ks = await wallet.get(); /* usually loads ~/.dcp/default.keystore */
  job.setPaymentAccountKeystore(ks);
  await job.exec(compute.marketValue)
}

console.log("Initializing client...")
require('dcp-client').init().then(main).finally(() => setImmediate(process.exit))
console.log("Initialized client.")