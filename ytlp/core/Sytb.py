import whisper
import os

# ffmpeg 所在目录
ffmpeg_dir = r"ffmpeg-2025-04-14-git-3b2a9410ef-essentials_build\bin"
os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]
print(os.environ["PATH"])
# 加载 Whisper 模型
model = whisper.load_model("base")

# 转录音频文件（路径需确认）
result = model.transcribe(r"Best tips for cooking on a gas BBQ [mNsyK7oWPzA].mp3")

# 打印转录结果
print(result["text"])
