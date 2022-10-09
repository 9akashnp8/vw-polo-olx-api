from fastapi import FastAPI
from server.routes.polo import router as PoloAPIRouter

app = FastAPI()

app.include_router(PoloAPIRouter, tags=["polo"], prefix="/polo")

@app.get("/", tags=["home"])
def read_root():
    return {'message':'Welcome to this app'}

# Get OLX Listings

# Get OLX Listing by ID
