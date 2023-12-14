from util.DBConnection import dbConnection
def GetCompanies():
        try:
            conn,stmt=dbConnection.open()
            stmt.execute('''select * from Company''')
            records=stmt.fetchall()
            for i in records:
                print(i)
            return records
        except Exception as E:
            print(f"Error during retrieval: {E}")



            