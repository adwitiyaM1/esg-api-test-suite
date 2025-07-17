**Test Strategy:**
| Type            | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| **Integration** | Tests API endpoints end-to-end using live API                          |
| **Regression**  | Will be run continuously to ensure existing functionality isn’t broken |
| **Negative**    | Inputs with invalid payloads, missing parameters, etc.                 |

**Test Data & Environment:**
- Dynamic Data: Test payloads created and deleted within tests using fixtures. 
- Environment: Uses localhost:8000 by default, configurable via env vars.
- Data Cleanup: Use setup/teardown or fixtures to prevent test data from persisting.

**Scalability Strategy:**
- CI/CD Integration: Integrate with GitHub Actions, Jenkins, etc. Enables automated regression testing on every commit.
- Environment Configs: Use .env to manage different test environments (dev, stage, prod).
- Modular test files per endpoint. Add new files for new domains (e.g. test_users.py, test_reports.py).

## Files & Purpose:
### 1. `test_kpis.py`
#### Tests for KPI endpoints:
- GET /kpis: Retrieves all KPIs.
- GET /kpis/{id}: Retrieves a specific KPI.

### 2. `test_data.py`
#### Tests for data point endpoints:
- POST /data: Adds new KPI data.
- PUT /data/{id}: Updates KPI data.
- DELETE /data/{id}: Deletes data.
