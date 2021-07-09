from pydantic import BaseModel, ConfigDict

__all__ = ['Command']


class Command(BaseModel):
    model_config = ConfigDict(frozen=True)
