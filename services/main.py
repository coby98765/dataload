from fastapi import FastAPI
import mysql.connector
import uvicorn
import os

# DAL
class DAL:
    def __init__(self,url,user,pw):
        self.data_db = mysql.connector.connect(
        host=url,
        user=user,
        password=pw)

    def get_all(self):
        try:
            my_cursor = self.data_db.cursor()
            my_cursor.execute("SELECT * FROM data")
            data = my_cursor.fetchall()
            return data
        except Exception as ex:
            print(f"Error: {ex}")
            raise ex

DB_URL = os.environ['DB_URL']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

dal = DAL(DB_URL,DB_USER,DB_PASS)

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