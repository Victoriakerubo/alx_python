import requests
import json

def get_employee_todo_list_progress(employee_id):
  """Gets the TODO list progress for the given employee ID.

  Args:
    employee_id: The employee ID.

  Returns:
    A dictionary containing the employee TODO list progress. The dictionary has the
    following keys:
      employee_name: The name of the employee.
      number_of_done_tasks: The number of completed tasks.
      total_number_of_tasks: The total number of tasks.
      completed_task_titles: A list of the titles of the completed tasks.
  """

  # Get the employee details.
  employee_response = requests.get(
      f"https://jsonplaceholder.typicode.com/users/{employee_id}")
  employee_details = json.loads(employee_response.content)

  # Get the employee TODO list.
  todos_response = requests.get(
      f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
  todos = json.loads(todos_response.content)

  # Calculate the employee TODO list progress.
  number_of_done_tasks = 0
  total_number_of_tasks = len(todos)
  completed_task_titles = []
  for todo in todos:
    if todo["completed"]:
      number_of_done_tasks += 1
      completed_task_titles.append(todo["title"])

  # Return the employee TODO list progress.
  return {
      "employee_name": employee_details["name"],
      "number_of_done_tasks": number_of_done_tasks,
      "total_number_of_tasks": total_number_of_tasks,
      "completed_task_titles": completed_task_titles,
  }
def main():
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee TODO list progress.
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  # Display the employee TODO list progress.
  print(f"Employee {employee_todo_list_progress['employee_name']} is done with tasks({employee_todo_list_progress['number_of_done_tasks']}/{employee_todo_list_progress['total_number_of_tasks']}):")
  for completed_task_title in employee_todo_list_progress["completed_task_titles"]:
    print(f"\t{completed_task_title}")


if __name__ == "__main__":
  main()
