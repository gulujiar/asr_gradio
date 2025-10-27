# ASR Tools - 基于Gradio的语音识别工具

🎤 基于必剪ASR接口的智能语音识别工具，使用Gradio构建用户友好的Web界面。

## ✨ 特色功能

- 🚀 **无需复杂配置**: 无需GPU和繁琐的本地配置
- 🖥️ **高颜值界面**: 基于Gradio构建，界面美观且用户友好
- ⚡ **效率超人**: 支持批量处理，文字转换快如闪电
- 📄 **多格式支持**: 支持生成SRT、TXT、ASS字幕文件
- 🎥 **视频直接处理**: 支持输入视频文件自动处理

## 🛠️ 安装指南

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动应用

```bash
python asr_gradio.py
```

应用将在 http://localhost:7860 启动

## 🖥️ 快速上手

1. **启动应用**: 运行 `python asr_gradio.py`
2. **选择文件**: 点击"选择音频/视频文件"按钮上传文件
3. **选择输出格式**: 在下拉菜单中选择SRT、TXT或ASS格式
4. **开始处理**: 点击"开始处理"按钮
5. **获取结果**: 处理完成后，字幕文件将保存在原文件同目录下

## 📄 支持格式

### 输入格式
- **音频**: MP3, WAV, M4A, FLAC, AAC
- **视频**: MP4, AVI, MOV, MKV

### 输出格式
- **SRT**: 标准字幕格式，包含时间轴信息
- **TXT**: 纯文本格式，只包含识别文字
- **ASS**: 高级字幕格式，支持样式和特效

## 🎯 使用示例

```python
# 命令行使用示例
python asr_gradio.py

# 然后在浏览器中访问 http://localhost:7860
# 上传文件并选择输出格式即可
```

## 📁 项目结构

```
srtars/
├── asr_gradio.py      # Gradio主界面
├── BcutASR.py         # 必剪ASR接口实现
├── BaseASR.py         # ASR基类
├── ASRData.py         # 数据模型
├── requirements.txt   # 依赖文件
└── README.md          # 说明文档
```

## ⚠️ 注意事项

- 文件大小限制：单个文件建议不超过100MB
- 处理时间：根据文件大小和网络状况而定
- 输出文件：保存在原文件同目录下

## 📬 联系与支持

如有问题或建议，请提交Issue。

---

感谢您使用 ASR Tools！🎉