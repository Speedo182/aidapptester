// JavaScript for the front-end UI/UX design
const codeForm = document.getElementById("code-form");
const codeInput = document.getElementById("code-input");
const testCodeButton = document.getElementById("test-code");

codeForm.addEventListener("submit", (event) => {
    event.preventDefault();
    saveCode(codeInput.value);
    codeInput.value = "";
    testCodeButton.disabled = false;
});

testCodeButton.addEventListener("click", () => {
    deployTest();
});
