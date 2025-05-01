from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ytlp.models.base import Base


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    vedio_file = Column(String)
    subtitle_file = Column(String)

    # 正确写法，指向类名 Subtitle
    subtitles = relationship("Subtitle", back_populates="video")
