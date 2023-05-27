let heads = 0;
let tails = 0;
let streak = 0;
let lastCoin = null;
let coin = document.querySelector(".coin");
let flipBtn = document.querySelector("#flip-button");
let resetBtn = document.querySelector("#reset-button");
let changeBgBtn = document.querySelector("#change-bg");

flipBtn.addEventListener("click", () => {
  let i = Math.floor(Math.random() * 2);
  coin.style.animation = "none";
  if (i) {
    if (lastCoin === "heads") {
      streak++;
    } else {
      streak = 1;
    }
    lastCoin = "heads";
    setTimeout(function () {
      coin.style.animation = "spin-heads 3s forwards";
    }, 100);
    heads++;
  } else {
    if (lastCoin === "tails") {
      streak++;
    } else {
      streak = 1;
    }
    lastCoin = "tails";
    setTimeout(function () {
      coin.style.animation = "spin-tails 3s forwards";
    }, 100);
    tails++;
  }
  setTimeout(updateStats, 3000);
  disableButton();
});

function updateStats() {
  let total = heads + tails;
  let headsPercentage = total ? ((heads / total) * 100).toFixed(2) : 0;
  let tailsPercentage = total ? ((tails / total) * 100).toFixed(2) : 0;

  document.querySelector("#heads-count").textContent = `Heads: ${heads}`;
  document.querySelector("#tails-count").textContent = `Tails: ${tails}`;
  document.querySelector(
    "#heads-percentage"
  ).textContent = `Heads: ${headsPercentage}%`;
  document.querySelector(
    "#tails-percentage"
  ).textContent = `Tails: ${tailsPercentage}%`;
  document.querySelector("#streak-count").textContent = `Streak: ${streak}`;
  checkAchievements();
}

function checkAchievements() {
  const achievementsDiv = document.querySelector("#achievements");
  if (streak === 3) {
    achievementsDiv.textContent = "Achievement: 3 in a row!";
  } else if (streak === 10) {
    achievementsDiv.textContent = "Achievement: 10 in a row!";
  } else if (streak === 20) {
    achievementsDiv.textContent = "Achievement: 20 in a row!";
  }
}

function disableButton() {
  flipBtn.disabled = true;
  setTimeout(function () {
    flipBtn.disabled = false;
  }, 3000);
}

resetBtn.addEventListener("click", () => {
  coin.style.animation = "none";
  heads = 0;
  tails = 0;
  streak = 0;
  lastCoin = null;
  updateStats();
});

changeBgBtn.addEventListener("click", () => {
  let randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
  document.body.style.backgroundColor = randomColor;
});
