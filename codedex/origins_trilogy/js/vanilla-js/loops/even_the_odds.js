"""
Instructions
Let's try out the continue and break keywords using even and odd numbers!

Write an even-odds.js file that begins with a for loop that iterates from 1 to 50.

If the iterator variable i is odd, use the continue keyword to skip this iteration. Otherwise, log the number to the Console.

If the iterator variable is equal to 42, log 42 to the Console and use the break keyword to exit the loop.

The output should look like this:

2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
"""



for (let i = 1; i <= 50; i++) {
  if (i % 2 === 1) {
    continue;
  } else if (i === 42) {
    console.log(i);
    break;
  } else {
    console.log(i);
  }
}
