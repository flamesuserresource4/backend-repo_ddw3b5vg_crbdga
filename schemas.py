"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (you can keep these for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# NCUK Partner Lead schema (B2B Study Centre leads)
class PartnerLead(BaseModel):
    """
    Partner leads from potential study centres interested in delivering NCUK programmes.
    Collection name: "partnerlead"
    """
    centre_name: str = Field(..., description="Institution or study centre name")
    contact_name: str = Field(..., description="Primary contact person")
    email: EmailStr = Field(..., description="Contact email")
    phone: Optional[str] = Field(None, description="Contact phone number")
    country: Optional[str] = Field(None, description="Country of the institution")
    city: Optional[str] = Field(None, description="City of the institution")
    website: Optional[str] = Field(None, description="Institution website")
    interest_level: Optional[str] = Field(
        None, description="Stage of interest e.g., exploring, ready_to_apply, meeting_requested"
    )
    notes: Optional[str] = Field(None, description="Additional context or requirements")
    marketing_consent: bool = Field(False, description="Consent to receive marketing communications")
    source: Optional[str] = Field(None, description="Lead source e.g., website, referral, event")
    utm_source: Optional[str] = Field(None)
    utm_medium: Optional[str] = Field(None)
    utm_campaign: Optional[str] = Field(None)
