def main():
    dinesh = input("Enter the filename you want to create: ")
    with open(dinesh, 'w') as file:
        file.write(input(f"Enter the content for '{dinesh}': "))
    print(f"Content successfully written to '{dinesh}'")
    
    with open(dinesh, 'r') as file:
        print(f"Content of '{dinesh}':")
        print(file.read())
    
    with open(dinesh, 'a') as file:
        file.write("\n" + input("Enter new content to append: "))
    print("Content successfully appended to the file.")
    
    confirmation = input(f"Are you sure you want to delete '{dinesh}'? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        import os
        os.remove(dinesh)
        print(f"File '{dinesh}' deleted successfully.")
    else:
        print(f"Deletion of '{dinesh}' canceled.")

if __name__ == "__main__":
    main()
