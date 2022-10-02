from graphene import ObjectType, Field, Schema
from app.graphql.queries.user import User
from app.graphql.queries.course import Course


class Query(ObjectType):
    User = Field(User, resolver=lambda _, __: User)
    Course = Field(Course, resolver=lambda _, __: Course)
