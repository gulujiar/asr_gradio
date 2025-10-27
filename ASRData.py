from dataclasses import dataclass
from typing import List


@dataclass
class ASRDataSeg:
    """ASR数据片段"""
    text: str
    start: float
    end: float


class ASRData:
    """ASR数据类"""
    
    def __init__(self, segments: List[ASRDataSeg] = None):
        self.segments = segments or []
    
    def __iter__(self):
        return iter(self.segments)
    
    def __len__(self):
        return len(self.segments)
    
    def __getitem__(self, index):
        return self.segments[index]
    
    def add_segment(self, text: str, start: float, end: float):
        """添加片段"""
        self.segments.append(ASRDataSeg(text, start, end))
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            'segments': [
                {
                    'text': seg.text,
                    'start': seg.start,
                    'end': seg.end
                }
                for seg in self.segments
            ]
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ASRData':
        """从字典创建"""
        segments = [
            ASRDataSeg(
                text=seg['text'],
                start=seg['start'],
                end=seg['end']
            )
            for seg in data.get('segments', [])
        ]
        return cls(segments)