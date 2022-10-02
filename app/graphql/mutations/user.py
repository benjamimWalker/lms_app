from graphene import Mutation, String, Field, Int, Boolean, InputObjectType
from app.controllers.user_controller import UserController
from app.controllers.validators.user_validator import UserValidator
from app.graphql.types.types import UserType


class CreateUserInput(InputObjectType):
    email = String()
    role = Int()
    is_active = Boolean()
    id = Int()


class CreateUser(Mutation):
    user = Field(UserType)

    class Arguments:
        user_input = CreateUserInput()

    def mutate(root, info, user_input: CreateUserInput) -> 'CreateUser':
        valid_user_input = UserValidator(
            email=user_input.email,
            role=user_input.role,
            is_active=user_input.is_active,
            id=user_input.id
        )

        create_user = UserController().create_user(valid_user_input)

        return CreateUser(user=create_user)