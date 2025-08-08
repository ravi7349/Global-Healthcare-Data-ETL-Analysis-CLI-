# Global Healthcare Data ETL & Analysis CLI



# Table of Contents
Project Description

Features

Technologies Used

Project Structure

Setup Instructions

Database Schema

How to Use

Sample Outputs


# Project Description
This project is a command-line interface (CLI) Python application that performs ETL (Extract, Transform, Load) on global healthcare COVID-19 data. It extracts data from CSV files or APIs, transforms it by cleaning and formatting, and loads it into a MySQL database for analysis. Users can query data interactively through the CLI for insights on hospital capacity and COVID-19 trends.

Why include this?
It clearly tells anyone what your project is and what problem it solves.


# Features
Extract healthcare data from CSV or APIs

Transform and clean data for consistency

Load cleaned data into a MySQL database

Interactive CLI to run analytical queries

Modular design for easy maintenance and extension

Why include this?
Users and collaborators want to know what the app can do.

# Technologies Used
Python 3.x

Pandas for data manipulation

MySQL database

mysql-connector-python for DB connection

CSV data files for input

CLI for user interaction

Why include this?
It helps users know the tools and dependencies involved.

# Project Structure

/GlobalHealthcareDataETL
│
├── main.py              # CLI entry point  
├── api_client.py        # Fetch data from API (optional)  
├── etl.py               # Extract, transform, load logic  
├── config.py            # Configurations (DB credentials, file paths)  
├── requirements.txt     # Python dependencies  
├── README.md            # Project documentation  
└── data/
    └── healthcare_data.csv  # Input CSV data  

# Setup Instructions
1. Prerequisites
Python 3.x installed

MySQL Server installed and running

# 1.Install Python packages:

pip install pandas mysql-connector-python

# 2. Database Setup
Create the database in MySQL:

CREATE DATABASE healthcare_db;

# 2.1 Update config.py with your database credentials:

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'healthcare_db'
}


# Database Schema

Example schema for the main table storing healthcare data:

CREATE TABLE hospital_covid_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(50),
    date DATE,
    total_beds INT,
    available_beds INT,
    icu_beds INT,
    available_icu_beds INT,
    covid_patients INT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# How to Use
Run ETL process to load data into the database:

python main.py --etl --file data/healthcare_data.csv


# Run interactive queries on the loaded data:

python main.py --query


# Sample Outputs




