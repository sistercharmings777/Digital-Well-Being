from pydantic import BaseModel
from typing import List


class DiseaseInfectionCreate(BaseModel):
    name: str
    type: str | None = None
    description: str
    causes: str | None = None
    # image: str | None = None
    prevention: str | None = None
    prone_areas: List[str] | None = None



