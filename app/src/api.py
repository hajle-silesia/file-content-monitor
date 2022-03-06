from fastapi import FastAPI
from file_content_monitor import FileContentMonitor


api = FastAPI()
file_content_monitor = FileContentMonitor("./file_content_monitor/recipe.txt")


@api.get("/content")
async def content():
    return {"content": file_content_monitor.content,
            }
