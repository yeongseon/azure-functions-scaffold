# Security

The azure-functions-scaffold project is committed to providing a secure tool for generating Azure Functions projects. This document outlines our security policies, the measures we take to ensure the integrity of the scaffolded code, and how you can report potential vulnerabilities.

## Reporting Vulnerabilities

If you discover a security vulnerability within this project, please report it privately to ensure a coordinated disclosure process.

### Preferred Method
The most secure way to report a vulnerability is through the GitHub Security Advisory system:
https://github.com/yeongseon/azure-functions-scaffold/security/advisories/new

### Alternative Method
You can also contact the maintainer directly via email at:
yeongseon.choe@gmail.com

### What to Include
When submitting a report, please provide as much detail as possible to help us understand and resolve the issue quickly:
- A clear and descriptive title
- Detailed steps to reproduce the vulnerability
- A description of the potential impact
- Any suggested fixes or mitigations

### Response Timeline
- Initial acknowledgment: Within 48 hours of the report.
- Status update: Within 7 days of the initial acknowledgment.

We ask that you follow responsible disclosure practices and refrain from sharing the vulnerability publicly until a fix has been released.

## Supported Versions

We only provide security updates for the latest stable release of the tool.

| Version | Supported |
| :--- | :--- |
| Latest release | Yes |
| Older releases | No |

It's recommended to always use the most recent version of azure-functions-scaffold to benefit from the latest security improvements and bug fixes.

## Security Scanning

We use automated tools to maintain the security posture of the codebase.

### Bandit
Bandit (version 1.9.4) is used for static analysis security scanning. It's configured to:
- Scan all Python files in the `src/` directory.
- Exclude `tests/` and other non-production directories.

### Running Scans Locally
You can run the security scanner locally using one of the following commands:
```bash
make security
```
or
```bash
hatch run security
```

### CI/CD Integration
The `security.yml` workflow runs Bandit on every push and pull request to the main repository. This ensures that no new security issues are introduced during development.

### Pre-commit Hooks
Bandit is also integrated into our pre-commit configuration. It automatically scans changed files in the `src/` directory before any commit is finalized, preventing common security pitfalls from entering the version history.

## Security Scope

Understanding the boundaries of our security responsibility helps you use the tool more safely.

### Within Scope
- **Template Integrity**: We ensure that the generated code templates are free of known vulnerabilities and follow best practices.
- **Input Validation**: The tool validates project names and configuration options to prevent issues like path traversal or command injection during the scaffolding process.
- **Dependency Surface**: We maintain a minimal runtime dependency footprint, currently limited to `jinja2` and `typer`.

### Out of Scope
- **Generated Project Security**: Once a project is generated, its ongoing security is your responsibility. This includes updating dependencies within the generated project and ensuring your business logic is secure.
- **Azure Functions Runtime**: Security of the underlying Azure platform and the Functions runtime is managed by Microsoft.
- **User Modifications**: Any manual changes you make to the templates or the generated code are outside our security scope.

## Security Best Practices for Users

Follow these guidelines to maintain a secure environment for your functions:
- Review all generated code before deploying it to production environments.
- Keep the azure-functions-scaffold tool updated to the latest version.
- Use the `--preset strict` flag to include high-quality linting and security tooling in your generated project.
- Enable the `--with-validation` option for HTTP-triggered functions to include built-in input validation.
- Regularly update the dependencies within your generated projects.

## Dependency Security

The tool is designed to be lightweight and secure by design.

### Minimal Dependencies
Azure-functions-scaffold has only two runtime dependencies:
1. `jinja2`: Used for template rendering.
2. `typer`: Used for the command-line interface.

### Automated Updates
We use Dependabot to monitor our dependencies and automatically create pull requests for security updates and version bumps.

### No Network Calls
The scaffolding process is performed entirely locally. All templates are embedded within the package, so no network calls are made during the project generation phase. This mitigates risks associated with man-in-the-middle attacks or malicious remote content.
