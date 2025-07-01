# Vibeosys FastAPI Assignment – Product APIs

This project implements a FastAPI backend for managing products using MySQL, SQLAlchemy ORM, and Pydantic validations. It includes 4 core endpoints as specified in the assignment.

---

## ✅ Tech Stack

- Python 3.11
- FastAPI – Web framework
- SQLAlchemy – ORM for database operations
- Pydantic – Data validation
- MySQL – Backend database

---
## 📁 Project Structure

vibeosys_fastapi/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       └── product.py
├── requirements.txt
├── README.md

---
## Note

MySQL username and password are **not included** for security reasons.  
Please update the credentials in `app/database.py`:

```python
DATABASE_URL = "mysql+mysqlconnector://<username>:<password>@localhost:3306/vibeosys_db"
```

## 🧩 API Endpoints

### 1. List Products
- **Method**: GET  
- **Endpoint**: `/product/list`  
- **Description**: Returns a paginated list of 10 products

### 2. Product Info
- **Method**: GET  
- **Endpoint**: `/product/{pid}/info`  
- **Description**: Returns details of a specific product by ID

### 3. Add Product
- **Method**: POST  
- **Endpoint**: `/product/add`  
- **Description**: Adds a new product to the database

### 4. Update Product
- **Method**: PUT  
- **Endpoint**: `/product/{pid}/update`  
- **Description**: Updates an existing product by ID

---

## 🗄️ Database Info (MySQL)

- The project uses MySQL as the backend database.

---

## 🖥️ How to Run

```cmd
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- Then open http://localhost:8000/docs


Let me know if you'd like to add a sample product payload or zip the project structure!
