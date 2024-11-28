from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Базовая схема для возврата успешного ответа
    """

    result: bool = True
    model_config = ConfigDict(from_attributes=True)
