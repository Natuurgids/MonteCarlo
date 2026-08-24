"""
Development-only AI gateway.

Run:
    uvicorn mock_gateway:app --host 127.0.0.1 --port 8000

Then set the app AI endpoint to:
    http://127.0.0.1:8000/assess

This gateway DOES NOT perform AI or internet research.
It exists only to test the end-to-end integration contract.
"""
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI
from typing import Any

app = FastAPI(title="SCA Mock AI Gateway")

@app.post("/assess")
def assess(payload: dict[str, Any]):
    drivers = []
    for d in payload.get("drivers", []):
        drivers.append({
            "driver_id": d["driver_id"],
            "low": d["human_low"],
            "ml": d["human_ml"],
            "high": d["human_high"],
            "confidence": 0.0,
            "reason": "MOCK gateway only — Human values echoed; no AI or external research used."
        })
    e = payload.get("event", {})
    now = datetime.now(timezone.utc)
    return {
        "assessment_id": "MOCK-" + now.strftime("%Y%m%d%H%M%S"),
        "generated_at": now.isoformat(),
        "valid_until": (now + timedelta(days=1)).date().isoformat(),
        "engine": "mock-no-ai",
        "internet_used": False,
        "drivers": drivers,
        "event": {
            "driver_id": "REGIONAL_EVENT",
            "probability": e.get("human_probability", 0),
            "impact_low": e.get("human_impact_low", 0),
            "impact_ml": e.get("human_impact_ml", 0),
            "impact_high": e.get("human_impact_high", 0),
            "confidence": 0.0,
            "reason": "MOCK gateway only — no geopolitical assessment performed."
        },
        "evidence": []
    }
