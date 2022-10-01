from graphene import ObjectType, Field, Schema
from app.graphql.queries.user import User


class Query(ObjectType):
    User = Field(User, resolver=lambda _, __: User)
