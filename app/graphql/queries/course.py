from graphene import ObjectType, Field, Int, List

from app.controllers.course_controller import CourseController
from app.graphql.types.types import CourseType


class Course(ObjectType):
    item = Field(CourseType, course_id=Int())
    all = List(CourseType, page=Int(), per_page=Int())

    def resolve_all(_, __, page: int, per_page: int):
        return CourseController().get_all_courses(page, per_page)

    def resolve_item(_, __, course_id: int):
        return CourseController().get_course(course_id)
