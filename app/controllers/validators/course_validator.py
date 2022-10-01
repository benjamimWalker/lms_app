from pydantic import BaseModel, validator


class CourseValidator(BaseModel):
    id: int | None
    creator_id: int
    title: str
    description: str

    @validator('id')
    def validate_id(cls, value: int) -> int | None:
        if value is None or value <= 0:
            raise Exception('Invalid id')

        return value

    @validator('creator_id')
    def validate_creator_id(cls, value: int) -> int | None:
        if value is None or value <= 0:
            raise Exception('Invalid creator id')

        return value

    @validator('title')
    def validate_title(cls, value: str) -> str | None:
        if value is None or 3 >= len(value) >= 50:
            raise Exception('Invalid title')

        return value

    @validator('description')
    def validate_description(cls, value):
        if value is None or 6 >= len(value) >= 250:
            raise Exception('Invalid title')

        return value
