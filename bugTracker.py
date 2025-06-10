
# Task 1: Set Up Initial Data Structures
# Create dictionaries for bugs and developers with sample entries using nested dictionaries, sets, lists, and tuples.
# Task 2: Add a New Bug Report
# Implement a function to add a new bug to the bugs dictionary using user input.
# Task 3: Assign a Bug to Developer
# Write logic to assign a bug to a developer based on skills and availability using set operations.
# Task 4: Update Bug Status
# Implement a function to update the status of a bug through valid transitions (Open → In Progress → Closed).
# Task 5: Filter and Display Bugs
# Create functions to display bugs by severity and status using loop and conditional filtering.
# Task 6: Developer Performance Dashboard
# Generate a report showing top-performing developers, average bugs resolved, and available developers.
# Task 7: Suggest Similar Bugs by Tags
# Find and display similar bugs based on shared tags using set intersection.
# Task 8: Detect Stale Bugs
# Identify and list bugs that are still open and reported more than 7 days ago using tuple dates and the datetime module.
# Task 9: Command-Line Menu Interface
# Build a basic command-line interface to interact with the system using menu options and function calls

from datetime import datetime
from datetime import date

bugs = {
    "BUG001": {
        "title": "Login button unresponsive",
        "severity": "High",
        "status": "Open",
        "tags": {"frontend", "authentication", "UI"},
        "reported_date": (2025, 5, 1),
        "assigned_to": None
    },
    "BUG002": {
        "title": "Crash on profile update",
        "severity": "Critical",
        "status": "In Progress",
        "tags": {"backend", "database"},
        "reported_date": (2025, 4, 25),
        "assigned_to": "DEV002"
    },
    "BUG003": {
        "title": "Typo in welcome message",
        "severity": "Low",
        "status": "Closed",
        "tags": {"frontend", "content"},
        "reported_date": (2025, 3, 15),
        "assigned_to": "DEV003"
    }
}
 
developers = {
    "DEV001": {
        "name": "Alice",
        "skills": {"frontend", "UI", "React"},
        "assigned_bugs": ["BUG003"],
        "bugs_resolved": 5
    },
    "DEV002": {
        "name": "Bob",
        "skills": {"backend", "database", "Python"},
        "assigned_bugs": ["BUG002"],
        "bugs_resolved": 3
    },
    "DEV003": {
        "name": "Charlie",
        "skills": {"authentication", "security", "frontend"},
        "assigned_bugs": [],
        "bugs_resolved": 4
    }
}


# Task 2
def adding_bug_details():
    while True:
        add_bug = input("do you want to add any bug YES or NO :")
        if add_bug == "YES" :
            bugid = input("Enter bug ID:")
            title = input("Enter bug Title:")
            severity = input("Enter the severity of the bug:")
            status = input("Enter status of the bug : ")
            tags_input = input("Enter tags (In comma separated): ")
            tags = set(tag.strip() for tag in tags_input.split(","))
            reported_date = input("Enter date:")
            assigned_to = input("Whom it is assigned to:")
        
            bugs[bugid] = {"title": title,
                    "severity": severity,
                    "status": status,
                    "tags": tags,
                    "reported_date": reported_date,
                    "assigned_to": assigned_to}
        else:
            break
    print(bugs)
# adding_bug_details()

# Task 3
# Write logic to assign a bug to a developer based on skills and availability using set operations.
def bug_assigner():
    for bug_id, bug_info in bugs.items():
        if bug_info["assigned_to"] is None:
            for dev_id, dev_info in developers.items():
                if bug_info["tags"] & dev_info["skills"]:
                    bug_info["assigned_to"] = dev_id
                    dev_info["assigned_bugs"].append(bug_id)
                    break  
    print("\n Assigning a bug to developer based on skills and availability","\n find the below updated data :", bugs)
# bug_assigner()

# Task4
# Update Bug Status
# Implement a function to update the status of a bug through valid transitions (Open → In Progress → Closed)
def update_status():
    for bug_id, bug_info in bugs.items():
        if bug_info["status"] == "Open":
            bug_info["status"] = "In Progress"
        elif bug_info["status"] == "In Progress":
            bug_info["status"] = "Closed"
    print("\n Implementing the status of a bug through transitions :",bugs)
