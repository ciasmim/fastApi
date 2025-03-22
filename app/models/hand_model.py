 # Modelos Pydantic para requests e responses
from pydantic import BaseModel

class PredictionResponse(BaseModel):
    label: str      # A classe do sinal de mão previsto
    confidence: float  # A confiança (probabilidade) da previsão
