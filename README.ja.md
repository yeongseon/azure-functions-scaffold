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

他の言語: [English](README.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md)

運用を意識した Azure Functions Python v2 プロジェクトのためのスキャフォールディング CLI です。

プロジェクト名は、英数字で始まり、英数字、ハイフン（-）、アンダースコア（_）のみを使用する必要があります。

## Scope

- Azure Functions Python **v2 プログラミングモデル**
- デコレータベースの `func.FunctionApp()` アプリケーション
- 軽量ながら実用的なプロジェクト生成
- 対話型ブートストラップ、プリセット、関数の拡張

このプロジェクトは、従来の `function.json` を使用した Python v1 プログラミングモデルをサポートして**いません**。

## Features

- `azure-functions-scaffold new <project-name>`
- `azure-functions-scaffold new <project-name> --template http|timer|queue|blob|servicebus`
- `azure-functions-scaffold new --interactive`
- `azure-functions-scaffold new <project-name> --preset minimal|standard|strict`
- `azure-functions-scaffold new <project-name> --with-openapi` — OpenAPI ドキュメント (Swagger UI, JSON, YAML) を含める
- `azure-functions-scaffold new <project-name> --with-validation` — リクエスト/レスポンスのバリデーションを含める
- `azure-functions-scaffold new <project-name> --with-openapi --with-validation` — 両方の機能を組み合わせる
- `azure-functions-scaffold new <project-name> --with-doctor` — azure-functions-doctor ヘルスチェックを含める
- `azure-functions-scaffold add http <function-name>`
- `azure-functions-scaffold add timer <function-name>`
- `azure-functions-scaffold add queue <function-name>`
- `azure-functions-scaffold add blob <function-name>`
- `azure-functions-scaffold add servicebus <function-name>`
- トリガーごとの組み込みプロジェクトテンプレート
- 生成される成果物に含まれるテスト、リント、パッケージングのデフォルト設定
- サービス指向の小規模なアプリケーション構成

## Installation

```bash
pip install azure-functions-scaffold
```

ローカル開発用:

```bash
git clone https://github.com/yeongseon/azure-functions-scaffold.git
cd azure-functions-scaffold
make install
```

## Usage

現在のディレクトリに新しい HTTP プロジェクトを作成します:

```bash
azure-functions-scaffold new my-api
```

新しいタイマープロジェクトを作成します:

```bash
azure-functions-scaffold new my-job --template timer
```

ローカルの Azurite 開発用に queue-trigger プロジェクトを作成します:

```bash
azure-functions-scaffold new my-worker --template queue
```

ローカルの Azurite 開発用に blob-trigger プロジェクトを作成します:

```bash
azure-functions-scaffold new my-blob-worker --template blob
```

Service Bus-trigger プロジェクトを作成します:

```bash
azure-functions-scaffold new my-bus-worker --template servicebus
```

対話形式でプロジェクトを作成します:

```bash
azure-functions-scaffold new --interactive
```

対話型のプロンプトは、プロジェクト名、テンプレート、プリセット、Python バージョンを事前検証します。これにより、生成過程でエラーが発生する代わりに対話時に間違いを修正できます。

ファイルを書き込まずに生成されるプロジェクトをプレビューします:

```bash
azure-functions-scaffold new my-api --template queue --preset strict --dry-run
```

既存のスキャフォールディングされたプロジェクトを明示的に上書きします:

```bash
azure-functions-scaffold new my-api --overwrite
```

OpenAPI ドキュメント (Swagger UI, JSON, YAML エンドポイント) を含む HTTP プロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --with-openapi
```

リクエスト/レスポンスのバリデーションを含む HTTP プロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --with-validation
```

OpenAPI とバリデーションの両方を含む HTTP プロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --with-openapi --with-validation
```

azure-functions-doctor ヘルスチェックを含むプロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --with-doctor
```

GitHub Actions を有効にした strict プリセットプロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --preset strict --python-version 3.12 --github-actions
```

特定の場所にプロジェクトを作成します:

```bash
azure-functions-scaffold new my-api --destination ./sandbox
```

利用可能なテンプレートの一覧を表示します:

```bash
azure-functions-scaffold templates
```

利用可能なプリセットの一覧を表示します:

```bash
azure-functions-scaffold presets
```

既存のスキャフォールディングされたプロジェクトに新しい関数を追加します:

```bash
azure-functions-scaffold add http get-user --project-root ./my-api
azure-functions-scaffold add timer cleanup --project-root ./my-api
azure-functions-scaffold add queue sync-jobs --project-root ./my-api
azure-functions-scaffold add blob ingest-reports --project-root ./my-api
azure-functions-scaffold add servicebus process-events --project-root ./my-api
```

プロジェクトを変更せずに追加される関数をプレビューします:

```bash
azure-functions-scaffold add servicebus process-events --project-root ./my-api --dry-run
```

## Generated Project

現在の HTTP テンプレートは、次のような構造を生成します:

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

timer, queue, blob, service bus テンプレートも同様のレイアウトに従いますが、トリガー固有の関数、サービス、テストモジュールから始まります。queue と blob テンプレートはローカルの Azurite ベースの開発が可能になるように構成されており、service bus テンプレートは開発用接続情報のプレースホルダと共に生成されます。

`--with-openapi` オプションを使用すると、3 つのエンドポイントが追加で登録されます:

- `/api/docs` — Swagger UI
- `/api/openapi.json` — OpenAPI 3.0 仕様 (JSON)
- `/api/openapi.yaml` — OpenAPI 3.0 仕様 (YAML)

`--with-validation` オプションを使用すると、hello エンドポイントは Pydantic のリクエスト/レスポンスモデル (`HelloRequest`, `HelloResponse`) を使用する POST 方式に変更されます。

`--with-doctor` オプションを使用すると、生成された Makefile に `make doctor` ターゲットが追加され、`azure-functions-doctor` がプロジェクトの依存関係に含まれます。

すべての生成されたプロジェクトには、`setup_logging(format="json")` と `get_logger()` による構造化 JSON ロギングのために `azure-functions-logging` が含まれます。
## Development

エントリポイントとして Makefile コマンドを使用してください:

```bash
make install
make check-all
make docs
make build
```

## Documentation

- 全ドキュメント: [yeongseon.github.io/azure-functions-scaffold](https://yeongseon.github.io/azure-functions-scaffold/)
- ルート設計ドキュメント: `AGENT.md`, `DESIGN.md`, `PRD.md`
- リリース履歴: `CHANGELOG.md`
- CLI ガイド: `docs/cli.md`
- テンプレート仕様: `docs/template_spec.md`
- スタイルガイド: `docs/style_guide.md`
- ロードマップ: `docs/roadmap.md`
- コントリビューションガイド: `CONTRIBUTING.md`

## Disclaimer

本プロジェクトは独立したコミュニティプロジェクトであり、Microsoft と提携、承認、または維持されているものではありません。

Azure および Azure Functions は、Microsoft Corporation の商標です。

## License

MIT
