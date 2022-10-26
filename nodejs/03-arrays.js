var myArray = [1, 2, 3];

console.log(myArray);

console.log(myArray[2]);

var anotherArray = [
  1,
  "Hello, World",
  true,
  { name: "Allen" },
  [[0, 32, 43], 1, 2],
];
console.log(anotherArray[3]["name"]);
console.log(anotherArray[4][0][1]);

var myStack = [];
myStack.push(1);
myStack.push(5);
myStack.push(23);

console.log(myStack);

myStack.pop();
myStack.pop();
myStack.pop();

console.log(myStack);

var myOtherArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
var splice = myOtherArray.splice(3, 5);

console.log(splice);
