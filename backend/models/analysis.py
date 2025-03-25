from pydantic import BaseModel

class AnalysisResult(BaseModel):
    analysis_id: str
    message_id: str
    sentiment: str
    emotion: str
    confidence: float
    details: dict