import argparse
import requests

def check_email_availability(email):
    url = f"https://api.x.com/i/users/email_available.json?email={email}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"email": email, "error": str(e)}

def check_username_availability(username):
    url = f"https://api.x.com/i/users/username_available.json?username={username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"username": username, "error": str(e)}

def process_file(file_path, check_function):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                item = line.strip()
                if item:
                    results.append(check_function(item))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return results

def main():
    parser = argparse.ArgumentParser(description="Check email or username availability.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--email", help="Check a single email")
    group.add_argument("--username", help="Check a single username")
    group.add_argument("--email_file", help="Check emails from a text file")
    group.add_argument("--username_file", help="Check usernames from a text file")

    args = parser.parse_args()

    if args.email:
        result = check_email_availability(args.email)
        print(f"Email Check Result: {result}")
    elif args.username:
        result = check_username_availability(args.username)
        print(f"Username Check Result: {result}")
    elif args.email_file:
        results = process_file(args.email_file, check_email_availability)
        for result in results:
            print(f"Email Check Result: {result}")
    elif args.username_file:
        results = process_file(args.username_file, check_username_availability)
        for result in results:
            print(f"Username Check Result: {result}")

if __name__ == "__main__":
    main()
