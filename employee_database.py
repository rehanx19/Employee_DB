employees = []


def add_employee():
    print("\nAdd employee")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    job = input("Job title: ")
    salary = input("Salary: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("That employee ID already exists.")
            return

    employee = {
        "id": emp_id,
        "name": name,
        "job": job,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added.")


def remove_employee():
    print("\nRemove employee")
    emp_id = input("Employee ID to remove: ")

    found = False
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            found = True
            print("Employee removed.")
            break

    if found == False:
        print("Employee not found.")


def update_salary():
    print("\nUpdate salary")
    emp_id = input("Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("Current salary:", emp["salary"])
            new_salary = input("New salary: ")
            emp["salary"] = new_salary
            print("Salary updated.")
            return

    print("Employee not found.")


def search_employee():
    print("\nSearch employee")
    search = input("Enter employee ID or name: ")
    found_any = False

    for emp in employees:
        if emp["id"] == search or search.lower() in emp["name"].lower():
            print("\nID:", emp["id"])
            print("Name:", emp["name"])
            print("Job:", emp["job"])
            print("Salary:", emp["salary"])
            found_any = True

    if not found_any:
        print("No matching employee found.")


def show_all_employees():
    print("\nEmployee list")

    if len(employees) == 0:
        print("No employees saved yet.")
        return

    for emp in employees:
        print(emp["id"], "-", emp["name"], "-", emp["job"], "- Salary:", emp["salary"])


def save_backup():
    file_name = "employee_backup.txt"
    backup = open(file_name, "w")

    backup.write("EMPLOYEE DATABASE BACKUP\n")
    backup.write("------------------------\n")

    for emp in employees:
        backup.write("ID: " + emp["id"] + "\n")
        backup.write("Name: " + emp["name"] + "\n")
        backup.write("Job: " + emp["job"] + "\n")
        backup.write("Salary: " + emp["salary"] + "\n")
        backup.write("\n")

    backup.close()
    print("Backup saved to", file_name)


def menu():
    while True:
        print("\n--- Employee Database ---")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Update salary")
        print("4. Search employee")
        print("5. Show all employees")
        print("6. Save backup to file")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_salary()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            show_all_employees()
        elif choice == "6":
            save_backup()
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


menu()
