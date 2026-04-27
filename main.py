from fastapi import FastAPI

app = FastAPI()

def soma(a, b):
    return a + b

@app.get("/funcionamentoSoma")
async def funcionamento_soma(a: int, b: int):
    resultado = soma(a, b)
    return {
        "a": a,
        "b": b,
        "resultadoss": resultados
    }