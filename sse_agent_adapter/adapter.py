"""Server-Sent Events line parser and token extractor."""
import json
from typing import Optional, Dict, Any

def parse_sse_line(line: str) -> Optional[Dict[str, Any]]:
    clean = line.strip()
    if not clean.startswith("data:"):
        return None
    payload = clean[5:].strip()
    if payload == "[DONE]":
        return {"delta": "", "done": True}
    try:
        data = json.loads(payload)
        # OpenAI style
        if "choices" in data and data["choices"]:
            delta = data["choices"][0].get("delta", {}).get("content", "")
            return {"delta": delta, "done": False}
        # Generic text style
        if "text" in data:
            return {"delta": data["text"], "done": False}
        return {"delta": str(data), "done": False}
    except Exception:
        return {"delta": payload, "done": False}
