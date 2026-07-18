from pydantic import BaseModel
from .enums import Environment
class Settings(BaseModel):
    environment: Environment = Environment.DEV
    catalog: str = 'agri'
    schema: str = 'bronze'
