from util.DBConnection import dbConnection
from exceptions.invalidEmailErrorException import InvalidEmailFormatError, validate_email
from exceptions.fileuploadException import FileUploadError, upload_cover_letter

def InsertApplicant():
    try:
        conn,stmt=dbConnection.open()
        ApplicantID = int(input("Enter Applicant ID: "))
        FirstName = input("Enter First Name: ")
        LastName = input("Enter Last Name: ")
        #calling file upload error
        while True:
            try:
                Email = input("Enter Email: ")
                validate_email(Email)
                break
            except InvalidEmailFormatError as ex:
                print(f"Unexpected error: {ex}")
                    
        Phone = input("Enter Phone: ")
        ResumeFile = input("Enter Resume file path: ")
        while True:
            try:
                upload_cover_letter(ResumeFile)
                with open(ResumeFile,'r') as file:
                    Resume=file.read()
               

                data = [(ApplicantID, FirstName,LastName,Email, Phone,Resume)]

                # Insert data into the Applicants table
                stmt.executemany('''INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume)
                VALUES (%s, %s, %s, %s, %s, %s)''', data)

                conn.commit()
                print("Applicant inserted successfully.")
            except FileUploadError as ex:
                print(f"Error: {ex}")

    except Exception as E:
        print(f"Error during insertion: {E}")
    finally:
        if conn:
            dbConnection.close(conn)