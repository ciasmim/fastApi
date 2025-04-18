## Descrição

Este projeto é uma API baseada em **FastAPI** que utiliza **TensorFlow**, **Keras**, para detectar e interpretar gestos das mãos. Esta aplicação está sendo desenvolvida para ser usada como backend de um aplicativo móvel, onde a captura de imagem da mão do usuário é realizada no lado cliente, e os pontos de referência (landmarks) ou gestos são enviados para a API para interpretação.

A API retorna uma resposta baseada no gesto da mão detectado para traduzir um gesto de libras para texto PT/BR.

## Funcionalidades

- **Captura de Imagem da Mão**
- **Interpretação de Gesto**
- **Retorno de Resposta**

## Pré-requisitos

1. **Python 3.9+**
2. **Dependências do Projeto**: As dependências estão listadas no arquivo `requirements.txt`. Você pode instalar todas as bibliotecas necessárias com o seguinte comando:  
        pip install -r requirements.txt

## Executando o projeto
 1. execute o comando uvicorn app.main:app --reload
 2. Documentação Swagger: http://127.0.0.1:8000/docs
 


## Modelo pronto utilizado
https://www.kaggle.com/models/sayannath235/american-sign-language