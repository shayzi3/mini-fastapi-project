
from sqlalchemy import select, update, insert

from models.model import Pool, Tables


class DataCommands(Pool):
     
     @classmethod
     async def get_user_tables(cls, id: int) -> str:
          async with cls._sessions() as session:
               sttm = select().add_columns(Tables.name).where(Tables.id == id)
               
               response = await session.execute(sttm)
               return response.scalar()
          
          
     @classmethod
     async def insert_data_tables(cls, id: int, name: str, pass_: str) -> None:
          async with cls._sessions.begin() as session:
               sttm = (
                    insert(Tables).
                    values(id = id, name = name, password = pass_)
               )
               await session.execute(sttm)
               
               
     @classmethod
     async def update_data_tables(cls, id: int, new_name: str, pass_: str) -> bool:
          async with cls._sessions.begin() as session:
               sttm_password = select().add_columns(Tables.password).where(Tables.id == id)
               check_password = await session.execute(sttm_password)
               
               if pass_ == check_password.scalar():
                    sttm = (
                         update(Tables).
                         where(Tables.id == id).
                         values(name = new_name)
                    )
                    await session.execute(sttm)
                    
                    return True
               return False
          
          
          
data_command = DataCommands()
          
               
          
     