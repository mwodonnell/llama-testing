import uvicorn
from fastapi import FastAPI
from core.api import router as core_router
from llama.api import router as llama_router

# probably load the model here

app = FastAPI()

routes = [
    {
        "path": "",
        "router": core_router,
    },
    {
        "path": "/llama",
        "router": llama_router,
    },
]

for route in routes:
    app.include_router(route["router"], prefix=route['path'])


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
