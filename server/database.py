from decouple import config
import motor.motor_asyncio

MONGO_URL = config("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.polo_api_db

polo_collection = database.get_collection("polo_api_collection")

# Helpers
def polo_helper(polo) -> dict:
    return {
        "id": str(polo["_id"]),
        "ad_link": polo["ad_link"],
        "asking_price": polo["asking_price"],
        "model_year": polo["model_year"],
        "kms_driven": polo["kms_driven"],
        "ad_title": polo["ad_title"],
        "ad_location": polo["ad_location"]
    }

async def retrieve_ad_listings():
    ad_listings = []
    async for listing in polo_collection.find():
        ad_listings.append(polo_helper(listing))
    return ad_listings