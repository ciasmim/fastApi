# Lógica de detecção de mão
from fastapi import APIRouter, File, UploadFile
from app.services.hand_service import predict_hand_sign
from app.models.hand_model import PredictionResponse

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_hand_sign_endpoint(image: UploadFile = File(...)):
    """
    Recebe uma imagem e retorna a previsão do sinal de mão detectado.
    """
    # Lê os dados da imagem recebida
    image_data = await image.read()
    
    # Chama o serviço para fazer a detecção e previsão
    prediction = predict_hand_sign(image_data)
    
    return prediction
