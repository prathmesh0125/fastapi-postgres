import datetime as _dt
import pydantic as _pydantic

class _BaseContact(_pydantic.BaseModel):
  first_name:str
  last_name:str
  email:str
  Phone_number:str
  
class Contact(_BaseContact):
  id:int
  date_created:_dt.datetime  
  
  class Config:
    orm_mode:True
    from_attributes = True 
  
class CreateContact(_BaseContact):
  pass