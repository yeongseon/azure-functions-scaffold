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

다른 언어: [English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

운영 환경 중심의 Azure Functions Python v2 프로젝트를 위한 스캐폴딩 CLI입니다.

프로젝트 이름은 영문자나 숫자로 시작해야 하며, 영문자, 숫자, 하이픈(-), 언더스코어(_)만 사용할 수 있습니다.

## Scope

- Azure Functions Python **v2 프로그래밍 모델**
- 데코레이터 기반 `func.FunctionApp()` 애플리케이션
- 가볍지만 강력한 프로젝트 생성
- 대화형 부트스트랩, 프리셋 및 함수 확장

이 프로젝트는 기존 `function.json` 기반의 Python v1 프로그래밍 모델을 지원하지 **않습니다**.

## Features

- `azure-functions-scaffold new <project-name>`
- `azure-functions-scaffold new <project-name> --template http|timer|queue|blob|servicebus`
- `azure-functions-scaffold new --interactive`
- `azure-functions-scaffold new <project-name> --preset minimal|standard|strict`
- `azure-functions-scaffold new <project-name> --with-openapi` — OpenAPI 문서(Swagger UI, JSON, YAML) 포함
- `azure-functions-scaffold new <project-name> --with-validation` — 요청/응답 유효성 검사 포함
- `azure-functions-scaffold new <project-name> --with-openapi --with-validation` — 두 기능 모두 포함
- `azure-functions-scaffold new <project-name> --with-doctor` — azure-functions-doctor 헬스 체크 포함
- `azure-functions-scaffold add http <function-name>`
- `azure-functions-scaffold add timer <function-name>`
- `azure-functions-scaffold add queue <function-name>`
- `azure-functions-scaffold add blob <function-name>`
- `azure-functions-scaffold add servicebus <function-name>`
- 트리거별 내장 프로젝트 템플릿
- 생성된 결과물에 테스트, 린트, 패키징 설정 포함
- 서비스 중심의 소규모 애플리케이션 구조

## Installation

```bash
pip install azure-functions-scaffold
```

로컬 개발용:

```bash
git clone https://github.com/yeongseon/azure-functions-scaffold.git
cd azure-functions-scaffold
make install
```

## Usage

현재 디렉토리에 새로운 HTTP 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api
```

새로운 timer 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-job --template timer
```

로컬 Azurite 개발을 위한 queue-trigger 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-worker --template queue
```

로컬 Azurite 개발을 위한 blob-trigger 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-blob-worker --template blob
```

Service Bus-trigger 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-bus-worker --template servicebus
```

대화형으로 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new --interactive
```

대화형 프롬프트는 프로젝트 이름, 템플릿, 프리셋, Python 버전을 미리 검증합니다. 덕분에 생성 과정에서 오류가 발생하는 대신 프롬프트 단계에서 실수를 바로잡을 수 있습니다.

파일을 실제로 작성하지 않고 생성될 프로젝트를 미리 확인합니다:

```bash
azure-functions-scaffold new my-api --template queue --preset strict --dry-run
```

기존 스캐폴딩된 프로젝트를 명시적으로 교체합니다:

```bash
azure-functions-scaffold new my-api --overwrite
```

OpenAPI 문서(Swagger UI, JSON, YAML 엔드포인트)가 포함된 HTTP 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --with-openapi
```

요청/응답 유효성 검사가 포함된 HTTP 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --with-validation
```

OpenAPI와 유효성 검사가 모두 포함된 HTTP 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --with-openapi --with-validation
```

azure-functions-doctor 헬스 체크가 포함된 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --with-doctor
```

GitHub Actions가 활성화된 strict 프리셋 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --preset strict --python-version 3.12 --github-actions
```

특정 위치에 프로젝트를 생성합니다:

```bash
azure-functions-scaffold new my-api --destination ./sandbox
```

사용 가능한 템플릿 목록을 확인합니다:

```bash
azure-functions-scaffold templates
```

사용 가능한 프리셋 목록을 확인합니다:

```bash
azure-functions-scaffold presets
```

기존 스캐폴딩된 프로젝트에 새로운 함수를 추가합니다:

```bash
azure-functions-scaffold add http get-user --project-root ./my-api
azure-functions-scaffold add timer cleanup --project-root ./my-api
azure-functions-scaffold add queue sync-jobs --project-root ./my-api
azure-functions-scaffold add blob ingest-reports --project-root ./my-api
azure-functions-scaffold add servicebus process-events --project-root ./my-api
```

프로젝트를 수정하지 않고 추가될 함수를 미리 확인합니다:

```bash
azure-functions-scaffold add servicebus process-events --project-root ./my-api --dry-run
```

## Generated Project

현재 HTTP 템플릿은 다음과 같은 구조를 생성합니다:

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

timer, queue, blob, service bus 템플릿도 동일한 최상위 구조를 따르지만, 트리거 전용 함수, 서비스, 테스트 모듈로 시작합니다. queue와 blob 템플릿은 로컬 Azurite 기반 개발이 가능하도록 구성되어 있으며, service bus 템플릿은 개발용 연결 정보 자리표시자와 함께 생성됩니다.

`--with-openapi` 옵션을 사용하면 세 가지 엔드포인트가 추가로 등록됩니다:

- `/api/docs` — Swagger UI
- `/api/openapi.json` — OpenAPI 3.0 사양 (JSON)
- `/api/openapi.yaml` — OpenAPI 3.0 사양 (YAML)

`--with-validation` 옵션을 사용하면 hello 엔드포인트가 Pydantic 요청/응답 모델(`HelloRequest`, `HelloResponse`)을 사용하는 POST 방식으로 변경됩니다.

`--with-doctor` 옵션을 사용하면 생성된 Makefile에 `make doctor` 타겟이 추가되고, `azure-functions-doctor`가 프로젝트 의존성에 포함됩니다.

모든 생성된 프로젝트에는 `setup_logging(format="json")` 및 `get_logger()`를 통한 구조화된 JSON 로깅을 위해 `azure-functions-logging`이 포함됩니다.
## Development

입력 지점으로 Makefile 명령을 사용하세요:

```bash
make install
make check-all
make docs
make build
```

## Documentation

- 전체 문서: [yeongseon.github.io/azure-functions-scaffold](https://yeongseon.github.io/azure-functions-scaffold/)
- 루트 설계 문서: `AGENT.md`, `DESIGN.md`, `PRD.md`
- 릴리즈 히스토리: `CHANGELOG.md`
- CLI 가이드: `docs/cli.md`
- 템플릿 사양: `docs/template_spec.md`
- 스타일 가이드: `docs/style_guide.md`
- 로드맵: `docs/roadmap.md`
- 컨트리뷰션 가이드: `CONTRIBUTING.md`

## Disclaimer

본 프로젝트는 독립적인 커뮤니티 프로젝트이며, Microsoft와 제휴하거나, Microsoft가 보증하거나 유지 관리하지 않습니다.

Azure 및 Azure Functions는 Microsoft Corporation의 상표입니다.

## License

MIT
