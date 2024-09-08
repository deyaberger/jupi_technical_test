from fastapi import FastAPI
import random
import string
import time

app = FastAPI()

@app.get("/suggestions/")
async def get_suggestions(query: str):
    suggestions = []
    for _ in range(5):
        time.sleep(random.randint(0, 5))
        random_suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
        suggestions.append(query + random_suffix)
    return {"suggestions": suggestions}
