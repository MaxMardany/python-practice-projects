from datadog import initialize, api
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DD_API_KEY")
app_key = os.getenv("DD_APP_KEY")

# Debug prints
print(f"DD_API_KEY loaded: {api_key[:6]}...")
print(f"DD_APP_KEY loaded: {app_key[:6]}...")

options = {
    'api_key': api_key,
    'app_key': app_key
}
initialize(**options)

response = api.Metric.send(
    metric='debug.metric.test',
    points=[(time.time(), 99)],
    tags=["env:test"]
)
print("📤 Response:", response)

