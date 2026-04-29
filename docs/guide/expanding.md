# Expanding Your Project

The `afs api add` and `afs advanced add` commands let you add new triggers to an existing project while maintaining the Blueprint structure. They automatically handle trigger registration in `function_app.py`.

### Add Commands

Use `afs api add` for HTTP functions and `afs advanced add` for non-HTTP triggers.

```bash
afs api add <function-name> --project-root <path>
afs advanced add <trigger-type> <function-name> --project-root <path>
```

When you run this command, the CLI:
1. Creates a new Blueprint file in `app/functions/`.
2. Creates a unit test in `tests/`.
3. Imports and registers the new Blueprint in `function_app.py`.

### Examples

Add a secondary HTTP endpoint to your API:
```bash
afs api add user-profile
```

Add a timer trigger to an existing project:
```bash
afs advanced add timer cleanup-job
```

Add a queue listener to handle background tasks:
```bash
afs advanced add queue task-processor
```

### Dry Run

Use the `--dry-run` flag to preview which files will be created and how `function_app.py` will be modified before making any changes.

```bash
afs api add reports --dry-run
```

### Development Workflow

1.  **Add Trigger**: Run `afs api add` or `afs advanced add` to generate the boilerplate.
2.  **Implement Logic**: Create a corresponding service file in `app/services/` and write your core business rules there.
3.  **Update Schemas**: If needed, define new request/response models in `app/schemas/`.
4.  **Add Tests**: Update the generated test file in `tests/` to verify your new function.

### What's Next?

Once your project is ready, follow the [Deploying](deploying.md) guide to push it to Azure.
