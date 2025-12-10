from pydantic import BaseModel

class AuraResponse(BaseModel):
    aura_number: str
