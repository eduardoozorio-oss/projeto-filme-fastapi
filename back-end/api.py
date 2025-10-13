from fastapi import FastAPI

import funcao


#rodar o fastapi:
#python -m uvicorn api:app --reload

#testar api fastAPI
# /dcs > documentação Swagger
# /redoc > documentacao redoc

#inicial o fastapi
app = FastAPI(title="gerenciador de filmes")


@app.get("/")
def home():
    return {"mensagem": "quero café prof"}


@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "filme adicionando com sucesso!"}