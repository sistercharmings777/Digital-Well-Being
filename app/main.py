from enum import Enum
import random

from fastapi import FastAPI

from app.dbase import list_of_terms, infections, general_infections
from schemas.healthy_schema import DiseaseInfectionCreate


class TermClarification(str, Enum):
    diseases = "Disease"
    illness = "Illness"
    sti = "STIs"
    health = "Health"
    drugs = "Drugs"


app = FastAPI()


@app.get("/")
async def index():
    """ Healthy Living"""
    return {"message": "Welcome to Well-Being"}


@app.get("/general")
async def general(limit: int = 20):
    """ Returns Unfiltered and Uncategorized Information """
    return {"message": general_infections}


@app.get('/term_clarification/{term}')
async def term_clarification(term: TermClarification):
    """ Educates confusing terms found in health based on predefined values"""
    if term is TermClarification.diseases:
        print(term)
        return {"term": term, "message": list_of_terms[0][term]}
    elif term is TermClarification.illness:
        return {"term": term, "message": list_of_terms[1][term]}
    elif term is TermClarification.sti:
        return {"term": term, "message": list_of_terms[2][term]}
    elif term is TermClarification.health:
        return {"term": term, "message": list_of_terms[3][term]}
    elif term is TermClarification.drugs:
        return {"term": term, "message": list_of_terms[4][term]}


@app.get('/random_health_tip')
async def random_health_tip():
    """ Randomly educates end-user with health tips"""
    selected_tip = random.choice(general_infections)
    return selected_tip


@app.post('/add_health_tip')
async def add_tip_data(data: DiseaseInfectionCreate):
    """ Endpoint to populate the DB with information """
    new_tip = data.dict()
    general_infections.append(new_tip)
    return {"message": new_tip}


@app.put('/tip_update/{tip_id}')
async def update_tip_data(tip_id: int, data: DiseaseInfectionCreate):
    """ Endpoint to Update a tip in the DB"""
    if tip_id <= len(infections):
        tip_to_update = general_infections[tip_id]
        tip_to_update.update(data.dict())
        return tip_to_update
    else:
        print(f"Tip with the id of {tip_id} not found")
    return "Update Successfully"
