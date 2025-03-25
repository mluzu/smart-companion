from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_id: str
    username: str
    created_at: datetime
    last_active: datetime


class VoiceProfile(BaseModel):
    profile_id: str
    user_id: str
    voice_embedding: list  # Feature vector from voice
    created_at: datetime
    updated_at: datetime
    

class Session(BaseModel):
    session_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    status: str