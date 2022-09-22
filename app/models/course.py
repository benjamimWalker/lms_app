import enum
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from db.database import Base
from .user import User, course_student
from .mixins import Timestamp


class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3


class Course(Timestamp, Base):
    __tablename__ = 'courses'

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, nullable=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_by = relationship(User)
    sections = relationship('Section', back_populates='course', uselist=False)
    students = relationship(User, secondary=course_student, back_populates='courses')


class Section(Timestamp, Base):
    __tablename__ = 'sections'

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, nullable=True)
    course_id: int = Column(Integer, ForeignKey('courses.id'), nullable=False)
    course = relationship('Course', back_populates='sections')
    content_blocks = relationship('ContentBlock', back_populates='section')


class ContentBlock(Timestamp, Base):
    __tablename__ = 'content_blocks'

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, nullable=True)
    type: enum = Column(Enum(ContentType))
    url = Column(URLType, nullable=True)
    content: str = Column(Text, nullable=True)
    section_id: int = Column(Integer, ForeignKey('sections.id'), nullable=False)
    section = relationship('Section', back_populates='content_blocks')
