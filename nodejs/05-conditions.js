const name = "John Smith";

if (name === "John Smyth") {
  console.log("Hello John. How are you?");
} else {
  console.log("Then who the f are you?");
}

var foo = 1;
var bar = 2;

if (foo < bar) {
  console.log("foo is smaller that bar.");
}

var foo = 1;
var bar = 2;
var moo = 3;

// && = AND
// || = OR
if (foo < bar && moo > bar) {
  console.log("foo is smaller than var AND moo is larger than bar.");
}

var notTrue = false;
if (!notTrue) {
  console.log("not not true is true!");
}

var rank = "Commander";

switch (rank) {
  case "Private":

  case "Sergeant":
    console.log("You are not authorized");
    break;

  case "Commander":
    console.log("Hello commander");
    break;

  default:
    break;
}
