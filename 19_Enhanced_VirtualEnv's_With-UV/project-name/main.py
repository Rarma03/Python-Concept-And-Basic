import uvicorn
from fastapi import FastAPI

def main():
    print("Hello from project-name!")
    uvicorn.run(app, host='127.0.0.1', port=8000)

app = FastAPI()

# create a route
@app.get('/')
async def root():
    return {'message': 'hello raj verma!'}

if __name__ == "__main__":
    main()