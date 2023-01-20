import re
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save-code', methods=['POST'])
def save_code():
    code = request.json['code']
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
        extract_rholang_code(code):
with open("contract.rho", "w") as file:
file.write(code)
try:
# Compile the contract
subprocess.run(["rholang", "compile", "contract.rho"], stdout=PIPE, stderr=PIPE, check=True)
# Deploy the contract to a local blockchain
subprocess.run(["rnode", "deploy", "contract.rho"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["rholang", "test", "contract.rho"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_csharp_code(code):
with open("program.cs", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["csc", "program.cs"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["nunit3-console", "program.dll"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_cplusplus_code(code):
with open("program.cpp", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["g++", "-std=c++11", "program.cpp", "-o", "program"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./program"], stdout
=PIPE, stderr=PIPE, check=True)
except Exception as e:
print("Error: ", e)

def extract_sql_code(code):
with open("query.sql", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["psql", "-f", "query.sql"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_csharp_code(code):
with open("program.cs", "w") as file:
file.write(code)
try:
# Compile the program
subprocess.run(["mcs", "program.cs"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./program.exe"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_cplusplus_code(code):
with open("program.cpp", "w") as file:
file.write(code)
try:
# Compile the program
subprocess.run(["g++", "-o", "program", "program.cpp"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./program"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_csharp_code(code):
with open("main.cs", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["dotnet", "test"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_cplusplus_code(code):
with open("main.cpp", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["g++", "-o", "program", "main.cpp"], stdout=PIPE, stderr=PIPE, check=True)
subprocess.run(["./program"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_ruby_code(code):
with open("main.rb", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["ruby", "main.rb"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_java_code(code):
with open("Main.java", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["javac", "Main.java"], stdout=PIPE, stderr=PIPE, check=True)
# Run the code
subprocess.run(["java", "Main"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_php_code(code):
with open("main.php", "w") as file:
file.write(code)
try:
# Run the code
subprocess.run(["php", "main.php"], stdout=PIPE, stderr=PIPE, check=True)
def extract_php_code(code):
    with open("main.php", "w") as file:
        file.write(code)
    try:
        # Run tests
        subprocess.run(["php", "main.php"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)
        
def extract_sql_code(code):
    with open("main.sql", "w") as file:
        file.write(code)
    try:
        # Run tests
        subprocess.run(["sql", "main.sql"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)
        
@app.route("/save-code", methods=["POST"])
def save_code():
    code = request.json["code"]
    with open("dapp_code.txt", "w") as file:
        file.write(code)
    return "Code saved successfully", 200

@app.route("/deploy-test", methods=["GET"])
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
def extract_haskell_code(code):
with open("main.hs", "w") as file:
file.write(code)
try:
# Install dependencies
subprocess.run(["cabal", "install"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["runhaskell", "main.hs"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_golang_code(code):
with open("main.go", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["go", "test"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_csharp_code(code):
with open("main.cs", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["csc", "main.cs"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./main.exe"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_cplusplus_code(code):
with open("main.cpp", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["g++", "main.cpp"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./a.out"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")

def extract_golang_code(code):
with open("main.go", "w") as file:
file.write(code)
try:
# Run tests
subprocess.run(["go", "test"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_csharp_code(code):
with open("main.cs", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["mcs", "main.cs"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./main.exe"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_cplusplus_code(code):
with open("main.cpp", "w") as file:
file.write(code)
try:
# Compile the code
subprocess.run(["g++", "main.cpp"], stdout=PIPE, stderr=PIPE, check=True)
# Run tests
subprocess.run(["./a.out"], stdout=PIPE, stderr=PIPE, check=True)
print("Test successful.")
except Exception as e:
print("Error: ", e)

def extract_ruby_code(code):
with open("main.rb", "w") as file:
file.write(code)
try:
# Run tests
def extract_haskell_code(code):
    with open("main.hs", "w") as file:
        file.write(code)
    try:
        # Compile the code
        subprocess.run(["ghc", "main.hs"], stdout=PIPE, stderr=PIPE, check=True)
        # Run tests
        subprocess.run(["./main"], stdout=PIPE, stderr=PIPE, check=True)
        print("Test successful.")
    except Exception as e:
        print("Error: ", e)

# Other extract code functions for other languages would be added here

@app.route("/save-code", methods=["POST"])
def save_code_route():
    code = request.json["code"]
    save_code(code)
    return "Code saved successfully."

@app.route("/deploy-test", methods=["GET"])
def deploy_test_route():
    deploy_test()
    return "Code deployed and tested successfully."

if __name__ == "__main__":
    app.run()
