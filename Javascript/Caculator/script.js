const display = document.querySelector(".display");
const buttons = document.querySelectorAll(".buttons button");
const specialChars = ["%", "*", "/", "-", "+", "=", "^2", "sqrt", "log", "sin", "cos", "tan"];
let output = "";

const darkModeToggle = document.getElementById("darkModeToggle");
const historyDiv = document.getElementById("history");
const container = document.querySelector('.container'); // 修复的地方

// Array to store history of calculations.
let history = [];

darkModeToggle.addEventListener("click", () => {
  // Toggle dark mode on body and calculator elements.
  const elements = [document.body, darkModeToggle, container, display];
  buttons.forEach((button) => elements.push(button));

  elements.forEach((element) => {
    element.classList.toggle("dark-mode");
  });

  // Change the text of the dark mode toggle button accordingly.
  if (document.body.classList.contains("dark-mode")) {
    darkModeToggle.textContent = "Switch to Light Mode";
  } else {
    darkModeToggle.textContent = "Switch to Dark Mode";
  }
});


// Define function to calculate based on button clicked.
const specialOperations = {
  "^2": (num) => Math.pow(num, 2),
  "sqrt": (num) => Math.sqrt(num),
  "log": (num) => Math.log10(num),
  "sin": (num) => Math.sin(num),
  "cos": (num) => Math.cos(num),
  "tan": (num) => Math.tan(num),
};

let lastOperation = {
    operation: null,
    operand: null
};

const calculate = (btnValue) => {
    display.focus();

    // If special operation is called
    if (specialOperations.hasOwnProperty(btnValue)) {
        output = specialOperations[btnValue](parseFloat(output));
        lastOperation = { operation: btnValue, operand: parseFloat(output) };
    } else if (btnValue === "=" && output !== "") {
        // Repeat the last operation if it exists
        if (lastOperation.operation) {
            output = specialOperations[lastOperation.operation](lastOperation.operand);
            lastOperation.operand = output;
        } else {
            output = eval(output.toString().replace("%", "/100"));

            // Save to history and display the history.
            history.push(output);
            const historyParagraph = document.createElement("p");
            historyParagraph.textContent = output;
            historyDiv.appendChild(historyParagraph);

            // Extract last operation and value
            const operationMatch = output.toString().match(/([\d.]+)(\D)([\d.]+)$/);
            if (operationMatch) {
                lastOperation = {
                    operation: operationMatch[2],
                    operand: parseFloat(operationMatch[3])
                };
            }
        }
    } else if (btnValue === "AC") {
        output = "";
        lastOperation = { operation: null, operand: null };
    } else if (btnValue === "DEL") {
        // If DEL button is clicked, remove the last character from the output.
        output = output.toString().slice(0, -1);
    } else {
        // If output is empty and button is specialChars then return
        if (output === "" && specialChars.includes(btnValue)) return;
        output += btnValue;
    }
    display.value = output;
};

  
// Add event listener to buttons, call calculate() on click.
buttons.forEach((button) => {
  // Button click listener calls calculate() with dataset value as argument.
  button.addEventListener("click", (e) => calculate(e.target.dataset.value));
});

// Support keyboard input
document.addEventListener("keydown", (event) => {
  const keyName = event.key;

  // Check if the key corresponds to a calculator button
  for (let button of buttons) {
    if (button.dataset.value === keyName || button.innerText === keyName) {
      calculate(button.dataset.value);
      break;
    }
  }
});
