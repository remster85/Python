# FastAPI Docker Example

This project demonstrates how to containerize a FastAPI application using Docker and run it with working internet access (even in restricted environments like WSL).

## Prerequisites

- Docker installed and running
- Internet connectivity from Docker containers

## Build Instructions

To build the Docker image with proper network access (especially useful in environments like WSL):

```bash
docker build --network=host -t fastapi-hello .
```

> The `--network=host` flag allows the build process (especially `pip install`) to access the internet.

## Run the Container

Once built, you can run the container:

```bash
docker run -p 8000:8000 fastapi-hello
```

Access the app at [http://localhost:8000](http://localhost:8000)

## Project Structure

```
.
├── app
│   └── main.py
├── requirements.txt
└── Dockerfile
```

## Sample `Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Sample `requirements.txt`

```txt
fastapi
uvicorn[standard]
```

## Sample `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI inside Docker!"}
```

## Troubleshooting

If you encounter issues like:

```
pip._vendor.urllib3.connection.HTTPSConnection: Failed to establish a new connection: [Errno 101] Network is unreachable
```

Add `--network=host` to your `docker build` command as shown above.

## License

MIT
