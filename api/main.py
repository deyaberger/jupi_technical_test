from fastapi import FastAPI
from autocomplete import MySuperCoolLLM

app = FastAPI()

autocomplete_agent = MySuperCoolLLM()

@app.get("/suggestions/")
async def get_suggestions(query: str):
    suggestions = autocomplete_agent.get_suggestions(query)
    return {"suggestions": suggestions}
