from fastapi import APIRouter, Depends, HTTPException
from model.event import Event
from db import get_db
from sqlalchemy.orm import Session

router = APIRouter()
@router.get('/api/events')
async def events_list(db: Session = Depends(get_db)):
    events_list = db.query(Event).all()
    return events_list

@router.get('/api/events/{event_id}')
async def event_detail(event_id: int, db: Session = Depends(get_db)):
    event_list = db.query(Event).filter(Event.id == event_id).first()
    if event_list is None:
        raise HTTPException(status_code=404, detail="item_not_found")
    else:
        return event_list
