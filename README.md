# DistributedPython - README.md

DistributedPython is a Python library that allows developers to run Python code on the Distributed Compute Protocol.

**Developer Usage:** see [DEV-USAGE.md](https://github.com/GeorgeShao/distributedpython/DEV-USAGE.md)

## Inspiration
I was inspired to create when I was first introduced to the Distributed Compute Protocol in May 2020. I was fascinated by the thought of being able to easily deploy computationally heavy tasks to various computers on the internet that would together form a virtual supercomputer. One issue I found was that it was very easy to get started and deploy tasks in JavaScript, but many intermediate programmers who only had good knowledge of the Python programming language, weren't able to experience the power of DCP. With my project DistributedPython, I aimed to solve this problem.

## What it does
DistributedPython allows developers to run Python code on the Distributed Compute Protocol, making the power of DCP accessible and more convenient for many developers.

## How we built it / how it works
DistributedPython first gets the payload and the Python code that you want to run on the DCP network. Then it transpiles your Python code to JavaScript code and saves it in a JavaScript file. DistributedPython then reads the transpiled code from the generated JavaScript file. It takes that and inserts the payload and the JavaScript code into a custom events.js file which is then run and uses Node.js to communicate with and get results from the DCP network.

## Challenges we ran into
I had some issues with stdin/stdout/stderr stream pipes. In the end, it was a fairly easy issue, and I fixed it, but I still spent a 3-4 hours debugging that issue since there were so many things that could've caused the problem I was having and I wasn't getting enough debugging/logging data.

## Accomplishments that we're proud of
I'm proud that I managed to get the project fully functioning as intended in the end! Although the Python code cannot contain other external libraries, it works for the vast majority of standard Python code.

## What we learned
I learned how to use DCP with Node.js, how to create a Python library, and how to send/receive data streams via stdin/stdout/stderr pipes. I was amazed at the immense computing power of DCP!

## What's next for DistributedPython
I want to further optimize and improve the generated code and various other parts of the DistributedPython library.
