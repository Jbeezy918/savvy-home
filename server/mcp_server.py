from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"status": "Savvy Home running", "version": "0.1.2"}

def main():
    import uvicorn
    print("🏠 Savvy Home Server")
    print("📍 http://localhost:5055")
    uvicorn.run(app, host="0.0.0.0", port=5055)

if __name__ == "__main__":
    main()
