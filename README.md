
# Python Final Project

The data has been downloaded from dataworld.com which is an opensource platform.

## Purposeof this project

The primary components of this project are a Jupyter notebook (Python_Project.ipynb) and a Flask web application (app.py). The basic purpose of this project is to read data from a CSV file called Titanic Disaster Dataset.CSV, save it in a SQLite database called python_project.db, and build a webpage to display the dataset.

## Files

### 1. Ship.py

This script establishes a connection to the database and reads a CSV file. Additionally, it demonstrates how to retrieve sample data from the dataset.

### 2. Titan.py

This file encompasses the Flask web application code, including the routing logic for three pages: the index page (also referred to as the home page), the About page, and the Data page.

### 3. templates

This folder contains the 3 html files i.e index.html, data.html, about.html.

## How to run the project


Execute the Jupyter notebook Ship.ipynb to extract and store data in the SQLite database. Launch the Flask web application by running the Titan.py file. Access the website through the specified routes, including the Index page, Data Page, and About page.

