# azure-functions-scaffold

[![PyPI](https://img.shields.io/pypi/v/azure-functions-scaffold.svg)](https://pypi.org/project/azure-functions-scaffold/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://pypi.org/project/azure-functions-scaffold/)
[![CI](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/ci-test.yml/badge.svg)](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/ci-test.yml)
[![Release](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/release.yml/badge.svg)](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/release.yml)
[![Security Scans](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/security.yml/badge.svg)](https://github.com/yeongseon/azure-functions-scaffold/actions/workflows/security.yml)
[![codecov](https://codecov.io/gh/yeongseon/azure-functions-scaffold/branch/main/graph/badge.svg)](https://codecov.io/gh/yeongseon/azure-functions-scaffold)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://yeongseon.github.io/azure-functions-scaffold/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

其他语言: [English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md)

用于生产导向的 Azure Functions Python v2 项目的脚手架 CLI。

项目名称必须以字母或数字开头，且仅包含字母、数字、连字符（-）或下划线（_）。

## Scope

- Azure Functions Python **v2 编程模型**
- 基于装饰器的 `func.FunctionApp()` 应用程序
- 轻量级且实用的项目生成
- 交互式引导、预设和函数扩展

本项目**不**支持基于 `function.json` 的旧版 Python v1 编程模型。

## Features

- `azure-functions-scaffold new <project-name>`
- `azure-functions-scaffold new <project-name> --template http|timer|queue|blob|servicebus`
- `azure-functions-scaffold new --interactive`
- `azure-functions-scaffold new <project-name> --preset minimal|standard|strict`
- `azure-functions-scaffold new <project-name> --with-openapi` — 包含 OpenAPI 文档 (Swagger UI, JSON, YAML)
- `azure-functions-scaffold new <project-name> --with-validation` — 包含请求/响应验证
- `azure-functions-scaffold new <project-name> --with-openapi --with-validation` — 结合以上两种功能
- `azure-functions-scaffold new <project-name> --with-doctor` — 包含 azure-functions-doctor 健康检查
- `azure-functions-scaffold add http <function-name>`
- `azure-functions-scaffold add timer <function-name>`
- `azure-functions-scaffold add queue <function-name>`
- `azure-functions-scaffold add blob <function-name>`
- `azure-functions-scaffold add servicebus <function-name>`
- 针对不同触发器的内置项目模板
- 生成的成果中包含测试、Lint 和打包的默认设置
- 面向服务的微型应用程序结构

## Installation

```bash
pip install azure-functions-scaffold
```

本地开发使用:

```bash
git clone https://github.com/yeongseon/azure-functions-scaffold.git
cd azure-functions-scaffold
make install
```

## Usage

在当前目录创建一个新的 HTTP 项目:

```bash
azure-functions-scaffold new my-api
```

创建一个新的定时器项目:

```bash
azure-functions-scaffold new my-job --template timer
```

创建一个用于本地 Azurite 开发的队列触发器项目:

```bash
azure-functions-scaffold new my-worker --template queue
```

创建一个用于本地 Azurite 开发的 Blob 触发器项目:

```bash
azure-functions-scaffold new my-blob-worker --template blob
```

创建一个 Service Bus 触发器项目:

```bash
azure-functions-scaffold new my-bus-worker --template servicebus
```

交互式地创建项目:

```bash
azure-functions-scaffold new --interactive
```

交互式提示会在生成前验证项目名称、模板、预设和 Python 版本，以便在提示阶段纠正错误，而不是在生成过程中失败。

预览生成的项目而不实际写入文件:

```bash
azure-functions-scaffold new my-api --template queue --preset strict --dry-run
```

显式替换现有的脚手架项目:

```bash
azure-functions-scaffold new my-api --overwrite
```

创建一个包含 OpenAPI 文档 (Swagger UI, JSON, YAML 端点) 的 HTTP 项目:

```bash
azure-functions-scaffold new my-api --with-openapi
```

创建一个包含请求/响应验证的 HTTP 项目:

```bash
azure-functions-scaffold new my-api --with-validation
```

创建一个同时包含 OpenAPI 和验证的 HTTP 项目:

```bash
azure-functions-scaffold new my-api --with-openapi --with-validation
```

创建一个包含 azure-functions-doctor 健康检查的项目:

```bash
azure-functions-scaffold new my-api --with-doctor
```

创建一个启用了 GitHub Actions 的 strict 预设项目:

```bash
azure-functions-scaffold new my-api --preset strict --python-version 3.12 --github-actions
```

在指定位置创建项目:

```bash
azure-functions-scaffold new my-api --destination ./sandbox
```

列出可用的模板:

```bash
azure-functions-scaffold templates
```

列出可用的预设:

```bash
azure-functions-scaffold presets
```

在现有的脚手架项目中添加新函数:

```bash
azure-functions-scaffold add http get-user --project-root ./my-api
azure-functions-scaffold add timer cleanup --project-root ./my-api
azure-functions-scaffold add queue sync-jobs --project-root ./my-api
azure-functions-scaffold add blob ingest-reports --project-root ./my-api
azure-functions-scaffold add servicebus process-events --project-root ./my-api
```

在不修改项目的情况下预览要添加的函数:

```bash
azure-functions-scaffold add servicebus process-events --project-root ./my-api --dry-run
```

## Generated Project

当前的 HTTP 模板生成的结构如下:

```text
my-api/
|- function_app.py
|- host.json
|- local.settings.json.example
|- pyproject.toml
|- .gitignore
|- .funcignore
|- README.md
|- app/
|  |- core/
|  |  `- logging.py
|  |- functions/
|  |  `- http.py
|  |- schemas/
|  |  `- request_models.py
|  `- services/
|     `- hello_service.py
`- tests/
   `- test_http.py
```

定时器、队列、Blob 和 Service Bus 模板遵循相同的高级布局，但会从针对特定触发器的函数、服务和测试模块开始。队列和 Blob 模板已准备好用于本地基于 Azurite 的开发，而 Service Bus 模板在生成时会带有开发连接占位符。

使用 `--with-openapi` 时，会额外注册三个端点:

- `/api/docs` — Swagger UI
- `/api/openapi.json` — OpenAPI 3.0 规范 (JSON)
- `/api/openapi.yaml` — OpenAPI 3.0 规范 (YAML)

使用 `--with-validation` 时，hello 端点会切换为使用 Pydantic 请求/响应模型 (`HelloRequest`, `HelloResponse`) 的 POST 方式。

使用 `--with-doctor` 时，生成的 Makefile 中会添加 `make doctor` 目标，并将 `azure-functions-doctor` 包含在项目依赖中。

所有生成的项目都包含 `azure-functions-logging`，通过 `setup_logging(format="json")` 和 `get_logger()` 进行结构化 JSON 日志记录。
## Development

使用 Makefile 命令作为标准入口点:

```bash
make install
make check-all
make docs
make build
```

## Documentation

- 完整文档: [yeongseon.github.io/azure-functions-scaffold](https://yeongseon.github.io/azure-functions-scaffold/)
- 根设计文档: `AGENT.md`, `DESIGN.md`, `PRD.md`
- 发布历史: `CHANGELOG.md`
- CLI 指南: `docs/cli.md`
- 模板规范: `docs/template_spec.md`
- 风格指南: `docs/style_guide.md`
- 路线图: `docs/roadmap.md`
- 贡献指南: `CONTRIBUTING.md`

## Disclaimer

本项目是一个独立的社区项目，不隶属于 Microsoft，也不受其认可或维护。

Azure 和 Azure Functions 是 Microsoft Corporation 的商标。

## License

MIT
