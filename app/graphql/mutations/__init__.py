from graphene import ObjectType
from app.graphql.mutations.user import CreateUser, UpdateUser


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
