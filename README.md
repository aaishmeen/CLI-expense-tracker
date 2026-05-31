# CLI Expense Tracker

A command-line expense management application built using Python. This project enables users to record, manage, search, and analyze personal expenses through an interactive terminal-based interface while persisting data using JSON storage.

## Project Overview

 The project focuses on data management, user interaction, file handling, and code organization while following industry-standard Git and GitHub workflows.

## Features

### Expense Management

* Add new expenses
* View all recorded expenses
* Delete existing expenses
* Search expenses by category

### Expense Analysis

* Calculate total spending

### Data Persistence

* Save expenses to a JSON file
* Automatically load saved expenses when the application starts

### User Experience

* Interactive menu-driven interface
* Formatted tabular display
* Screen clearing for improved readability
* Pause-and-continue functionality
* Input validation for user actions

## Concepts Applied

* Functions and Functional Decomposition
* Lists and Dictionaries
* File Handling (File I/O)
* JSON Serialization and Deserialization
* Data Persistence
* Control Flow and Conditional Logic
* Iteration using Loops
* Search and Filtering Operations
* String Formatting
* Command-Line Interface (CLI) Design
* Software Refactoring and Code Reusability

## Project Structure


CLI-expense-tracker/
│
├── main.py
├── expenses.json
├── README.md


## Application Workflow


Start Program
      │
      ▼
 Load Expenses
      │
      ▼
 Display Menu
      │
      ▼
 ┌─────┬─────┬─────┬─────┬─────┐
 ▼     ▼     ▼     ▼     ▼
Add   View  Total Delete Search
      │
      ▼
 Save Changes
      │
      ▼
 Return to Menu
      │
      ▼
     Exit


## Future Enhancements

* Monthly expense summaries
* Budget tracking
* Date-wise expense filtering
* Expense reports and analytics
* Data export functionality
* Flask-based web application version
* User authentication and profiles


## Learning Outcomes

Through this project, I gained practical experience in:

* Python Programming
* Data Structures
* File Handling
* JSON-Based Storage
* Software Refactoring
* Version Control using Git and GitHub
* Problem Solving and Debugging
* Incremental Software Development


