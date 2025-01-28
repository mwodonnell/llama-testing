from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def generate():
    return {"response": "hello world"}
