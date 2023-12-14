from util.DBConnection import dbConnection
def GetApplicationsForJob():
        try:
            conn,stmt=dbConnection.open()
            stmt.execute('''select * from JobApplication''')
            records=stmt.fetchall()
            for i in records:
                print(i)
            return records
        except Exception as E:
            print(f"Error during retrieval: {E}") 