import requests
import sys

def get_employee_data(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee data
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list data
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    return employee_name, completed_tasks, total_tasks, [todo["title"] for todo in todos_data if todo["completed"]]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_name, completed_tasks, total_tasks, completed_titles = get_employee_data(employee_id)
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        for title in completed_titles:
            print(f"\t{title}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
