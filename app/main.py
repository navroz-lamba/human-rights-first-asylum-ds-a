"""This is where we bring all the modular components together."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
#from app.database import engine

# to create our models in the databse
#models.Base.metadata.create_all(bind=engine)
from . import models, schemas, routes, database

# to create our models in the databse

description = """
**Human Rights First Asylum**

To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

app = FastAPI(
    title = "Human Rights First Asylum API",
    description = description,
    docs_url='/',
)

app.include_router(routes.router)
app.include_router(database.routerdb)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == "__main__":
    uvicorn.run(app)