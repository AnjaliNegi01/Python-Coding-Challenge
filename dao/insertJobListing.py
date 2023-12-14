from util.DBConnection import dbConnection
from exceptions.negativeSalaryException import NegativeSalaryException,calculate_average_salary
def InsertJobListing():
            JobID = int(input("Enter Job ID: "))
            companyID = int(input("Enter Company ID: "))
            JobTitle = input("Enter Job Title: ")
            JobDescription = input("Enter Job Description: ")
            JobLocation = input("Enter Job Location: ")
            while True:
                try:
                    salary=int(input("enter the salary: "))
                    NegativeSalaryException(salary)
                    break
                except NegativeSalaryException as e:
                    print(f"Error Occured: {e}")

            JobType = input("Enter Job Type: ")
            PostedDate = input("Enter Posted Date: ")
            try:
                    conn,stmt=dbConnection.open()
                    data = [(JobID, companyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)]
                    stmt.executemany('''INSERT INTO JobListing (jobID, companyID, jobTitle, jobDescription, jobLocation, salary, jobType, postedDate)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', data)
                    conn.commit()
                    print("Job listing inserted successfully.")

            except Exception as E:
                print(f"Error during insertion: {E}")
            finally:
                    if conn:
                            dbConnection.close(conn)
            