# update_status()

# Task5
# Create functions to display bugs by severity and status using loop and conditional filtering.
def print_bug_details(bug_id, bug_info):
    print(f"\nBug ID       : {bug_id}")
    print(f"Title        : {bug_info['title']}")
    print(f"Severity     : {bug_info['severity']}")
    print(f"Status       : {bug_info['status']}")
    print(f"Tags         : {', '.join(bug_info['tags'])}")
    print(f"Reported Date: {bug_info['reported_date']}")
    print(f"Assigned To  : {bug_info['assigned_to'] if bug_info['assigned_to'] else 'Unassigned'}")

def display_status_severity():
    print("\nDisplaying the bugs by severity and Status : ")
    severity = input("\nEnter the severity (Low, Critical, High): ")
    status = input("Enter the status (Open, In Progress, Closed): ")
    for bug_id, bug_info in bugs.items():
        if bug_info["severity"] == severity:
            print(print_bug_details(bug_id, bug_info))
    for bug_id, bug_info in bugs.items():
        if bug_info["status"] == status:
            print(print_bug_details(bug_id, bug_info))

# display_status_severity()

# Task6
#  Generate a report showing top-performing developers, average bugs resolved, and available developers.
def report():
    # one
    top_performer = []
    max_bugs = max(dev["bugs_resolved"] for dev in developers.values())
    
    for dev_id, dev_info in developers.items():
       if dev_info["bugs_resolved"] == max_bugs:
           top_performer.append(dev_info["name"])
    print("Top Performer:" ,top_performer)

    # two
    total = sum(dev_info["bugs_resolved"] for dev_info in developers.values())
    avg_bugs = total/len(developers)
    print("Average bugs resolved:",avg_bugs)

    # three
    available_developer = []
    for dev_id, dev_info in developers.items():
       if dev_info["assigned_bugs"] == []:
           available_developer.append(dev_info["name"])
    print("Available Developer:" ,available_developer)

# report()

# Task 7: Suggest Similar Bugs by Tags
# Find and display similar bugs based on shared tags using set intersection.

def display_bugs():
    user_input = input("Enter the bugID to get the Bugs with similar Tag: ")
    similar = []
    for bug_id, bug_info in bugs.items():
        if bug_id != user_input:
            if bugs[user_input]["tags"] & bugs[bug_id]["tags"]:
                similar.append(bug_id)
                print("Similar Bugs for the provided bugID are: ",similar)

# display_bugs()

# Task 8: Detect Stale Bugs
# Identify and list bugs that are still open and reported more than 7 days ago using tuple dates and the datetime module.
def date_diff():
    today = datetime.today().date()
    open_bugs = []
    for bug_id, bug_info in bugs.items():
        p_date = bugs[bug_id]["reported_date"]
        year, month, day = (p_date)
        # year += 2000
        prev_date = date(year,month,day)
        diff = abs((today - prev_date).days)
        if diff >= 7 and bug_info["status"] == "Open" :
            open_bugs.append(bug_id)
    print("Bugs that are still open and reported more than 7 days ago :",open_bugs)

# date_diff()

# Task 9: Command-Line Menu Interface
# Build a basic command-line interface to interact with the system using menu options and function calls

def menu():
    print("---------------MENU----------------")
    print("01-Add a New Bug Report")
    print("02-Assign a Bug to Developer")
    print("03-Update Bug Status")
    print("04-Filter and Display Bugs")
    print("05-Developer performance Dashboard")
    print("06-Suggest Similar Bugs by Tags")
    print("07-Detect scale bugs")

while True:
    menu()
    choice= input("\nEnter the options from the -MENU- (01-07) || Enter -EXIT- to exit ")

    if choice == '01':
        adding_bug_details()
    elif choice == '02':
        bug_assigner()
    elif choice == '03':
        update_status()
    elif choice == '04':
        display_status_severity()
    elif choice == '05':
        report()
    elif choice == '06':
        display_bugs()
    elif choice == '07':
        date_diff()
    elif choice == "EXIT":
        break
    else:
        print("Invalid choice. Please enter a number between 01 and 07.")


