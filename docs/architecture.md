# Architecture Overview

This microservice follows **Clean Architecture** with DDD principles.

## Layers

1. **Domain Layer**
   - Core entities, value objects, domain services
   - Pure Python, no external dependencies
   - Example: `Account`, `Money`

2. **Application Layer**
   - Use Cases / Interactors
   - Encapsulate business rules
   - Example: `CreateAccountUseCase`, `GetBalanceUseCase`

3. **Infrastructure Layer**
   - External systems, database, repositories
   - Example: `DjangoAccountRepository`

4. **Interfaces Layer**
   - REST API endpoints
   - Serializers, views, request validation

## Data Flow

```mermaid
graph TD
  API[REST API] --> UC[Use Cases]
  UC --> Repo[Repository]
  UC --> Domain[Entities & Value Objects]
  Repo --> DB[(Database)]