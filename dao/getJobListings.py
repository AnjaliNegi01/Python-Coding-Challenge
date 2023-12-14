from util.DBConnection import dbConnection
def GetJobListings():
        try:
            from util.DBConnection import dbConnection
            conn,stmt=dbConnection.open()
            stmt.execute('''select * from JobListing''')
            records=stmt.fetchall()
            for i in records:
                print(i)
            return records
        except Exception as E:
            print(f"Error during retieval: {E}")