def main():
    file_name = input("Enter the name of the file to read: ")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.rstrip())   
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except IOError as e:
        print(f"Error: IO Error occurred: {e}")

if __name__ == "__main__":
    main()