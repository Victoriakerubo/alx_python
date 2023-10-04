import requests
import csv
import sys

def get_employee_data(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee data
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Fetch TODO list data
    response = requests.get(todos_url)
    todos_data = response.json()

    return user_id, username, todos_data

def export_to_csv(employee_id):
    user_id, username, todos_data = get_employee_data(employee_id)

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            task_completed_status = todo["completed"]
            task_title = todo["title"]
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        export_to_csv(employee_id)
        print(f"Data has been exported to {employee_id}.csv")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
