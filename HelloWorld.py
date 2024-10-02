def main():
    print("Press 1 for 'Hello World!' or 2 for 'Goodbye!'")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("Hello World!")
    elif choice == '2':
        print("Goodbye!")
    else:
        print("Invalid choice. Please press 1 or 2.")

if __name__ == "__main__":
    main()
