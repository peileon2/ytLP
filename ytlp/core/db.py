from sqlalchemy import create_engine

# 连接到本地文件数据库（如果文件不存在会自动创建）
engine = create_engine("sqlite:///example.db", echo=True)  # echo=True 会输出 SQL 日志
