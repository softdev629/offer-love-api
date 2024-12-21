# Offers API

A FastAPI-based REST API service for managing and retrieving offers from various merchants.

## Features

- Fetch latest offers for carousel/banner display
- Search offers by keywords
- Get merchant-specific offers
- Retrieve offer statistics
- Cross-origin resource sharing (CORS) enabled
- MongoDB integration

## API Endpoints

### Offers

```http
GET /api/offer/latest-images
```
Returns the 8 most recent offers with images, optimized for carousel display.

```http
GET /api/offers/search?q={query}
```
Search offers by query string (minimum 2 characters). Searches through offer titles, descriptions, and merchant names.

```http
GET /api/offer/latest?limit={limit}
```
Get latest offers, sorted by insertion date. Optional limit parameter (default: 10, max: 50).

```http
GET /api/offer/{merchant_slug}/{offer_slug}/{date_slug}
```
Get a specific offer by its merchant slug, offer slug, and end date (YYYY-MM-DD format).

```http
GET /api/offer/merchants
```
Returns a list of all unique merchants with their slugs and names, sorted alphabetically.

### Statistics

```http
GET /api/stats
```
Returns offer statistics including total offers, total merchants, and latest offer timestamp.

## Setup

1. Clone the repository
```bash
git clone https://github.com/softdev629/offer-love-api.git
cd offer-love-api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the development server
```bash
uvicorn app.main:app --reload
```

## Environment Variables

- `MONGO_URI`: MongoDB connection string

## Project Structure

```
.
├── app/
│   ├── main.py
│   ├── config/
│   │   └── database.py
│   ├── models/
│   │   ├── offer.py
│   │   └── response.py
│   ├── routes/
│   │   ├── offer.py
│   │   └── stats.py
│   └── services/
│       ├── offer.py
│       └── stats.py
├── requirements.txt
└── .env
```

## API Response Format

Successful responses follow this format:
```json
{
    "status": "success",
    "data": [
        // Response data
    ]
}
```

Error responses:
```json
{
    "detail": "Error message"
}
```

## Requirements

- Python 3.10+
- FastAPI
- MongoDB
- PyMongo
- Python-dotenv