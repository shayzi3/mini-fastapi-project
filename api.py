
from random import choice
from fastapi import FastAPI

from models.base import data_command
from src.validation import Register, NameUp


app = FastAPI()


@app.get('/users/{user_id}')
async def get_user(user_id: int):
     check = await data_command.get_user_tables(id = user_id)
     
     if check:
          return {'id': user_id, 'name': check}
     
     return {'status': 404, 'message': 'User was not found'}



@app.post('/new_name')
async def update_name(data: NameUp):
     check = await data_command.update_data_tables(
          id = data.your_id,
          new_name = data.new_name,
          pass_ = data.password
     )
     
     if check:
          return {'status': 200, 'message': 'Nickname change success!'}
     
     return {'status': 323, 'message': 'Invalid password!'}
     



@app.post('/reg')
async def register_user(reg: Register):
     id = choice([i for i in range(100, 301)])
     
     await data_command.insert_data_tables(
          id = id,
          name = reg.name,
          pass_ = reg.password
     )
     
     return {'status': 200, 'message': f'New account create success! Your ID: {id}'}
     

          
     
     