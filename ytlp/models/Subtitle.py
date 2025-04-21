from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Subtitle(Base):
    __tablename__ = "subtitles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String, nullable=False)  # 视频标识
    start_time = Column(Float, nullable=False)  # 起始时间（单位：秒）
    end_time = Column(Float, nullable=False)  # 结束时间（单位：秒）
    content = Column(Text, nullable=False)  # 字幕内容
    language = Column(String, default="en")  # 字幕语言，例如 "en", "zh"

    def __repr__(self):
        return f"<Subtitle(video_id={self.video_id}, start={self.start_time}, end={self.end_time}, content={self.content[:20]}...)>"
