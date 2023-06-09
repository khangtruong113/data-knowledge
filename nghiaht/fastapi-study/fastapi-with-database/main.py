from fastapi import FastAPI
from student import router as student_router
import uvicorn

app = FastAPI(title="Sample Docs", description="private", version="1.0", redoc_url=None)




app.include_router(student_router.router)


uvicorn.run(app, port=8000, host="127.0.0.1")