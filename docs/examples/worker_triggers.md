# Worker Triggers Example

This walkthrough covers the four worker trigger templates: **queue**, **blob**,
**servicebus**, and **eventhub**. All four follow the same scaffold workflow —
generate, configure connections, run locally, and test — with
trigger-specific differences in connection setup and message shape.

## What You Will Build

By the end, you will have:

- a scaffolded worker project for one of the four trigger types
- a working local development environment with the correct emulator or connection
- a customized message handler with service-layer separation
- a passing test suite

## 1) Choose a Worker Template

| Template | CLI Command | Primary Use Case | Connection Required |
| :--- | :--- | :--- | :--- |
| **Queue** | `afs worker queue <name>` | Async message processing from Azure Storage Queues | `AzureWebJobsStorage` |
| **Blob** | `afs worker blob <name>` | File processing triggered by blob uploads | `AzureWebJobsStorage` |
| **Service Bus** | `afs worker servicebus <name>` | Enterprise messaging with queues or topics | `ServiceBusConnection` |
| **Event Hub** | `afs worker eventhub <name>` | High-throughput event stream ingestion | `EventHubConnection` |

## 2) Generate the Project

This walkthrough uses the queue template as the primary example. Replace the
command with any trigger from the table above.

```bash
afs worker queue my-queue-processor
```

Set up environment and dependencies:

```bash
cd my-queue-processor
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

Run quality checks:

```bash
make check-all
```

## 3) Understand Generated Layout

```text
my-queue-processor/
├── function_app.py
├── app/
│   ├── functions/queue.py
│   └── services/queue_service.py
├── tests/test_queue.py
├── local.settings.json.example
└── pyproject.toml
```

- `function_app.py` — registers the queue blueprint.
- `app/functions/queue.py` — trigger handler that decodes messages and logs output.
- `app/services/queue_service.py` — service function for message decoding.
- `tests/test_queue.py` — smoke test using a `SimpleNamespace` stub.

The generated queue handler:

```python
@queue_blueprint.queue_trigger(
    arg_name="message",
    queue_name="work-items",
    connection="AzureWebJobsStorage",
)
def process_queue_message(message: func.QueueMessage) -> None:
    payload = decode_queue_message(message)
    logging.info("Processed queue message: %s", payload)
```

## 4) Local Prerequisites

### Queue and Blob (Azurite)

Queue and blob triggers use `AzureWebJobsStorage` with Azurite for local
development.

Using npm:

```bash
npm install -g azurite
azurite --silent --location .azurite --debug .azurite/debug.log
```

Using Docker:

```bash
docker run --rm -p 10000:10000 -p 10001:10001 -p 10002:10002 \
  mcr.microsoft.com/azure-storage/azurite
```

### Service Bus

Service Bus triggers require a real Azure Service Bus namespace or a local
emulator. Set `ServiceBusConnection` in `local.settings.json` to a valid
connection string.

### Event Hub

Event Hub triggers require a real Azure Event Hubs namespace or a local
emulator. Set `EventHubConnection` in `local.settings.json` to a valid
connection string.

### Activate Local Settings

```bash
cp local.settings.json.example local.settings.json
```

!!! warning "Replace placeholder connection strings"
    Service Bus and Event Hub templates include placeholder connection strings.
    Replace them with real values before running locally.

## 5) Run and Test Locally

```bash
func start
```

Send a test message depending on the trigger type:

- **Queue**: Use Azure Storage Explorer or the Azure CLI to add a message to the
  `work-items` queue.
- **Blob**: Drop a file into the `samples-workitems` container via Storage
  Explorer or Azurite.
- **Service Bus**: Use the Azure CLI or a sender script to post a message to the
  `work-items` queue.
- **Event Hub**: Use the Azure CLI or a sender script to send an event to
  `my-event-hub`.

Watch the terminal for log output confirming message processing.

## 6) Trigger-Specific Configuration

| Trigger | Key Decorator Parameters |
| :--- | :--- |
| **Queue** | `queue_name`, `connection` |
| **Blob** | `path` (container path with `{name}` pattern), `connection` |
| **Service Bus** | `queue_name`, `connection` (use `topic_name` + `subscription_name` for topics) |
| **Event Hub** | `event_hub_name`, `connection` |

## 7) Add a Second Worker Function

Add another function module to the same project:

```bash
afs advanced add queue cleanup --project-root .
```

Preview before writing if needed:

```bash
afs advanced add queue cleanup --project-root . --dry-run
```

After adding, verify:

- `app/functions/cleanup.py` exists
- `function_app.py` includes import and registration
- `tests/test_cleanup.py` exists (if tests are enabled)

## 8) Customization Patterns

Keep trigger modules thin and route business logic to service functions:

```python
from __future__ import annotations

import logging

import azure.functions as func

from app.services.order_service import process_order

queue_blueprint = func.Blueprint()  # type: ignore[no-untyped-call]


@queue_blueprint.queue_trigger(
    arg_name="message",
    queue_name="orders",
    connection="AzureWebJobsStorage",
)
def process_order_message(message: func.QueueMessage) -> None:
    payload = message.get_body().decode("utf-8")
    process_order(payload)
    logging.info("Order processed: %s", payload[:50])
```

!!! tip "Keep business logic separated"
    For larger workers, move parsing, validation, and side effects into
    `app/services/` and keep trigger modules focused on wiring.

## 9) Run Tests

Run the generated test suite:

```bash
pytest
```

The generated tests use `SimpleNamespace` stubs to validate message decoding
without requiring running emulators or real Azure resources.

## Troubleshooting Notes

!!! warning "No messages processed"
    Confirm Azurite is running (queue/blob) or connection strings are valid
    (servicebus/eventhub). Check that `local.settings.json` exists.

!!! warning "Queue name mismatch"
    The queue or container must exist before the trigger can fire. Create
    `work-items` in Azurite or match the name in the decorator to an existing
    resource.

!!! warning "Service Bus or Event Hub connection refused"
    Placeholder connection strings in `local.settings.json.example` are not
    functional. Replace with real Azure resource connection strings.

## Next Steps

- See [Timer Job](timer_job.md) for scheduled workloads.
- See [Templates](../guide/templates.md) for the full template list.
- See [Expanding Your Project](../guide/expanding.md) for add-command flows.
- See [Troubleshooting](../guide/troubleshooting.md) for runtime diagnostics.
