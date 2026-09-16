"""Simulation-only cloud/endpoint correlation handler."""
import json
from datetime import datetime, timezone

KNOWN_CIDRS = ("10.", "192.168.", "172.16.")

def is_known_ip(ip):
    return ip.startswith(KNOWN_CIDRS)

def handler(event, context):
    detail = event.get("detail", {})
    name = detail.get("eventName")
    ip = detail.get("sourceIPAddress", "")
    endpoint_match = detail.get("userAgent") == "simulated-edr-process-match"
    suspicious = name == "AssumeRole" and not is_known_ip(ip) and endpoint_match
    result = {"timestamp": datetime.now(timezone.utc).isoformat(), "suspicious": suspicious, "mode": "simulation-only"}
    if suspicious:
        result["finding"] = {"title": "Cloud/endpoint correlation: possible lateral movement", "severity": "HIGH"}
    print(json.dumps(result))
    return result
