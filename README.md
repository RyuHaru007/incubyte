# Incubyte Salary Management API 🚀

A robust, production-ready REST API built with FastAPI and Python to manage employee data and calculate region-specific salary metrics.

## 🛠 Tech Stack & Architecture

- **Language:** Python 3.11
- **Framework:** FastAPI
- **Database:** SQLite with SQLAlchemy ORM
- **Testing:** Pytest with `pytest-cov` (Using an isolated, in-memory `StaticPool` database)
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions
- **Architecture Pattern:** Clean Architecture (Separation of API Routers, Business Services, and Data Access/CRUD layers)

---

## 🎯 Methodology: Strict TDD & Micro-Cycles

This repository was constructed using **Strict Test-Driven Development (TDD)**, adhering closely to the purist "Red-Green-Refactor" micro-cycles. 

Instead of practicing "Test-First" development (writing all tests for a feature upfront and batching the implementation), this codebase evolved incrementally:
1. **RED:** Write *one* single, minimal failing test (e.g., testing the 10% deduction rule for India).
2. **GREEN:** Write the absolute simplest code to pass *only* that test (often hardcoding logic in the router).
3. **REFACTOR:** Abstract the implementation into clean architecture (e.g., moving the math to a `services.py` layer) without changing external behavior.

### Key Engineering Practices Demonstrated:
- **Atomic Commits:** Features, bug fixes, and infrastructure setup are strictly isolated in their own commits.
- **Emergent Design:** Complex requirements (like the country-specific salary rules) were not built "Big-Bang." They emerged organically, one country at a time, resulting in a cleaner `services` layer.
- **Explicit Refactoring:** Frequent, dedicated `refactor` commits that extract duplicate logic (e.g., extracting 404 validation into reusable helper functions) while the tests remained green.

---

## 🤖 AI Implementation Details (Transparency Statement)

As requested, here is a transparent breakdown of how Artificial Intelligence (LLM) was utilized as a collaborative pair-programmer during this exercise to maintain high velocity and code quality:

**1. Scaffolding & DevOps Boilerplate:**
- *Usage:* Generated standard boilerplate like the `Dockerfile`, `docker-compose.yml`, and the GitHub Actions `ci.yml` pipeline.
- *Rationale:* AI excels at standard infrastructure configuration, allowing me to focus my cognitive energy purely on domain business logic and TDD flows.

**2. Enforcing Strict TDD Micro-Cycles:**
- *Usage:* I used the AI to help me decompose large business requirements into granular, sequential micro-cycles. 
- *Example:* Instead of asking the AI to "write tests for the salary endpoint," I prompted it to act as an agile pair programmer: "Help me write *just* the failing test for the Indian salary deduction rule." Once passed, I prompted: "Now let's refactor this before moving to the US rule."
- *Rationale:* This prevented batching and ensured a pristine, atomic Git history.

**3. Database Optimizations:**
- *Usage:* During the metrics implementation, I collaborated with the AI to utilize SQLAlchemy aggregations (`func.min`, `func.max`, `func.avg`).
- *Rationale:* AI helped ensure the syntax was correct while I drove the architectural decision to offload mathematical computation to the database layer rather than the Python application layer.

---

## 🚀 Running the Application

### Option 1: Docker Container (Recommended)
1. **Build and spin up the container:**
   ```bash
   docker-compose up -d --build
   ```
2. **View Swagger UI:** Navigate to [http://localhost:8000/docs](http://localhost:8000/docs)
3. **Tear down:**
   ```bash
   docker-compose down
   ```

### Option 2: Local Virtual Environment
1. **Create and activate venv:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🧪 Testing

The test suite validates Schemas, CRUD operations, Salary Calculations, and Metrics using an isolated in-memory database pool.

**Run the tests with coverage:**
```bash
pytest --cov=app tests/
```

## ⚙️ CI/CD Pipeline
Every push to the `main` branch triggers a GitHub Actions pipeline that provisions an Ubuntu environment, installs dependencies, and runs the entire Pytest suite to ensure zero regressions.