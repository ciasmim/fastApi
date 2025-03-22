from fastapi import FastAPI
from app.api.v1.hand_detection import router as hand_detection_router

app = FastAPI()

# Incluindo as rotas de detecção de mão
app.include_router(hand_detection_router, prefix="/api/v1/hand_detection", tags=["Hand Detection"])

