from util.DBConnection import dbConnection
def searchBySalary():
        try:
            conn,stmt=dbConnection.open()
            minSalary=float(input("Enter min Salary:"))
            maxSalary=float(input("Enter max Salary: "))
            data = (minSalary,maxSalary)
            stmt.execute('''select JobTitle, Salary from JobListing 
                            where Salary between %s and %s''',data)
            
            result = stmt.fetchall()
            dbConnection.close(conn)
            if result:
                print("Job listings are present within specified salary range")
                for row in result:
                    print(f'Job Title:{row[0]} Salary:{row[1]}')
            else:
                print("No job listings found within the specified salary range.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            dbConnection.close(conn)