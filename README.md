# Core App

Dockerized Streamlit application for graph server interaction

## Getting Started

1. Make sure you have Docker and Docker Compose installed on your system.

2. Build and run the application:
```bash
docker-compose up --build
```

3. Access the application at http://localhost:8501

## Development

- The application code is in `app/main.py`
- Core methods should be placed in `core/`
- Add Python dependencies to `requirements.txt`
- For Rust dependencies, modify the Dockerfile accordingly
