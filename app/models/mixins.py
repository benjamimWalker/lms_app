from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    created_at: datetime = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow(), nullable=False)
