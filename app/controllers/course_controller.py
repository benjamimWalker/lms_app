from sqlalchemy.orm import selectinload
from app.controllers.base_controller import BaseController
from app.controllers.validators.course_validator import CourseValidator
from app.models.course.basic import Course


class CourseController(BaseController):
    def get_all_courses(self, page: int, per_page: int) -> list[Course]:
        if page <= 0 or per_page <= 0:
            raise Exception('Invalid pagination parameters')

        return self.session.query(Course).options(
            selectinload(Course.students)
        ).offset(page - 1) \
            .limit(per_page) \
            .all()

    def get_course(self, course_id: int) -> Course:
        if course := self.session.query(Course) \
                .options(selectinload(Course.students)) \
                .get(course_id):
            return course

        else:
            raise Exception('Course not found')

    def create_course(self, course_data: CourseValidator) -> Course:
        course = Course(
            creator_id=course_data.creator_id,
            title=course_data.title,
            description=course_data.description
        )

        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)

        return course

    def update_course(self, course_data: CourseValidator) -> Course:
        if course := self.session.query(Course).get(course_data.id):
            course.title = course_data.title
            course.description = course_data.description
            course.creator_id = course_data.creator_id

        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)

        return course
