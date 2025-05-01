from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from ytlp.models.base import Base


class Subtitle(Base):
    __tablename__ = "subtitles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)  # 外键
    video_name = Column(String, nullable=False)
    start_time = Column(Float, nullable=False)
    end_time = Column(Float, nullable=False)
    content = Column(Text, nullable=False)
    language = Column(String, default="en")

    # 正确写法，指向类名 Video
    video = relationship("Video", back_populates="subtitles")

    def __repr__(self):
        return f"<Subtitle(video_id={self.video_id}, start={self.start_time}, end={self.end_time}, content={self.content[:20]}...)>"
