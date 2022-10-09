from pydantic import BaseModel, Field

class PoloSchema(BaseModel):
    ad_link: str = Field(...)
    asking_price: str = Field(...)
    model_year: str = Field(...)
    kms_driven: str = Field(...)
    ad_title: str = Field(...)
    ad_location: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "ad_link": "https://www.olx.in/item/volkswagen-polo-gt-tsi-2014-petrol-iid-1689682101",
                "asking_price": "₹ 5,45,000",
                "model_year": "2017",
                "kms_driven": "50,000 km",
                "ad_title": "Volkswagen Polo GT TSI, 2014, Petrol",
                "ad_location": "Ottapalam"
            }
        }
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}