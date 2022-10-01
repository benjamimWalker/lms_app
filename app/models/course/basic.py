import enum
from sqlalchemy import Enum, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType
from app.db.database import Base
from app.models.mixins import Timestamp
from app.models.user.basic import User


class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3


class Course(Timestamp, Base):
    __tablename__ = 'course'

    id: int = Column(Integer, primary_key=True, index=True)

    creator_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    creator = relationship(User)

    title: str = Column(String(200), nullable=False)

    description: str = Column(Text, nullable=True)

    sections = relationship('Section', back_populates='course', uselist=False)
    students = relationship(User, secondary='course_student', back_populates='courses')


class Section(Timestamp, Base):
    __tablename__ = 'sections'

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    description: str = Column(Text, nullable=True)
    course_id: int = Column(Integer, ForeignKey('course.id'), nullable=False)
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
