"""Deterministic teaching simulator; no network calls or real messages."""
import hashlib
import json
from datetime import datetime, timezone

CATEGORIES = {"sales", "support", "billing", "other"}

def classify(message):
    """Mock model substitute. Ambiguity uses a review status, not a category."""
    if not isinstance(message, str) or not message.strip():
        return {"status": "needs_review", "category": None}
    text = message.lower()
    hits = [category for word, category in (("charge", "billing"), ("demo", "sales"), ("broken", "support")) if word in text]
    if len(set(hits)) != 1:
        return {"status": "needs_review", "category": None}
    return {"status": "ok", "category": hits[0]}

def validate_decision(decision):
    if not isinstance(decision, dict):
        return False
    return ((decision.get("status") == "ok" and isinstance(decision.get("category"), str) and decision.get("category") in CATEGORIES)
            or (decision.get("status") == "needs_review" and decision.get("category") is None))

def make_draft(event):
    for key in ("event_id", "name", "email", "message"):
        if not isinstance(event.get(key), str) or not event[key].strip():
            raise ValueError(f"missing or invalid {key}")
    email = event["email"].strip().lower()
    if email.count("@") != 1 or any(c.isspace() for c in email):
        raise ValueError("invalid email")
    local, domain = email.split("@")
    if not local or "." not in domain or domain.startswith(".") or domain.endswith("."):
        raise ValueError("invalid email")
    decision = classify(event["message"])
    return {"event_id": event["event_id"].strip(), "recipient": email,
            "body": f"Hello {event['name'].strip()}, we received your request.",
            "decision": decision}

def digest(draft):
    return hashlib.sha256(json.dumps(draft, sort_keys=True).encode()).hexdigest()

def execute(draft, approved_digest, sent, logs, service_available=True):
    # Validate and review before side effects; approval is a teaching-only token.
    decision = draft.get("decision")
    if not validate_decision(decision):
        outcome = "invalid_decision"
    elif decision["status"] != "ok":
        outcome = "needs_review"
    elif approved_digest != digest(draft):
        outcome = "approval_required"
    elif draft["event_id"] in sent:
        outcome = "duplicate_suppressed"
    elif not service_available:
        outcome = "service_failed"
    else:
        sent.add(draft["event_id"])
        outcome = "simulated_sent"
    logs.append({"timestamp": datetime.now(timezone.utc).isoformat(),
                 "step": "simulated_send", "status": outcome})
    return outcome

def main():
    event = {"event_id": "demo-001", "name": "Morgan", "email": "morgan@example.com", "message": "Can I get a demo?"}
    draft = make_draft(event)
    sent, logs = set(), []
    approval = digest(draft)
    print(execute(draft, approval, sent, logs))
    print(execute(draft, approval, sent, logs))
    draft["body"] = "Edited draft requires new approval."
    print(execute(draft, approval, sent, logs))
    review = make_draft(dict(event, event_id="demo-002", message="Help please"))
    print(execute(review, digest(review), sent, logs))
    print(json.dumps(logs, indent=2))

if __name__ == "__main__":
    main()
