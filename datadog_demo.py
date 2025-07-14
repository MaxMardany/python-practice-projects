import os
import time
import random
from datadog import initialize, api
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

options = {
    'api_key': os.getenv("DD_API_KEY"),
    'app_key': os.getenv("DD_APP_KEY")
}

print("API KEY LOADED:", os.getenv("DD_API_KEY"))
print("Datadog initialized?", os.getenv("DD_API_KEY") is not None and os.getenv("DD_APP_KEY") is not None)

initialize(**options)

while True:
    current_time = int(time.time())

    robot_speed = random.randint(60, 100)
    hopper_weight = random.randint(200, 1000)
    compartment_temp = random.uniform(20.0, 80.0)

    api.Metric.send(
        metric='infinite_kitchen_robot_speed',
        points=[(current_time, robot_speed)],
        tags=["env:demo"]
    )

    api.Metric.send(
        metric='infinite_kitchen_hopper_weight',
        points=[(current_time, hopper_weight)],
        tags=["env:demo"]
    )

    api.Metric.send(
        metric='infinite_kitchen_compartment_temp',
        points=[(current_time, compartment_temp)],
        tags=["env:demo"]
    )

    print(f'Sent metrics -> Speed: {robot_speed} RPM | Weight: {hopper_weight}g | Temp: {compartment_temp:.2f}°C')

    time.sleep(10)
