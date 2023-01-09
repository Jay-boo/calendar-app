from click.utils import text_streams
import uvicorn
from fastapi import FastAPI
from database import Database
from routes import root
from crud import get_events


db=Database()
test_GET_event=get_events(db)
app = FastAPI()

app.include_router(root.router)












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










if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
