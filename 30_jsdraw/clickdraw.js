var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle"
        bToggler.innerHTML = "Circle";
    }
    else {
        mode = "rect"
        bToggler.innerHTML = "Rectangle";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillSyle = "red";
    ctx.fillRect(mouseX, mouseY, 100, 300)
}

var drawCircle = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillSyle = "red";
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
}

var draw = function(e) {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

var wipeCanvas = function(e) {
  ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
