from graphene import ObjectType, List, Field, Argument, Int
from app.controllers.user_controller import UserController
from app.graphql.types.types import UserType


class User(ObjectType):
    item = Field(UserType,
                 user_id=Int()
                 )

    all = List(UserType,
               page=Int(),
               per_page=Int()
               )

    def resolve_item(_, __, user_id: int):
        return UserController().get_user_by_id(user_id)

    def resolve_all(_, __, page: int, per_page: int):
        return UserController().get_all_users(page=page, per_page=per_page)
