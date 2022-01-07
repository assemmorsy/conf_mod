from fastapi import  FastAPI

from routes import speaker_route ,conf_router

from depen import models

from depen import database
import os
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

engine=database.engine

models.Base.metadata.create_all(bind=engine)

directory = "file_tree"
parent_dir = "."
path = os.path.join(parent_dir, directory)
#"C:/AoConferance/file_tree"
if(not (os.path.exists(path))):
  os.mkdir(path)

  

middleware = [Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])]



app = FastAPI(middleware=middleware)



#app.include_router(speaker_route.router)
app.include_router(conf_router.router)







