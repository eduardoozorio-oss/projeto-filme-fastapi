from fastapi import FastAPI

import funcao


#rodar o fastapi:
#python -m uvicorn api:app --reload

#testar api fastAPI
# /dcs > documentação Swagger
# /redoc > documentacao redoc

#inicial o fastapi
app = FastAPI(title="gerenciador de filmes")
''

@app.get("/")
def home():
    return {"mensagem": "bem-vindo ao gerenciador de filmes"}


@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "filme adicionando com sucesso!"}


@app.get("/filmes")
def exibir_filmes():
    filmes = funcao.lista_filme()
    lista = []
    for linha in filmes:
        lista.append({
            "id": linha [0], 
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliacao":[4]
            })
    return {"filmes": lista}