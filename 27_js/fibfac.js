// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------

function factorial(num) {
    if(num < 2 ){
      return 1;
    } else {
      return num * factorial(num - 1);
    }
  }
  
  console.log(factorial(1));
  console.log(factorial(2));
  console.log(factorial(3));
  console.log(factorial(4));
  console.log(factorial(5)); // Output: 120
  

function fib(n) {
    if (n < 2){
        return n;
    } else {
        return fib(n-1) + fib(n-2);
    }
}

console.log(fib(0));
console.log(fib(1));
console.log(fib(2));
console.log(fib(3));
console.log(fib(4));

// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
