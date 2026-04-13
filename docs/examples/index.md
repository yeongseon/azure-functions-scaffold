# Examples Overview

Use these practical walkthroughs to move from scaffold generation to a running,
customized function app.

## Available Examples

- [HTTP API](http_api.md): strict API project with endpoint customization,
  OpenAPI usage, and local verification.
- [Timer Job](timer_job.md): scheduled workloads, NCRONTAB patterns, and Azurite
  setup for local execution.
- [Worker Triggers](worker_triggers.md): queue, blob, Service Bus, and Event Hub
  trigger projects with connection setup and local testing.
- [Durable Workflow](durable_workflow.md): orchestrator, activities, and HTTP
  starter for durable workflows.
- [CosmosDB Change Feed](cosmosdb_change_feed.md): change feed processing with
  lease tracking and emulator setup.
- [AI Agents](ai_agents.md): Azure OpenAI chat endpoint and LangGraph agent
  deployment.
- [Full Stack](full_stack.md): end-to-end setup with strict preset, OpenAPI,
  validation, doctor checks, and CI-oriented workflow.

## Recommended Order

1. Start with HTTP API if you are new to the scaffold.
2. Continue with Timer Job if you need background/scheduled processing.
3. Try Worker Triggers for message and event-driven patterns.
4. See Durable Workflow or CosmosDB Change Feed for specialized triggers.
5. See AI Agents for OpenAI or LangGraph workloads.
6. Use Full Stack as your production baseline template.

## Related Docs

- [Configuration](../guide/configuration.md)
- [CLI Reference](../reference/cli.md)
- [Troubleshooting](../guide/troubleshooting.md)
