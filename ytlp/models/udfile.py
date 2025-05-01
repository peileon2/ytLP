from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

## 用于保存，字幕文件夹和视频文件夹地址
Base = declarative_base()


class Foldsrecord(Base):
    __tablename__ = "Foldsrecord"

    id = Column(Integer, primary_key=True)
    video_path = Column(String)
    subtitle_path = Column(String)
