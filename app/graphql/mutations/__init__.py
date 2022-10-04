from graphene import ObjectType
from app.graphql.mutations.course import CreateCourse, UpdateCourse
from app.graphql.mutations.user import CreateUser, UpdateUser


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    create_course = CreateCourse.Field()
    update_course = UpdateCourse.Field()
