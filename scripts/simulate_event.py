import json
event = {"detail": {"eventName": "AssumeRole", "sourceIPAddress": "203.0.113.77", "userAgent": "simulated-edr-process-match"}}
print(json.dumps(event))
