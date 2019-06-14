var interval;

function Go_() {
    var content = document.title;
    var firstChar = content.charAt(0);
    var sub = content.substring(1, content.length);
    document.title = sub +firstChar;
}

function Go() {
    interval = setInterval("Go_()", 500);
}

Go();

function Stop() {
    clearInterval(interval);
}