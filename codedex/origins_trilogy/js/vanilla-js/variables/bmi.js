"""
Instructions
The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.


bmi= 
height 
2
 
mass
​
 

Create a program that calculates your own BMI.

Author's note: Psst. BMI is an archaic and oversimplified way to measure personal health. It was created by a mathematician — not a doctor! 💡

"""



// bmi = mass / height**2

// I will be using metric system:

let mass = 104.33; // in kg
let height = 172.72 / 100 // in m

const bmi = mass / height ** 2;

console.log(bmi);
