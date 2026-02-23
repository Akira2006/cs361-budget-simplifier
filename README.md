# CS361 Budget Simplifier by Akira

## Overview

This repository contains:

1. Main Program:
   - budget_simplifier.py (CLI Budget Application)

2. Budget Calculation Microservice:
   - budget_microservice.py
   - test_program.py

The microservice communicates using JSON files and does not directly call the test program.

---

# Budget Calculation Microservice

## Description

This microservice processes a total budget and category percentages provided in JSON format.  
It calculates dollar amounts for each category, validates the total percentage, and returns a structured JSON response.

The microservice communicates through JSON files (request.json and response.json).

---

## Communication Contract

### Request Format

The requesting program must create a file named:

request.json

With the following structure:

{
    "total_budget": 2000,
    "categories": {
        "Rent": 50,
        "Food": 30,
        "Gym": 10
    }
}

- total_budget must be a positive number.
- categories must be a dictionary of category names and percentage values.

---

### How to Request Data

1. Create request.json in the same directory.
2. Run:

python budget_microservice.py

The microservice reads the request file and processes the data.

---

### Response Format

The microservice writes a file named:

response.json

With the following structure:

{
    "total_percentage": 90,
    "breakdown": {
        "Rent": {
            "percentage": 50,
            "amount": 1000.0
        },
        "Food": {
            "percentage": 30,
            "amount": 600.0
        },
        "Gym": {
            "percentage": 10,
            "amount": 200.0
        }
    },
    "unassigned": {
        "percentage": 10,
        "amount": 200.0
    },
    "status": "incomplete"
}

Status values:
- "valid" → total percentage equals 100
- "incomplete" → total percentage less than 100
- "invalid" → total percentage greater than 100

---

## UML Sequence Overview

Sequence of communication:

1. Test Program writes request.json
2. Budget Microservice reads request.json
3. Budget Microservice processes the budget
4. Budget Microservice writes response.json
5. Test Program reads response.json

The test program and microservice do not directly call each other.  
They communicate indirectly through JSON files.
