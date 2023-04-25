/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team JiangPark Morgan :: Ian Jiang, Gitae Park 
// SoftDev pd7
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//typing f(2) in the console outputs 32

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };
//typing o in the console outputs the object
//typing o.func(3) outputs 33 in the console


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
//addItem("hi") added another element to the list in the html file

var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
//removeItem(8) removed the last item in the list because there were 9 total items.

var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
//red() added red to every item in the list. The first and last items became red and the middle items stayed the same.

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
//stripe() added red to every other item in the list and blue to the other items. The only visible change was that the last item became blue. It was red before.
//insert your implementations here for...
// FIB
var fib = function(n) {
  if (n < 2){
      return n;
  } else {
      return fib(n-1) + fib(n-2);
  }
};
// FAC
var fac = function(num) {
  if(num < 2 ){
    return 1;
  } else {
    return num * fac(num - 1);
  }
};
// GCD
var gcd = function(a,b) {
  if (b == 0){
    return a;
  } else {
    return gcd(b, a%b);
  }
};
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  var retVal = param1 * param2;
  return retVal;
};
//functions the same as the previous syntax

console.log("the 3rd fib number is " + fib(3));
console.log("the 3! is " + fac(3));
console.log("the gcd of 3 and 7 is " + gcd(3,7));
