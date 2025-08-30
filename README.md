# Intern Workshop App

A polished Flask app with Bootstrap that demonstrates containerization and CI/CD with GitHub Actions.

## Features

- Flask web app listening on `0.0.0.0:8080`
- Bootstrap 5 responsive design
- Environment variable configuration
- Docker containerization
- Automated GitHub Actions CI/CD
- Publishes to GitHub Container Registry (GHCR)

## Local Development

### Prerequisites

- Python 3.12+
- pip

### Quick Start

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Visit `http://localhost:8080`

### Environment Variables

Customize the app with these environment variables:

- `TITLE` - Main heading (default: "Hello from Intern Workshop")
- `SUBTITLE` - Subheading (default: "Built live with GitHub + Docker 🚀")
- `BUTTON_TEXT` - Button text (default: "Interns Rule ✨")

Example:
```bash
TITLE="Welcome!" SUBTITLE="Custom message" BUTTON_TEXT="Click me!" python app.py
```

## Docker

### Build and Run

```bash
# Build the image
docker build -t intern-workshop-app .

# Run the container
docker run -p 8080:8080 intern-workshop-app

# Run with custom environment variables
docker run -p 8080:8080 -e TITLE="Docker Demo" -e SUBTITLE="Running in container!" intern-workshop-app
```

### Pull from GHCR

```bash
docker pull ghcr.io/OWNER/intern-workshop-app:latest
docker run -p 8080:8080 ghcr.io/OWNER/intern-workshop-app:latest
```

## API Endpoints

- `GET /` - Main page with Bootstrap UI
- `GET /status` - Health check endpoint returning JSON `{"ok": true, "version": "1.0.0"}`

## CI/CD

The GitHub Actions workflow:
- Builds Docker images on all PRs to `main`
- Publishes images to GHCR on pushes to `main`
- Tags images with `latest` and commit SHA
- Image name: `ghcr.io/{owner}/intern-workshop-app`