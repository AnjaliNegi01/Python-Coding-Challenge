from util.DBConnection import dbConnection
from exceptions.fileuploadException import FileUploadError, upload_cover_letter
from exceptions.deadLineException import ApplicationDeadlineError
from datetime import datetime
def InsertJobApplication():
     try:
        conn,stmt=dbConnection.open()
        ApplicationID = int(input("Enter Application ID: "))
        JobID = int(input("Enter Job ID: "))
        ApplicantID = int(input("Enter Applicant ID: "))
        ApplicationDate = input("Enter Application Date (YYYY-MM-DD HH:MM:SS): ")
        CoverLetterFile = input("Enter the path of the cover letter file: ")
            # Read the content of the file
        while True:
            try:
                upload_cover_letter(CoverLetterFile)
                with open(CoverLetterFile, 'r') as file:
                    CoverLetter = file.read()
                    
                    stmt.execute('SELECT deadLine FROM JobListing WHERE JobID = %s', (JobID,))
                    deadline_result = stmt.fetchone()

                    if deadline_result:
                        deadline = deadline_result[0]
                        current_time = datetime.strptime(ApplicationDate, "%Y-%m-%d %H:%M:%S")

                    if current_time > deadline:
                        raise ApplicationDeadlineError("Application deadline has passed. Application not accepted")
                

                    data = [(ApplicationID, JobID,ApplicantID, ApplicationDate, CoverLetter)]

                    # Insert data into the JobApplications table
                    stmt.executemany('''
                    INSERT INTO JobApplication (ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter)
                    VALUES (%s, %s, %s, %s, %s)''', data)

                    conn.commit()
                    print("Job Application inserted successfully.")
            except FileUploadError as ex:
                print(f"Error: {ex}")
     except Exception as E:
        print(f"Error during insertion: {E}")
     finally:
        if conn:
            dbConnection.close(conn)