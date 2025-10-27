import os
import logging
from abc import ABC, abstractmethod
from typing import Union, Optional
from pathlib import Path

from ASRData import ASRData, ASRDataSeg


class BaseASR(ABC):
    """ASR基类"""
    
    def __init__(self, audio_path: Union[str, bytes], use_cache: bool = False):
        self.audio_path = audio_path
        self.use_cache = use_cache
        self.file_binary = None
        
        # 加载音频数据
        if isinstance(audio_path, str):
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"音频文件不存在: {audio_path}")
            
            with open(audio_path, 'rb') as f:
                self.file_binary = f.read()
        elif isinstance(audio_path, bytes):
            self.file_binary = audio_path
        else:
            raise ValueError("audio_path必须是文件路径或字节数据")
    
    def run(self) -> ASRData:
        """运行ASR处理"""
        try:
            logging.info("开始ASR处理...")
            
            # 执行具体实现
            result_data = self._run()
            
            # 转换为ASRData格式
            if isinstance(result_data, dict):
                asr_data = self._make_segments(result_data)
            elif isinstance(result_data, ASRData):
                asr_data = result_data
            else:
                raise ValueError(f"不支持的返回类型: {type(result_data)}")
            
            logging.info(f"ASR处理完成，共识别{len(asr_data.segments)}个片段")
            return asr_data
            
        except Exception as e:
            logging.error(f"ASR处理失败: {str(e)}")
            raise
    
    @abstractmethod
    def _run(self):
        """具体实现方法"""
        pass
    
    @abstractmethod
    def _make_segments(self, resp_data: dict) -> ASRData:
        """将API响应转换为ASRData"""
        pass
    
    def _check_file_size(self, max_size_mb: int = 100) -> bool:
        """检查文件大小"""
        if isinstance(self.audio_path, str):
            file_size = os.path.getsize(self.audio_path) / (1024 * 1024)  # MB
            if file_size > max_size_mb:
                logging.warning(f"文件大小({file_size:.2f}MB)超过建议限制({max_size_mb}MB)")
                return False
        return True
    
    def _get_file_info(self) -> dict:
        """获取文件信息"""
        if isinstance(self.audio_path, str):
            path = Path(self.audio_path)
            return {
                'name': path.name,
                'size': len(self.file_binary),
                'extension': path.suffix.lower()
            }
        else:
            return {
                'name': 'audio_data',
                'size': len(self.file_binary),
                'extension': '.mp3'
            }