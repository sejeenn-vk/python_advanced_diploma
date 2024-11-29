from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    result: bool = True
    model_config = ConfigDict(from_attributes=True)
