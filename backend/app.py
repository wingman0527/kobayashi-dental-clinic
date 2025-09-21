from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
from pathlib import Path
import json
import datetime

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

CONTACTS_FILE = DATA_DIR / "contacts.json"
APPOINTMENTS_FILE = DATA_DIR / "appointments.json"

class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str

class Appointment(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    date: str  # YYYY-MM-DD
    time: str  # HH:MM
    note: Optional[str] = None

app = FastAPI(title="Kobayashi Dental Clinic API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/clinic-info")
async def clinic_info():
    return {
        "name": "小林歯科",
    "tagline": "あなたの笑顔を、美しく健やかに",
    "motto": "いつもの治療を、ていねいに。",
        "address": "〒134-0083 中葛西6-2-1",
        "phone": "03-3687-4181",
    "director": "小林 一公",
        "hours": {
            "mon_fri": "09:30 - 13:00 / 14:30 - 19:30",
            "sat": "09:30 - 13:00 / 14:30 - 16:30",
            "sun_holiday": "休診（日・祝）"
        },
        "services": ["歯科", "矯正歯科", "小児歯科", "歯科口腔外科"],
        "access": "地下鉄東西線 西葛西駅から 都バス なぎさニュータウン行『西葛西6丁目』下車 徒歩9分 / JR京葉線 葛西臨海公園駅から 都バス 西葛西駅行『中葛西7丁目』下車 徒歩3分"
    }

@app.post("/api/contact")
async def contact(contact: Contact):
    payload = contact.model_dump()
    payload["created_at"] = datetime.datetime.utcnow().isoformat()
    _append_json(CONTACTS_FILE, payload)
    return {"ok": True}

@app.post("/api/appointment")
async def appointment(appt: Appointment):
    # 簡易バリデーション
    try:
        datetime.datetime.strptime(appt.date, "%Y-%m-%d")
        datetime.datetime.strptime(appt.time, "%H:%M")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date or time format")

    payload = appt.model_dump()
    payload["created_at"] = datetime.datetime.utcnow().isoformat()
    _append_json(APPOINTMENTS_FILE, payload)
    return {"ok": True}


def _append_json(file: Path, data: dict):
    if not file.exists():
        file.write_text(json.dumps([data], ensure_ascii=False, indent=2), encoding="utf-8")
        return
    try:
        existing = json.loads(file.read_text(encoding="utf-8"))
        if not isinstance(existing, list):
            existing = []
    except Exception:
        existing = []
    existing.append(data)
    file.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
