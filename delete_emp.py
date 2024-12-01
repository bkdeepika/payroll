import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root',
            database='employee_payroll'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create Employee Table
def create_table():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    position VARCHAR(50),
                    salary DECIMAL(10, 2),
                    hire_date DATE
                )
            """)
            connection.commit()
            print("Employee table created successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Add a New Employee
def add_employee():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            hire_date = input("Enter hire date (YYYY-MM-DD): ")

            sql_insert_query = """
                INSERT INTO employees (name, position, salary, hire_date)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql_insert_query, (name, position, salary, hire_date))
            connection.commit()
            print("Employee added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# View All Employees
def view_employees():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()

            if rows:
                print("\nEmployee List:")
                print("ID | Name | Position | Salary | Hire Date")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
            else:
                print("No employees found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Update Employee Information
def update_employee():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            employee_id = int(input("Enter employee ID to update: "))
            new_salary = float(input("Enter new salary: "))

            sql_update_query = "UPDATE employees SET salary = %s WHERE id = %s"
            cursor.execute(sql_update_query, (new_salary, employee_id))
            connection.commit()

            if cursor.rowcount > 0:
                print("Employee salary updated successfully.")
            else:
                print("Employee not found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Delete an Employee
def delete_employee():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            employee_id = int(input("Enter employee ID to delete: "))

            sql_delete_query = "DELETE FROM employees WHERE id = %s"
            cursor.execute(sql_delete_query, (employee_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Main Menu
def main():
    create_table()
    while True:
        print("\nEmployee Payroll System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")


        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

  

  