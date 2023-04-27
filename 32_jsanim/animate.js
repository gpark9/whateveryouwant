var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

ctx.fillStyle = "cyan";
var requestID;
var radius = 0;
var growing = true;


var drawDot = () => {
    window.cancelAnimationFrame(requestID);
    
    clear();

    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();

    console.log(radius);
    if (radius >= 250) {
        growing = false;
    }
    
    if (radius == 0) {
        growing = true;
    }

    console.log(growing);
    if (growing) {
        radius += 1;
    }
    else {
        radius -= 1;
    }

    requestID = window.requestAnimationFrame(drawDot);
};

var clear = function(e) {
    //e.preventDefault();
    ctx.clearRect(0, 0, 500, 500);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 120;
    var rectHeight = 80;

    var rectX = Math.random() * (c.width - rectWidth);
    var rectY = Math.random() * (c.height - rectHeight);

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0,0,c.width,c.height);
        //ctx.fillRect(rectX,rectY,rectWidth,rectHeight);
        ctx.drawImage(logo,rectX,rectY,rectWidth,rectHeight);
        if (rectX + rectWidth >= c.width || rectX <= 0) {
            xVel = -xVel;
        }
        if (rectY + rectHeight >= c.height || rectY <= 0) {
            yVel = -yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};

var stopIt = function() {
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);
