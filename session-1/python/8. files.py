# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.
# Example 1: Writing to a Text File
# with open('python/data/example.txt', 'w') as file:
#     file.write("Hello, Python developers!\n")
#     file.write("Welcome to file I/O operations.")

# # Example 2: Reading from a Text File
# with open('python/data/example.txt', 'r') as file:
#     content = file.read() # readlines(), readlines()
#     print(content)

# # Section 2: CSV Files
# # --------------------
# # CSV (Comma-Separated Values) files are commonly used for storing tabular data.

# import csv

# # Example 3: Writing to a CSV File
# with open('data/example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 28, "New York"])
#     writer.writerow(["Bob", 22, "Los Angeles"])
#     writer.writerow(["Carol", 24, "Chicago"])

# # Example 4: Reading from a CSV File
# with open('data/example.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# # Section 3: JSON Data
# # --------------------
# # JSON (JavaScript Object Notation) is a lightweight data-interchange format.

# import json

# # Example 5: Writing JSON to a File
# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# with open('data/data.json', 'w') as file:
#     json.dump(data, file)


# # Example 6: Reading JSON from a File
# with open('data/data.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# # Section 4: Practical Applications
# # ---------------------------------
# # Combining file I/O with real-world data processing.

# # Example 7: Processing JSON Data from a File
# # Suppose we have a JSON file containing multiple user records.
# users = [
#     {"name": "Alice", "age": 25, "email": "alice@example.com"},
#     {"name": "Bob", "age": 30, "email": "bob@example.com"}
# ]
# with open('data/users.json', 'w') as file:
#     json.dump(users, file)

# with open('data/users.json', 'r') as file:
#     users = json.load(file)
#     for user in users:
#         print(f"{user['name']} ({user['age']}): {user['email']}")

# # Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

# import csv
# import json

# with open('python/data/my_csv.csv','w', newline='' ) as file:
#     writer = csv.writer(file)
#     writer.writerow(["Product Name", "Brand", "Price"])
#     writer.writerow(["Laptop", "HP", 40000])
#     writer.writerow(["Smartphone", "Samsung", 55000])
#     writer.writerow(["Television", "LG", 60000])

# with open('python/data/my_csv.csv','r') as file:
#     reader = csv.DictReader(file)
#     dictionary = [i for i in reader]

# with open('python/data/my_json.json','w') as file:
#     json.dump(dictionary,file)

# with open('python/data/my_json.json','r') as file:
#     reader = json.load(file)
#     for i in reader:
#         print(f"{i['Product Name']} ({i['Brand']}): {i['Price']} tk.")

    # Assignment 2: Create a log file writer that appends log messages to a file with timestamps.


from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = [f"{timestamp} 6013 The system uptime is 696208 seconds.", f"{timestamp} 24 The time zone information was refreshed with exit reason 0. Current time zone bias is -360.", f"{timestamp} 7021 Connection telemetry fields and analysis usage.", f"{timestamp} 1014 Name resolution for the name optimizationguide-pa.googleapis.com timed out after none of the configured DNS servers responded."]

with open('python/data/my_log.log','a') as file:
    for i in data:
        file.writelines(i+'\n')

with open('python/data/my_log.log','r') as file:
    for line in file:
        print(line.strip())
        
# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.