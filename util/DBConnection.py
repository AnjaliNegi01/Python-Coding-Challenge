import mysql.connector as sql
class dbConnection:
    def open():
        try:
            conn=sql.connect(host="localhost",database="career",user="root",password="@Anjali10")
            stmt=conn.cursor()
            return conn,stmt
        except Exception as E:
            print(f"Database cannot connect: {E}")
            return None,None
            
    def close(conn):
        if conn:
            conn.close()