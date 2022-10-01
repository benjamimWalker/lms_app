from app.controllers.base_controller import BaseController
from app.models.user.basic import User
from .validators.user_validator import UserValidator
from sqlalchemy.orm import selectinload


class UserController(BaseController):

    def get_all_users(self, page: int, per_page: int) -> list[User]:
        if page <= 0 or per_page <= 0:
            raise Exception('Invalid pagination parameters')

        return self.session.query(User).limit(per_page). \
            offset(page - 1). \
            all()

    def get_user_by_id(self, user_id: int):
        if user := self.session.query(User).get(user_id):
            return user

        raise Exception('User Not Found')

    def create_user(self, user_data: UserValidator) -> User:
        user = User(
            is_active=user_data.is_active,
            email=user_data.email,
            role=user_data.role
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def update_user(self, user_data: UserValidator) -> User:
        if user := self.session.get(User, user_data.id):
            user.is_active = user_data.is_active
            user.email = user_data.email
            user.role = user_data.role

            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)

            return user

        raise Exception('User not found')
