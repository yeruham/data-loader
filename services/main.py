from fastapi import FastAPI
import uvicorn
from DAL.DAL_DB import DAL_DB
import os


app = FastAPI()

port = 3306
app.state.db_host = os.getenv("DB_HOST", "localhost")
app.state.db_port = int(os.getenv("DB_PORT", 3306))
app.state.db_user = os.getenv("DB_USER", "root")
app.state.db_password = os.getenv("DB_PASSWORD", "")
app.state.db_database = os.getenv("DB_DATABASE", "eagleEyeDB")
app.state.db_table = os.getenv("DB_TABLE", "agents")


@app.get('/')
async def root():
    return {"message": "this API of data table with people full-names,"
            "by /data path"}


@app.get('/data')
async def get_data():
    data = select_data(host= app.state.db_host,
                       port= app.state.db_port,
                       user= app.state.db_user,
                       password= app.state.db_password,
                       database= app.state.db_database,
                       table= app.state.db_table)

    return data



def select_data(host, port, user, password, database, table):
    DAL_data = DAL_DB(host= host, port= port, user= user, password= password,
                   database= database, table= table)
    data = DAL_data.select()
    return data



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8001)