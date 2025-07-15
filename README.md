# STOCKERRA

Cloud based inventory management system.

This repository contains a minimal FastAPI backend prototype. Features include:

- Product management with categories and brands
- Stock transaction tracking (in/out/transfer)
- Basic in-memory storage for demonstration

The backend code is located in `backend/`.

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
