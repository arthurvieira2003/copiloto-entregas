from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Tuple
from services.entrega_service import processar_entregas

app = FastAPI(title="API de Processamento de Entregas", description="API para processar entregas e calcular o melhor lucro")

class Conexao(BaseModel):
    origem: str
    destino: str
    tempo: int

class Entrega(BaseModel):
    tempo_inicio: int
    destino: str
    bonus: int

class EntregaRequest(BaseModel):
    conexoes: List[Tuple[str, str, int]]
    entregas: List[Tuple[int, str, int]]

class EntregaResponse(BaseModel):
    entregas_realizadas: List[Tuple[int, str, int]]
    lucro_total: float

@app.post("/processar_entregas", response_model=EntregaResponse)
async def processar_entregas_route(request: EntregaRequest):
    try:
        resultado = processar_entregas(request.conexoes, request.entregas)
        return EntregaResponse(**resultado)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)