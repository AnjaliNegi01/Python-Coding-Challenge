from util.DBConnection import dbConnection
def GetApplicants():
        try:
            conn,stmt=dbConnection.open()
            stmt.execute('''select * from Applicants''')
            records=stmt.fetchall()
            for i in records:
                print(i)
            return records
        except Exception as E:
            print(f"Error during retrieval: {E}") 