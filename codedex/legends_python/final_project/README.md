
# Rock Paper Scissors Game

![Project Screenshot](screenshot.png)


This is the final project for the Codedex Python course.

It’s a simple Rock Paper Scissors game built with Python and Flask and displayed on a webpage.


## Technologies Used

- Python
- Flask
- HTML/CSS

## Folder Structure

```text
**final_project/
├── static/
│ └── main.css
├── app.py
└── README.md
```


## Navigate to the folder

- cd final_project


## Install virtual environment

- python -m venv venv


# Activate the venv

- source venv/bin/activate -> macOS/Linux

- venv\Scripts\activate -> Windows


# Install dependencies

- pip install flask


# Run the flask app

- python app.py  OR python3 app.py


# Open browser and go to

http://127.0.0.1:5000


P.S. if you want to run the app.py normally without flask:

make sure to comment out this:

# if __name__ == '__main__':
     app.run(debug=True)

