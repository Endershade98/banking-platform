# Layer Details

## Domain Layer
- Contains core business entities and value objects
- Pure logic without side effects
- Example files:
  - ``
  - `core/domain/value_objects/money.py`

## Application Layer
- Use Cases orchestrate domain logic
- Should not depend on frameworks
- Example files:
  - `core/application/use_cases/create_account.py`
  - `core/application/use_cases/get_balance.py`

## Infrastructure Layer
- Concrete implementations of repositories and services
- Example files:
  - `core/infrastructure/db/repositories/account_repository.py`

## Interfaces Layer
- API endpoints, serializers, request validation
- Example files:
  - `core/interfaces/rest/views.py`
  - `core/interfaces/rest/serializers.py`

## Testing Guidelines
- Unit tests for domain and application layers
- Integration tests for repository and API endpoints
- All tests should pass using `pytest -v`