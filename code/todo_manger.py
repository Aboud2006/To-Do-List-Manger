def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print("Task added successfully!")
            else:
                print("Empty task not added.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour Tasks:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
                try:
                    index = int(input("Enter the number of the task to remove: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("Number out of range.")
                except ValueError:
                    print("Invalid number.")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if name == "__main__":
    main()
