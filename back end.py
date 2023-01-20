import os
import re
from subprocess import run, PIPE
from flask import Flask, request

app = Flask(__name__)

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
    elif re.search(r"fn main", code):
        extract_rust_code(code)
    elif re.search(r"import", code):
        extract_go_code(code)
    elif re.search(r"module", code):
        extract_haskell_code(code)
    elif re.search(r"func", code):
        extract_golang_code(code)
    elif re.search(r"class", code):
        extract_csharp_code(code)
    elif re.search(r"#include", code):
        extract_cplusplus_code(code)
    elif re.search(r"require", code):
        extract_ruby_code(code)
    elif re.search(r"public class", code):
        extract_java_code(code)
    elif re.search(r"new contract", code):
        extract_rholang_code(code)
    elif re.search(r"<?php", code):
        extract_php_code(code)
    elif re.search(r"SELECT", code):
        extract_sql_code(code)
    elif re.search(r"using", code):
        extract_csharp_code(code)
    else:
        print("Unable to detect code type.")

def extract_solidity_code(code):
    with open("contract.sol", "w") as file:
        file.write(code)
    try:
        # Compile the contract
        subprocess.run(["solc", "contract.sol"], stdout=PIPE, stderr=PIPE, check=True)
        # Run test on local blockchain
        subprocess.run(["ganache-cli"], stdout=PIPE, stderr=PIPE, check=True)
        subprocess.run(["truffle", "test"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

def extract_javascript_code(code):
    with open("app.js", "w") as file:
        file.write(code)
    try:
        # Install dependencies
        subprocess.run(["npm", "install"], stdout=PIPE, stderr=PIPE, check=True)
        # Run tests
        subprocess.run(["mocha", "app.js"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

def extract_rust_code(code):
    with open("main.rs", "w") as file:
        file.write(code)
    try:
        # Run tests
        subprocess.run(["cargo", "test"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

def extract_go_code(code):
    with open("main.go", "w") as file:
        file.write(code)
    try:
        # Run tests
        subprocess.run(["go", "test"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

def extract_haskell_code(code):
    with open("Main.hs", "w") as file:
        file.write(code)
    try:
        # Run tests
        subprocess.run(["stack", "test"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

# and so on for the rest of the languages
