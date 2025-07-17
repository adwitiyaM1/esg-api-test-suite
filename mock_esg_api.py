from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class KPI(BaseModel):
    id: int
    name: str
    unit: float
    category: str
    mandatory: bool


kpis = [
    KPI(id=1, name="Energy Consumption", unit=10.5, category="Environment", mandatory=True),
    KPI(id=2, name="Water Usage", unit=20.3, category="Environment", mandatory=False)
]

data_store = {}

@app.get("/kpis", response_model=List[KPI])
def get_kpis():
    return kpis

@app.get("/kpis/{kpi_id}", response_model=KPI)
def get_kpi(kpi_id: int):
    for kpi in kpis:
        if kpi.id == kpi_id:
            return kpi
    raise HTTPException(status_code=404, detail="KPI not found")

@app.post("/data", status_code=201)
def create_data(kpi: KPI):
    data_store[kpi.id] = kpi
    return kpi

@app.put("/data/{kpi_id}", status_code=200)
def update_data(kpi_id: int, kpi: KPI):
    if kpi_id not in data_store:
        raise HTTPException(status_code=404, detail="KPI not found")
    data_store[kpi_id] = kpi
    return kpi

@app.delete("/data/{kpi_id}", status_code=200)
def delete_data(kpi_id: int):
    if kpi_id not in data_store:
        raise HTTPException(status_code=404, detail="KPI not found")
    del data_store[kpi_id]
    return {"message": "Deleted"}