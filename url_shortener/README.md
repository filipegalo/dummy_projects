# Modern URL Shortener

A modern, microservices-based URL shortener with a beautiful UI. Built with FastAPI, Next.js, and Redis.

## Features

- ⚡️ Fast URL shortening with Redis caching
- 🎨 Modern, responsive UI with glassmorphism design
- 🔄 Real-time URL redirection
- 📱 Mobile-friendly interface
- 🚀 Microservices architecture
- 🔒 Input validation and error handling
- 📋 One-click copy functionality

## Tech Stack

### Backend
- FastAPI - Fast and modern Python web framework
- Redis - In-memory data storage
- Docker - Containerization
- Python 3.12 - Programming language

### Frontend
- Nuxt.js - React framework
- TailwindCSS - Utility-first CSS framework
- TypeScript - Type-safe JavaScript

## Project Structure

```
url-shortener/
├── services/
│ ├── shortener-service/ # URL shortening service
│ │ ├── main.py # FastAPI application
│ │ ├── Dockerfile # Service container definition
│ │ └── requirements.txt # Python dependencies
│ └── redirect-service/ # URL redirection service
│ ├── main.py # FastAPI application
│ ├── Dockerfile # Service container definition
│ └── requirements.txt # Python dependencies
├── frontend/ # Next.js frontend application
│ ├── src/ # Source code
│ ├── public/ # Static files
│ └── Dockerfile # Frontend container definition
└── docker-compose.yml # Docker composition file
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local development)
- Python 3.12+ (for local development)

### Running with Docker Compose

```bash
docker-compose up --build
```


## API Documentation

### Shortener Service (Port 8000)

#### POST /shorten
Creates a shortened URL
- Request Body: `{ "long_url": "https://example.com" }`
- Response: `{ "short_url": "abc123", "long_url": "https://example.com" }`

### Redirect Service (Port 8001)

#### GET /{short_code}
Redirects to the original URL
- Response: HTTP 302 redirect to the original URL

## Environment Variables

### Frontend (.env.local)

NEXT_PUBLIC_SHORTENER_SERVICE_URL=http://localhost:8000
NEXT_PUBLIC_REDIRECT_SERVICE_URL=http://localhost:8001


### Services (docker-compose.yml)

REDIS_HOST=redis
REDIS_PORT=6379

## License

This project is licensed under the WTFPL - see the [LICENSE](LICENSE) file for details.
