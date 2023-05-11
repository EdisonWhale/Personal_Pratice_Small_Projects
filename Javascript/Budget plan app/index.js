let totalAmount = document.getElementById("total-amount");
let userAmount = document.getElementById("user-amount");
const checkAmountButton = document.getElementById("check-amount");
const totalAmountButton = document.getElementById("total-amount-button");
const productTitle = document.getElementById("product-title");
const errorMessage = document.getElementById("budget-error");
const productTitleError = document.getElementById("product-title-error");
const productCostError = document.getElementById("product-cost-error");
const amount = document.getElementById("amount");
const expenditureValue = document.getElementById("expenditure-value");
const balanceValue = document.getElementById("balance-amount");
const list = document.getElementById("list");
let tempAmount = 0;

// Set Budget Functions

totalAmountButton.addEventListener("click", () => {
    tempAmount = totalAmount.value;
    // Bad input
    if (tempAmount === "" || tempAmount < 0) {
        errorMessage.classList.remove("hide");
    } else {
        errorMessage.classList.add("hide");
        // Set bidget
        amount.innerHTML = tempAmount;
        balanceValue.innerText = tempAmount - expenditureValue.innerText;
        // Clear input
        totalAmount.value = "";
    }
});

// Disable edit and delete button function

const disableButtons = (bool) => {
    let editButtons = document.getElementsByClassName("edit");
    Array.from(editButtons).forEach((element) => {
        element.disabled = bool;
    });
};

// Modify list elements function

const modifyElement = (element, edit = false) => {
    let parentDiv = element.parentElement;
    let currentBalance = balanceValue.innerText;
    let currentExpense = expenditureValue.innerText;
    let parentAmount = parentDiv.querySelector(".amount").innerText;
    let parentCategory = parentDiv.classList[2];
    if (edit) {
      let parentText = parentDiv.querySelector(".product").innerText;
      productTitle.value = parentText;
      userAmount.value = parentAmount;
      document.getElementById("category").value = parentCategory;
      disableButtons(true);
    }
  
    let categoryAmounts = {};
    let expenses = document.getElementsByClassName("sublist-content");
    for (let i = 0; i < expenses.length; i++) {
      let category = expenses[i].classList[2];
      let amount = parseInt(expenses[i].querySelector(".amount").innerText);
      if (category in categoryAmounts) {
        categoryAmounts[category] += amount;
      } else {
        categoryAmounts[category] = amount;
      }
    }
  
    let categoryBalance = {};
    let categories = Object.keys(categoryAmounts);
    for (let i = 0; i < categories.length; i++) {
      let category = categories[i];
      let categorySum = categoryAmounts[category];
      let categoryBudget = categoryBudgets[category] || 0;
      categoryBalance[category] = categoryBudget - categorySum;
    }
  
    balanceValue.innerText = categoryBalance[parentCategory];
    expenditureValue.innerText = categoryAmounts[parentCategory];
    parentDiv.remove();
  };
  

// Create list function

const listCreator = (expenseName, expenseValue, categoryValue, dateTimeValue) => {
    let subListContent = document.createElement("div");
    subListContent.classList.add("sublist-content", "flex-space", categoryValue, dateTimeValue);
    list.appendChild(subListContent);
    subListContent.innerHTML = `<p class="product">${expenseName}</p><p class="amount">${expenseValue}</p><p class="datetime">${dateTimeValue}</p>`;
    let editButton = document.createElement("button");
    editButton.classList.add("fa-solid", "fa-pen-to-square", "edit");
    editButton.style.fontSize = "1.2em";
    editButton.addEventListener("click", () => {
      modifyElement(editButton, true);
    });
    let deleteButton = document.createElement("button");
    deleteButton.classList.add("fa-solid", "fa-trash-can", "delete");
    deleteButton.style.fontSize = "1.2em";
    deleteButton.addEventListener("click", () => {
      modifyElement(deleteButton);
    });
    subListContent.appendChild(editButton);
    subListContent.appendChild(deleteButton);
    document.getElementById("list").appendChild(subListContent);
  };
  
  

// Add expenses function

checkAmountButton.addEventListener("click", () => {
    // Check empty
    if (!userAmount.value || !productTitle.value || !document.getElementById("category").value) {
      productTitleError.classList.remove("hide");
      return false;
    }
    // Enable buttons
    disableButtons(false);
    //Expense
    let expenditure = parseInt(userAmount.value);
    // Total expense (existing + new)
    let sum = parseInt(expenditureValue.innerText) + expenditure;
    expenditureValue.innerText = sum;
    // Total balance = budget - total expense
    const totalBalance = tempAmount - sum;
    balanceValue.innerText = totalBalance;
    // Create list
    let categoryValue = document.getElementById("category").value;
    let dateTimeValue = document.getElementById("date").value;
    listCreator(productTitle.value, userAmount.value, categoryValue, dateTimeValue);
    // Clear inputs
    productTitle.value = "";
    userAmount.value = "";
    document.getElementById("category").value = "";
    document.getElementById("date").value = "";
  });
  
  