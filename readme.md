# 📌 Feed System (Twitter-like Architecture Study)

## 🚀 Overview

This project is a backend system inspired by social media platforms like Twitter/X.  
It focuses on **system design, backend architecture, authentication, and scalable feed generation**, rather than UI or frontend features.

The main goal is to simulate how real production backend systems are structured and scaled.

---

## 🎯 Why I Built This Project

I built this system to practice real-world backend engineering concepts such as:

- Designing scalable feed systems
- Implementing layered architecture
- Building secure authentication flows
- Handling asynchronous processing using queues
- Understanding trade-offs between different system designs

Instead of focusing on UI or simple CRUD apps, this project emphasizes **how backend systems evolve under load and complexity**.

---

## 🧠 Core Problem Being Solved

> “How do social media platforms efficiently generate and deliver feeds at scale?”

This introduces real system design challenges:

- High read vs write traffic imbalance
- Feed generation bottlenecks
- Real-time content distribution
- Background processing requirements

---

## 🏗️ Architecture

Each layer has a clear responsibility:

- **Routes** → Handle HTTP requests
- **Controllers** → Manage request/response flow
- **Services** → Business logic
- **Repositories** → Database operations

---

## ⚡ Queue-Based Processing (SCALING COMPONENT)

This system uses a **queue-based architecture** to handle heavy operations asynchronously.

### 🧵 Why Queueing is Used

Queueing solves:

- Slow API responses during heavy operations
- Bottlenecks during post creation
- Blocking database writes under load

---

### 🔥 How It Works

1. User creates a post
2. API sends task to a **queue**
3. Worker processes the task in background:
   - Feed updates
   - Data distribution logic
4. API responds immediately (non-blocking)

---

### ⚙️ Benefits of Queueing

- Faster API responses
- Asynchronous processing
- Better scalability under load
- Worker-based horizontal scaling
- Handles traffic spikes efficiently

---

## 🔐 Authentication System

- JWT-based authentication
- Short-lived access tokens
- Long-lived refresh tokens
- Refresh tokens stored in database (revocable)
- Password hashing using bcrypt

---

## 🗄️ Database Design

### Users
- id
- username
- email
- password (hashed)

### Posts
- id
- user_id
- content
- created_at

### Follows
- follower_id
- following_id

### Refresh Tokens
- id
- user_id
- token

---

## ⚙️ Tech Stack

- FastAPI (Backend framework)
- SQLAlchemy (ORM)
- Alembic (Migrations)
- MySQL (Database)
- JWT (Authentication)
- Passlib (Password hashing)
- Queue System (Background processing for scaling)

---

## 🔄 Authentication Flow

1. User signs up → password is hashed
2. User logs in → receives:
   - Access token (short-lived)
   - Refresh token (long-lived)
3. Access token is used for API requests
4. Refresh token generates new access token when expired
5. Logout deletes refresh token from database

---

## 🚧 Future Improvements

- Feed optimization (fan-out on read vs write vs hybrid)
- Redis caching layer for performance
- Worker scaling for queue system
- Rate limiting for API protection
- JWT middleware for secured routes
- Observability (logging & monitoring)

---

## 💡 Key Takeaway

This project demonstrates that backend systems are not just CRUD applications, but:

> “Systems designed to remain fast, scalable, and reliable under real-world load.”