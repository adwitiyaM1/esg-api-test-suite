# Setup:

**1. Create the Virtual Environment**
- python3 -m venv venv

**2. Activate the Environment**
- venv\\Scripts\\activate (Windows)
  
**3. Install Dependencies**
- pip install -r requirements.txt

# How to Run the Mock API:
**1. Install FastAPI and Uvicorn**
- pip install fastapi uvicorn

**2. Run the server**
- uvicorn mock_esg_api:app --reload

**Your API will now be available at:**
http://localhost:8000

**Now run the Tests
Activate your virtualenv and run:**
- pytest -v

All tests should now pass