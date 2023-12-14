from util.DBConnection import dbConnection
def InsertCompany():
    companyID = int(input("Enter Company ID: "))
    companyName = input("Enter Company Name: ")
    location = input("Enter Location: ")
    try:
        conn,stmt=dbConnection.open()
        data = [(companyID, companyName, location)]
        stmt.executemany('''INSERT INTO Company (companyID, companyName, location) VALUES (%s, %s, %s)''', data)
        conn.commit()

        print("Company inserted successfully.")

    except Exception as E:
        print(f"Error during insertion: {E}")
    finally:
         if conn:
             dbConnection.close(conn)
            
            
            
            
            
            