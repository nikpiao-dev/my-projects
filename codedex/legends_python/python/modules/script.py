"""
Instructions
Note: For this exercise, an outside code editor is needed. We recommend using VS Code. Check out this article to get started.

It's time to try out a Python package!

First, make sure pip is installed by running pip3 in a terminal. If not, follow the steps to do so here.

Next, install a package called wikipedia.

pip3 install wikipedia

Next, create a new file called wiki.py.

Then, use the wikipedia package's documentation to search for a phrase of your choice.

A few examples could be:

"Philosophy of life"
"Python (programming language)"
"Galaxy"
Try running this program in the terminal with:

python3 wiki.py

"""



import wikipedia

wikipedia.summary()
print(wikipedia.search('Philosophy of life'))
