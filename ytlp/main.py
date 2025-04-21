from ytlp.core.db import engine
from ytlp.models.Subtitle import Base, Subtitle
from sqlalchemy.orm import sessionmaker

# 创建表（仅当不存在时）
Base.metadata.create_all(bind=engine)

# 创建 session 工厂
Session = sessionmaker(bind=engine)

# 使用上下文管理（推荐做法，自动关闭）
with Session() as session:
    # 添加字幕数据
    subtitle = Subtitle(
        video_id="abc123",
        start_time=12.5,
        end_time=15.7,
        content="Hello, how are you?",
        language="en",
    )
    session.add(subtitle)
    session.commit()

# 查询字幕
subtitles = session.query(Subtitle).filter_by(video_id="abc123").all()
for s in subtitles:
    print(s)
