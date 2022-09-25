from pydantic import BaseModel, EmailStr, validator


class UserValidator(BaseModel):
    email: EmailStr
    role: int
    is_active: bool
    id: int | None

    @validator('role')
    def validate_role(cls, value: int) -> int | None:
        if value not in (1, 2):
            raise Exception('role must be either 1 or 2')

        return value

    @validator('id')
    def validate_id(cls, value: int) -> int | None:
        if value is None or value <= 0:
            raise Exception('id must be greater than 0')

        return value

    class Config:
        orm_mode = True
