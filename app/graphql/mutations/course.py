from graphene import Mutation, Field, Int, String, InputObjectType
from app.controllers.course_controller import CourseController
from app.controllers.validators.course_validator import CourseValidator
from app.graphql.types.types import CourseType


class UpdateCourseInput(InputObjectType):
    id = Int()
    creator_id = Int()
    title = String()
    description = String()


class CreateCourseInput(InputObjectType):
    id = Int(required=False, default=None)
    creator_id = Int()
    title = String()
    description = String()


class CreateCourse(Mutation):
    course = Field(CourseType)

    class Arguments:
        course_input = CreateCourseInput()

    def mutate(root, info, course_input: CreateCourseInput) -> 'CreateCourse':
        valid_course_input = CourseValidator(
            creator_id=course_input.creator_id,
            title=course_input.title,
            description=course_input.description
        )

        if course_input.id is not None:
            valid_course_input.id = course_input.id

        return CreateCourse(CourseController().create_course(valid_course_input))


class UpdateCourse(Mutation):
    course = Field(CourseType)

    class Arguments:
        course_input = UpdateCourseInput()

    def mutate(_, __, course_input: UpdateCourseInput) -> 'UpdateCourse':
        return UpdateCourse(
            CourseController().update_course(
                CourseValidator(
                    id=course_input.id,
                    title=course_input.title,
                    creator_id=course_input.creator_id,
                    description=course_input.description,
                )
            )
        )