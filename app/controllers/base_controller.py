from sqlalchemy.orm import Session
from app.db.database import get_session


class BaseController:
    def __init__(self, session: Session = next(get_session())):
        self.session = session
