from fastapi import FastAPI
import uvicorn
from DAL.DAL_DB import DAL


app = FastAPI()

host = ''
user = ''
password = ''
database = ''
table = 'data'

def select_data(host, user, password, database, table):
    DAL_data = DAL(host= host, user= user, password= password,
                   database= database, table= table)
    data = DAL_data.select()
    return data


app.get('/data')
async def root():
    data = select_data(host= host, user= user, password= password,
                   database= database, table= table)
    return data



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)