todo_list = []

def add_todo():
    title = input("Enter title of the todo: ")
    desc = input("Enter description of the todo: ")
    todo_list.append({'title': title, 'description': desc})
    print(f"Todo '{title}' added successfully!")

def display_todos():
    if not todo_list:
        print("Todo list is empty.")
    else:
        print("Todo List:")
        for index, todo in enumerate(todo_list, start=1):
            print(f"{index}. Title: {todo['title']}, Description: {todo['description']}")

def insert_todo():
    index = int(input("Enter the index where you want to insert the todo (1 to N): ")) - 1
    if 0 <= index <= len(todo_list):
        title = input("Enter title of the todo: ")
        desc = input("Enter description of the todo: ")
        todo_list.insert(index, {'title': title, 'description': desc})
        print(f"Todo '{title}' inserted successfully at index {index + 1}.")
    else:
        print("Invalid index.")

def delete_todo():
    index = int(input("Enter the index of the todo to delete (1 to N): ")) - 1
    if 0 <= index < len(todo_list):
        deleted_item = todo_list.pop(index)
        print(f"Todo '{deleted_item['title']}' deleted successfully.")
    else:
        print("Invalid index.")

def main():
    while True:
        print("\nTODO LIST APPLICATION")
        print("1. Add Todo")
        print("2. Display Todo List")
        print("3. Insert Todo")
        print("4. Delete Todo")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_todo()
        elif choice == '2':
            display_todos()
        elif choice == '3':
            insert_todo()
        elif choice == '4':
            delete_todo()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
