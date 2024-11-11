# Authentication_Django_Pyhton
# **Django API Project**

This project is a Django-based API server, implemented in Python, that provides user registration, login, and JWT (JSON Web Token) authentication functionalities. The project includes secure access and refresh token mechanisms with token expiration and creation date management.

## **Features**

### **User Registration API**
- Accepts `username`, `email`, and `password`.
- Both `username` and `email` are **unique** to ensure no duplicates.

### **User Login API**
- Accepts `username` and `password` for user authentication.
- Returns JWT `access` and `refresh` tokens upon successful authentication.

### **JWT Authentication**
- JWT `access` and `refresh` tokens are provided on login.
- Tokens are stored in the database with details such as:
  - **Created date**
  - **Expiration date**
- Secure token validation and expiration management for user sessions.

## **API Endpoints**

### **Registration**
- **Endpoint**: `/auth/register/`  
- **Method**: `POST`

#### **Request Body**:
```json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```
  - **Success:** Returns access and refresh JWT tokens with status 200.
  - **Error:** Authentication failed with status 401.
  Response:

- **Success:** User registered successfully with status 201.
- **Error:** Appropriate error messages for duplicate username/email or invalid input.

### Login
- **Endpoint:** `/auth/login/`
- **Method:** `POST`

- **Request Body:**
  
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
    ```

### Tokens:
- **Access Token:** Short-lived token used for authentication on protected routes.
- **Refresh Token:** Long-lived token that can be used to generate a new access token.
- Both tokens are stored in the database with their creation and expiration timestamps to manage token validity and session security.

## Setup and Installation

### Prerequisites:
- Python 3.0+
- Django 5.0+
- Django REST framework
- Simple JWT package for JWT handling

### Installation Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/minahil57/Authentication_Django_Pyhton.git
   

