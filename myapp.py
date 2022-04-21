"""Modulo uvicorn."""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def say_hi():
    """retornando un saludo."""
    return 'Hola soy Alexis'

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
