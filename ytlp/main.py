from ytlp.core.db import engine
from ytlp.models.base import Base
from ytlp.models.subtitle import Subtitle
from ytlp.models.vedio import Video
from ytlp.models.udfile import Foldsrecord
from sqlalchemy.orm import sessionmaker


# 创建表（仅当不存在时）
Base.metadata.create_all(bind=engine)

# 创建 session 工厂
Session = sessionmaker(bind=engine)

# 使用上下文管理（推荐做法，自动关闭）
with Session() as session:
    # Add subtitle data with correct video_id (must be an integer that exists in the Video table)
    subtitle = Subtitle(
        video_id=1,  # Replace this with the actual video ID from your database
        video_name="Example Video",
        start_time=12.5,
        end_time=15.7,
        content="Hello, how are you?",
        language="en",
    )

# 查询字幕
subtitles = session.query(Subtitle).filter_by(video_id="abc123").all()
for s in subtitles:
    print(s)


def main():
    print("Hello from main!")
