from pydantic import BaseModel
class validation(BaseModel):
    variance : float
    skewness : float	
    curtosis : float	
    entropy : float