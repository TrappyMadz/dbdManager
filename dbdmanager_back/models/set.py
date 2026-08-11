from models.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.dialects.postgresql import ARRAY

class Set(Base):
    __tablename__ = "sets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    role = Column(String, index=True)
    character = Column(String, index=True)
    perks = Column(ARRAY(String))
    addons = Column(ARRAY(String))
    likes_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(ForeignKey("users.id"), nullable=False)