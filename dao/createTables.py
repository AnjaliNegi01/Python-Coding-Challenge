from util.DBConnection import dbConnection

# Example usage
def createTable():
    conn=None 
    try:
            conn,stmt=dbConnection.open()
            if conn:
                 stmt.execute('''create table if not exists Company(companyID INT PRIMARY KEY, 
                                 companyName varchar(30), 
                                 Location varchar(30))''')
                 
                 stmt.execute('''create table if not exists JobListing(JobID int primary key, 
                                 companyID int,
                                 JobTitle varchar(20),
                                 JobDescription varchar(100),
                                 JobLocation varchar(30),
                                 Salary decimal(10,2),
                                 JobType varchar(20),
                                 PostedDate datetime,
                                 FOREIGN KEY (companyID) REFERENCES Company(companyID))''')
            
                 stmt.execute('''create table if not exists Applicants(ApplicantID int primary key,
                                 FirstName varchar(20),
                                 LastName varchar(20),
                                 Email varchar(30),
                                 Phone char(10),
                                 Resume text)''')
            
                 stmt.execute('''create table if not exists JobApplication(ApplicationID int primary key,
                                 JobID int,
                                 ApplicantID int,
                                 ApplicationDate datetime,
                                 CoverLetter text,
                                 FOREIGN KEY (JobID) REFERENCES JobListing(JobID),
                                 FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID))''')
            
            print("Database initialized successfully.")
            
    except Exception as e:
         print(f"Error during database initialization: {e}")
            
            
    finally:
        if conn:
             dbConnection.close(conn)
