from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.course.basic import Course
from app.models.user.basic import User


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
