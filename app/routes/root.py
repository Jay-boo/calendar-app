from fastapi import APIRouter,Request




router=APIRouter()
@router.get("/")
def root(request:Request):
    return {"message": "hello"}
