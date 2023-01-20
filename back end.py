import os
import sys
import re
import subprocess

def main():
    print("Code input complete. Type 'test' to begin testing.")
    while True:
        command = input("Enter command: ")
        if command == "test":
            deploy_test()
        elif command == "exit":
            sys.exit()

def save_code(code):
    with open("dapp_code.txt", "a") as file:
        file.write(code + "\n")

def deploy_test():
    with open("dapp_code.txt", "r") as file:
        code = file.read()
    # Automatically detect the code type and extract it into the correct files, locations or folders
    if re.search(r"pragma solidity", code):
        extract_solidity_code(code)
    elif re.search(r"contract", code):
        extract_solidity_code(code)
    elif re.search(r"function", code):
        extract_javascript_code(code)
    else:
        print("Unable to detect code type.")

def extract_solidity_code(code):
    with open("contract.sol", "w") as file:
        file.write(code)
    try:
        # Compile the contract
        subprocess.run(["solc", "contract.sol"])
        # Run test on local blockchain
        subprocess.run(["ganache-cli"])
        subprocess.run(["truffle", "test"])
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

def extract_javascript_code(code):
    with open("app.js", "w") as file:
        file.write(code)
    try:
        # Install dependencies
        subprocess.run(["npm", "install"])
        # Run tests
        subprocess.run(["mocha", "app.js"])
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

if name == "main":
    while True:
        code = input("Enter code: ")
        save_code(code)
        more_code = input("Do you have more code? (yes/no) ")
        if more_code == "no":
            break
    main()
