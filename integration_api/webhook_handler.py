from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import hmac
import hashlib

app = FastAPI()

class WebhookPayload(BaseModel):
    event_type: str
    data: Dict[str, Any]

def verify_signature(payload: bytes, signature: str, secret: str) -> bool:
    computed_signature = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_signature, signature)

@app.post("/webhook")
async def handle_webhook(request: Request, payload: WebhookPayload):
    signature = request.headers.get("X-Webhook-Signature")
    if not signature:
        raise HTTPException(status_code=400, detail="Missing signature")

    raw_payload = await request.body()
    if not verify_signature(raw_payload, signature, "your-webhook-secret"):
        raise HTTPException(status_code=401, detail="Invalid signature")

    # Process the webhook payload based on the event type
    if payload.event_type == "new_message":
        # Handle new message event
        pass
    elif payload.event_type == "channel_update":
        # Handle channel update event
        pass
    elif payload.event_type == "user_action":
        # Handle user action event
        pass
    else:
        # Handle unknown event type
        pass

    return {"status": "success"}

