import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

# Caminho para o modelo
model_path = r'C:\Users\ciasm\Documents\modelo_rede_neural'

# Tente carregar o modelo SavedModel
try:
    model = tf.saved_model.load(model_path)
    
    # Verifique as assinaturas disponíveis no modelo
    print("Assinaturas disponíveis:", model.signatures.keys())
    
    # Assinatura padrão que o modelo usa (ajuste se necessário)
    infer = model.signatures["serving_default"]
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    raise

def predict_hand_sign(image_data: bytes):
    """
    Processa a imagem recebida, faz a inferência e retorna a previsão.
    """
    try:
        image = Image.open(BytesIO(image_data))  # Converte os dados em uma imagem
        image = image.resize((224, 224))  # Ajuste do tamanho conforme o modelo
        image = np.array(image) / 255.0  # Normalização da imagem
        image = np.expand_dims(image, axis=0)  # Adiciona a dimensão do batch

        # Realiza a inferência
        prediction = infer(tf.convert_to_tensor(image, dtype=tf.float32))

        # Extrai a saída do modelo (tente entender o nome da camada de saída)
        output_key = list(prediction.keys())[0]  # Primeiro item na previsão (normalmente único)
        output_data = prediction[output_key]    # A saída real da camada

        # Obtém a classe com maior probabilidade
        predicted_class = np.argmax(output_data.numpy())  # Índice da classe com maior probabilidade

        # Definir as classes de sinais de mão (ajuste conforme necessário)
        hand_signs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # Retorna o resultado da previsão
        return {"label": hand_signs[predicted_class], "confidence": float(output_data[0][predicted_class])}
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        raise
