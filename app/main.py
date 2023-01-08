from fastapi import FastAPI, Request
import uvicorn


app = FastAPI()

# @app.on_event("startup")
# def startup_db_client():
#     app.mongodb_client = MongoClient(config["ATLAS_URI"])
#     app.database = app.mongodb_client[config["DB_NAME"]]
#
# @app.on_event("shutdown")
# def shutdown_db_client():
#     app.mongodb_client.close()
#
# app.include_router(book_router, tags=["books"], prefix="/book")



#------------------------------
# endpoints
@app.get("/")
def root(request:Request):
    return {"message": "hello"}







if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
