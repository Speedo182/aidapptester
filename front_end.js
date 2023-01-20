const codeForm = document.getElementById("code-form");
const codeInput = document.getElementById("code-input");
const testCodeButton = document.getElementById("test-code");

// function to save the code
function saveCode(code) {
    // make an HTTP request to the backend server to save the code
    fetch("http://localhost:5000/save-code", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to save code.");
        }
    })
    .catch(error => {
        console.error(error);
        alert("Failed to save code. Please try again.");
    });
}

// function to deploy and test the code
function deployTest() {
    // make an HTTP request to the backend server to deploy and test the code
    fetch("http://localhost:5000/deploy-test")
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to deploy and test code.");
        }
        return response.text();
    })
    .then(result => {
        alert(result);
    })
    .catch(error => {
        console.error(error);
        alert("Failed to deploy and test code. Please try again.");
    });
}

codeForm.addEventListener("submit", (event) => {
    event.preventDefault();
    // validate the form field
    if (!codeInput.value) {
        alert("Code input is required!");
        return;
    }
    // save the code
    saveCode(codeInput.value);
    codeInput.value = "";
    testCodeButton.disabled = false;
});

testCodeButton.addEventListener("click", () => {
    deployTest();
});
