Email and Username Availability Checker

This Python script allows you to check the availability of email addresses and usernames using specific API endpoints. It supports checking a single email or username, or processing lists from text files.
Features

    Check a single email for availability.
    Check a single username for availability.
    Batch check emails from a text file.
    Batch check usernames from a text file.
    Handles HTTP requests and error responses gracefully.

Requirements

    Python 3.7 or later
    requests library

Install the required library using:

pip install requests

Usage
Command-Line Arguments

The script supports the following command-line arguments:

    --email: Check a single email address.
    --username: Check a single username.
    --email_file: Provide a text file with a list of email addresses to check.
    --username_file: Provide a text file with a list of usernames to check.

Examples
Check a Single Email

python availability_checker.py --email test@example.com

Check a Single Username

python availability_checker.py --username testuser

Check Emails from a File

Provide a file (emails.txt) with one email per line:

python availability_checker.py --email_file emails.txt

Check Usernames from a File

Provide a file (usernames.txt) with one username per line:

python availability_checker.py --username_file usernames.txt

Input File Format

For batch processing, ensure the input file has one entry per line:

emails.txt

test1@example.com
test2@example.com

usernames.txt

user1
user2

Output

The script will output the results for each email or username, displaying either the availability status or an error message.

Example Output:

Email Check Result: {'email': 'test@example.com', 'available': True}
Username Check Result: {'username': 'testuser', 'available': False}
