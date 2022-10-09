from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import retrieve_ad_listings
from server.models.polo import (
    ErrorResponseModel,
    ResponseModel,
    PoloSchema
)

router = APIRouter()

@router.get("/", response_description="Polo Listings retrieved")
async def get_listings():
    listings = await retrieve_ad_listings()
    if listings:
        return ResponseModel(listings, "Listings successfully retrieved")
    return ResponseModel(listings, "Empty List Returned")