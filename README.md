#Program name:  AI Dapp Tester
#Slogan: Automatically test a DAPP with the click of a button within seconds.

This application is a program for testing DApps (Decentralized Applications) written in Solidity, JavaScript, and other programming languages. The program allows users to input code, save it to a file, and then test the code by automatically detecting the code type and extracting it into the correct files, locations or folders.

The front-end is a simple web page that allows users to input code and submit it to the backend, it also has a button to test the code. The front-end uses JavaScript, HTML, and CSS to provide the user interface.

The back-end is a Python script that receives the code from the front-end, saves it to a file, and then performs tests on the code depending on the language it's written in. The back-end uses libraries such as os, sys, and re. The back-end also uses the command-line tool solc to compile the Solidity contract, and ganache-cli to run tests on a local blockchain and truffle to test the contract.

The application uses the Flask web framework to handle the requests, routes, and responses. There's also a library called requests for handling the requests and responses in the back-end code.

The package.json file contains the dependencies for the application, which are used for testing the JavaScript code and the requirements.txt file contain the dependencies for the application, which are used for deploying the smart contract and the runtime.txt file contains the version of Python needed for the application.
