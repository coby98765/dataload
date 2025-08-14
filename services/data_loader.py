from fastapi import FastAPI
import mysql.connector
import uvicorn
import os

# DAL
class DAL:
    def __init__(self,url,user,pw,port):
        self.data_db = mysql.connector.connect(
        host=url,
        database = "dataload",
        user=user,
        password=pw,
        port =port)

    def get_all(self):
        try:
            my_cursor = self.data_db.cursor(dictionary=True)
            my_cursor.execute("SELECT * FROM data")
            data = my_cursor.fetchall()
            return data
        except Exception as ex:
            print(f"Error: {ex}")
            raise ex

DB_URL = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv('DB_USER',"root")
DB_PASS = os.getenv('DB_PASS',"")
DB_PORT = os.getenv('DB_PORT',3306)

dal = DAL(DB_URL,DB_USER,DB_PASS,DB_PORT)

# API
app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}

@app.get("/data")
def get_data():
    try:
        res = dal.get_all()
        return res
    except Exception as e:
        print(e)
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)