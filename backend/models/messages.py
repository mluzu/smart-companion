from typing import List
from pydantic import BaseModel
from datetime import datetime

from backend.models.analysis import AnalysisResult

class Message(BaseModel):
    message_id: str
    user_id: str
    timestamp: datetime
    sentiment: str
    emotion: str
    source: str

class TextMessage(Message):
    text: str
   

class AudioMessage(Message):
    audio_file_id: str
    file_path: str
    uploaded_at: datetime
    duration: float
    transcription_id: str = None


class Transcript(BaseModel):
    transcript_id: str
    audio_file_id: str
    content: str
    duration: float
    timestamp: datetime


class ChatHistory(BaseModel):
    session_id: str
    messages: List[Message]
    transcripts: List[Transcript]
    analysis_results: List[AnalysisResult]