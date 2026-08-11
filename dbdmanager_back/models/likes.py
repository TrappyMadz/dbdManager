from models.base import Base
from sqlalchemy import Column, ForeignKey

class Like(Base):
    __tablename__ = "likes"

    liked_by = Column(ForeignKey("users.id"), nullable=False, primary_key=True)
    set_id = Column(ForeignKey("sets.id"), nullable=False, primary_key=True)