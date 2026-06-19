# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to practice routing, request/response models, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Setup and Run

#### Description
Set up a Python virtual environment and install dependencies from `requirements.txt`, then run the FastAPI app with `uvicorn`.

#### Requirements
- Create and activate a virtual environment.
- Install dependencies with `pip install -r requirements.txt`.
- Start the server using `uvicorn starter-code:app --reload --port 8000`.

### 🛠️ Implement CRUD Endpoints

#### Description
Implement endpoints to create, read, update, and delete simple `Item` objects stored in-memory.

#### Requirements
Completed project should:
- Expose `GET /items` to list items.
- Expose `GET /items/{item_id}` to retrieve an item.
- Expose `POST /items` to create a new item.
- Expose `PUT /items/{item_id}` to update an item.
- Expose `DELETE /items/{item_id}` to delete an item.
- Use Pydantic models for request/response validation.
- Return appropriate HTTP status codes (201 for create, 404 for not found, etc.).

### 🛠️ Bonus: Documentation and Tests

#### Description
Make use of FastAPI's automatic docs and optionally add simple unit tests.

#### Requirements
- Ensure OpenAPI docs are available at `/docs`.
- (Optional) Add tests using `pytest` that validate endpoint behavior.

## 📂 Files
- Starter code: `starter-code.py`
- Dependencies: `requirements.txt`

## ⏱ Estimated time
~2 hours

## 📚 Resources
- https://fastapi.tiangolo.com/
- https://www.uvicorn.org/
