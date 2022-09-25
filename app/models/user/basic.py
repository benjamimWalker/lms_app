import enum
from app.db.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Table
from sqlalchemy.orm import relationship


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    role: enum = Column(Enum(Role))
    is_active: bool = Column(Boolean)
    profile = relationship('Profile', back_populates='user', uselist=False)
    courses = relationship('Course', secondary='course_student', back_populates='students')


class Profile(Base):
    __tablename__ = 'profiles'

    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String)
    last_name: str = Column(String)
    bio: str = Column(Text)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='profile')


course_student = Table(
    'course_student',
    Base.metadata,
    Column('student_id', ForeignKey('users.id'), primary_key=True),
    Column('course_id', ForeignKey('course.id'), primary_key=True)
)
