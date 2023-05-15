let optionsButtons = document.querySelectorAll(".option-button");
let advancedOptionButton = document.querySelectorAll(".adv-option-button");
let fontName = document.getElementById("fontName");
let fontSizeRef = document.getElementById("fontSize");
let writingArea = document.getElementById("text-input");
let linkButton = document.getElementById("createLink");
let alignButtons = document.querySelectorAll(".align");
let spacingButtons = document.querySelectorAll(".spacing");
let formatButtons = document.querySelectorAll(".format");
let scriptButtons = document.querySelectorAll(".script");

let fontList = [
    "Arial",
    "Verdana",
    "Times New Roman",
    "Garamond",
    "Georgia",
    "Courier New",
    "Cursive",
];

const intializer = () => {
    highlighter(alignButtons, true);
    highlighter(spacingButtons, true);
    highlighter(formatButtons, false);
    highlighter(scriptButtons, true);

    fontList.map((value) => {
        let option = document.createElement("option");
        option.value = value;
        option.innerHTML = value;
        fontName.appendChild(option);
    });

    for (let i = 1; i <= 7; i++) {
        let option = document.createElement("option");
        option.value = i;
        option.innerHTML = i;
        fontSizeRef.appendChild(option);
    }

    fontSizeRef.value = 3;
};
// 每当用户在编辑器中进行输入时，就保存他们的输入
writingArea.addEventListener("input", () => {
    localStorage.setItem("savedText", writingArea.innerHTML);
});


const modifyText = (command, defaultUi, value) => {
    document.execCommand(command, defaultUi, value);
};

optionsButtons.forEach((button) => {
    button.addEventListener("click", () => {
        modifyText(button.id, false, null);
    });
});

advancedOptionButton.forEach((button) => {
    button.addEventListener("change", () => {
        modifyText(button.id, false, button.value);
    });
});

linkButton.addEventListener("click", () => {
    let userLink = prompt("Enter a URL?");
    if (/http/i.test(userLink)) {
        modifyText(linkButton.id, false, userLink);
    } else {
        userLink = "http://" + userLink;
        modifyText(linkButton.id, false, userLink);
    }
});

const highlighter = (className, needsRemoval) => {
    className.forEach((button) => {
        button.addEventListener("click", () => {
            if (needsRemoval) {
                let alreadyActive = false;
                if (button.classList.contains("active")) {
                    alreadyActive = true;
                }
                highlighterRemover(className);
                if (!alreadyActive) {
                    button.classList.add("active");
                }
            } else {
                button.classList.toggle("active");
            }
        });
    });
};

const highlighterRemover = (className) => {
    className.forEach((button) => {
        button.classList.remove("active");
    });
};
let clearButton = document.getElementById("clear");

clearButton.addEventListener("click", () => {
    writingArea.innerHTML = "";
    localStorage.removeItem("savedText");
});

marked.setOptions({
    highlight: function (code, lang) {
        if (hljs.getLanguage(lang)) {
            return hljs.highlight(lang, code).value;
        } else {
            return hljs.highlightAuto(code).value;
        }
    },
});

writingArea.addEventListener("input", () => {
    const markdown = writingArea.value;
    const html = marked(markdown);
    writingArea.innerHTML = html;
    localStorage.setItem("savedText", html);
});

window.onload = () => {
    intializer();
    const savedText = localStorage.getItem("savedText");
    if (savedText) {
        writingArea.innerHTML = savedText;
    }
};

// 每当用户在编辑器中进行输入时，就保存他们的输入
writingArea.addEventListener("input", () => {
    localStorage.setItem("savedText", writingArea.innerHTML);
});

// 当页面加载时，检查是否有已保存的文本，如果有，就恢复
window.onload = () => {
    intializer();
    const savedText = localStorage.getItem("savedText");
    if (savedText) {
        writingArea.innerHTML = savedText;
    }
};
