from fastapi import FastAPI
import uvicorn
from DAL.DAL_DB import DAL
import os


app = FastAPI()


app.state.db_host = os.getenv("DB_HOST", "localhost")
app.state.db_user = os.getenv("DB_USER", "")
app.state.db_password = os.getenv("DB_PASSWORD", "")
app.state.db_database = os.getenv("DB_DATABASE", "db_data")
app.state.db_table = os.getenv("DB_TABLE", "data")


app.get('/')
async def root():
    return {"message": "this API of data table with people full-names,"
            "by /data path"}


app.get('/data')
async def get_data():
    data = select_data(host= app.state.db_host,
                       user= app.state.db_user,
                       password= app.state.db_password,
                       database= app.state.db_database,
                       table= app.state.db_table)
    return data



def select_data(host, user, password, database, table):
    DAL_data = DAL(host= host, user= user, password= password,
                   database= database, table= table)
    data = DAL_data.select()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)