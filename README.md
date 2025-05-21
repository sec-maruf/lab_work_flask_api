# lab_work_flask_api
# Flask RESTful API Project

A simple RESTful API built with Flask for managing person records, created as part of IBM's Python for AI Development course.

## Features

- RESTful endpoints for person management
- CRUD operations (Create, Read, Update, Delete)
- Error handling with JSON responses
- Dynamic URL routing
- Query parameter validation
- JSON request body parsing

## API Endpoints

| Endpoint | Method | Description | Status Codes |
|----------|--------|-------------|--------------|
| `/data` | GET | Get data statistics | 200, 404, 500 |
| `/name_search` | GET | Search by first name | 200, 400, 404, 422 |
| `/count` | GET | Get total person count | 200, 500 |
| `/person/<uuid:id>` | GET | Get person by ID | 200, 404 |
| `/person/<uuid:id>` | DELETE | Delete person by ID | 200, 404 |
| `/person` | POST | Add new person | 200, 422, 500 |

## Error Handling

The API returns JSON-formatted error messages for:
- 400 Bad Request
- 404 Not Found
- 422 Unprocessable Entity
- 500 Internal Server Error

Example error response:
```json
{
  "message": "Error description"
}
