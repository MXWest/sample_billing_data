#!/usr/bin/env python
import random

import yaml


def generate_randomized_entry():
    project_id = random.choice(["my-project-id-1", "my-project-id-2", "my-project-id-3"])
    service_name = random.choice(["Compute Engine", "Cloud Storage", "Cloud SQL", "Cloud Pub/Sub"])
    resource_id = random.randint(1, 10000)
    resource_type = random.choice(["instance", "bucket", "database", "topic"])
    start_time = "2023-01-01T00:00:00Z"
    end_time = "2023-01-02T00:00:00Z"
    usage = random.randint(1, 1000)
    cost = random.randint(1, 1000)
    currency = "USD"
    labels = {"environment": random.choice(["production", "staging", "development"]),
              "team": random.choice(["engineering", "marketing", "sales"])}
    location = "us-central1"
    credits = random.randint(0, 100)
    adjustments = random.randint(0, 100)

    return {
        "project_id": project_id,
        "service_name": service_name,
        "resource_id": resource_id,
        "resource_type": resource_type,
        "start_time": start_time,
        "end_time": end_time,
        "usage": usage,
        "cost": cost,
        "currency": currency,
        "labels": labels,
        "location": location,
        "credits": credits,
        "adjustments": adjustments,
    }


entries = []
for _ in range(100):
    entries.append(generate_randomized_entry())

with open("randomized_entries.yaml", "w") as f:
    yaml.dump(entries, f, indent=2)
