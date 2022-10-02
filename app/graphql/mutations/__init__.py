from graphene import ObjectType
from app.graphql.mutations.user import CreateUser


class Mutation(ObjectType):
    create_user = CreateUser.Field()
