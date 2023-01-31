#!/usr/bin/node
const number = Number(Math.trunc(process.argv[2]));
if (number){
console.log(`My Number: ${number}`);
}
else{
console.log{'Not a number'}
}
