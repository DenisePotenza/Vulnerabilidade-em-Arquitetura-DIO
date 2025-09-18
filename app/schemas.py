from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    extracted_text: str
    analysis: dict
