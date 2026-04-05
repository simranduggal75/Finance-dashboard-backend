# Finance Dashboard Backend

A backend system for managing financial records with role-based access control, built using FastAPI and SQLite.



## 🚀 Features

- User and Role Management (ADMIN, ANALYST, VIEWER)
- Financial Records CRUD (Create, Read, Update, Delete)
- Filtering by type, category, and date
- Pagination support (skip, limit)
- Dashboard Summary (total income, expenses, balance)
- Role-Based Access Control (RBAC)
- Input validation using Pydantic
- SQLite database with SQLAlchemy ORM



## 🛠️ Tech Stack

- Backend: FastAPI (Python)
- Database: SQLite
- ORM: SQLAlchemy
- Validation: Pydantic
- API Docs: Swagger UI (auto-generated)



## 📂 Project Structure

finance-dashboard-backend/

│── models/

│── routes/

│── services/

│── schemas/

│── utils/

│── main.py

│── database.py

│── requirements.txt

│── .gitignore

│── README.md



## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/simranduggal75/finance-dashboard-backend.git  
cd finance-dashboard-backend


### 2. Install dependencies

pip install -r requirements.txt


### 3. Run the application

uvicorn main:app --reload



### 4. Open API docs

http://127.0.0.1:8000/docs



## 🔐 Role-Based Access Control

Roles are passed using request headers:

X-ROLE: ADMIN  
X-ROLE: ANALYST  
X-ROLE: VIEWER  

### Permissions:

- ADMIN → Full access (CRUD operations)
- ANALYST → View records + dashboard
- VIEWER → View-only access



## 📊 API Endpoints

### Users

- POST /users → Create user  
- GET /users → Get all users  



### Transactions

- POST /transactions → Create transaction  
- GET /transactions → Get all transactions  
- PUT /transactions/{id} → Update transaction  
- DELETE /transactions/{id} → Delete transaction  

#### Filtering:

/transactions?type=expense  
/transactions?category=food  
/transactions?date=2026-04-05  

#### Pagination:

/transactions?skip=0&limit=10  



### Dashboard

- GET /dashboard/summary  

Returns:

{
  "totalIncome": 5000,
  "totalExpense": 2000,
  "balance": 3000
}



## ⚠️ Assumptions & Trade-offs

- Authentication is simplified using header-based roles (no JWT)
- SQLite is used for simplicity and quick setup
- Focus is on backend design and API structure rather than production deployment



## 🔮 Future Improvements

- Add JWT-based authentication  
- Use PostgreSQL for scalability  
- Add user status management (active/inactive)  
- Implement unit tests  
- Deploy API (Render / AWS)  



## 📌 Notes

- Ensure correct role header (X-ROLE) is provided while testing APIs  
- API can be tested directly using Swagger UI  


## 👩‍💻 Author

Simran Duggal

AI/ML Engineer 


## ⭐ If you found this useful

Give this repo a ⭐ on GitHub!

## 📸 Output Screenshot
  Please refer to screenshots folder for output screenshots