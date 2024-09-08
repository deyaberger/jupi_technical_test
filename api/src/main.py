"""FastAPI application that provides an endpoint to get autocomplete suggestions using an LLM model."""
from fastapi import FastAPI

from src.autocomplete import MySuperCoolLLM

app = FastAPI()

autocomplete_agent = MySuperCoolLLM()

@app.get("/suggestions/")
async def get_suggestions(query: str):
    """Endpoint to get suggestions based on user query."""
    suggestions = autocomplete_agent.get_suggestions(query)
    return {"suggestions": suggestions}
