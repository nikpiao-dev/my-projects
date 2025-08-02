"""

Instructions
Let's put these operators to use!

Create a temperature.js program that converts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in JavaScript:


Celsius= 
1.8
(Fahrenheit−32)
​
 

Print out the converted temperature using console.log().

"""



/* 

Fahrenheit (°F) to Celsius (°C) Formula:
  -> Celcius = (F - 32) / 1.8

*/


let temp = 68; // in Fahrenheit

let celcius = (temp - 32) / 1.8

console.log("Temperature in Fahrennheit: ", temp);
console.log("Temperature in celcius: ", celcius);

