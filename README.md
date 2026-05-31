# Product Catalogue Backend Service

## Overview
This repository contains a microservice-based product catalogue backend for an e-commerce application. It enables administrators to manage products efficiently through a RESTful API and a synchronized administrative user interface. 

The project is built using strict **Test-Driven Development (TDD)** practices for backend stability and **Behavior-Driven Development (BDD)** workflows to ensure seamless end-to-end UI automation.

---

## Technology Stack
- **Backend Framework:** Flask (Python)
- **Database & ORM:** SQLAlchemy
- **Test Data Generation:** factory_boy
- **Unit Testing Framework:** PyTest / Unittest
- **BDD Automation Framework:** Behave
- **Browser Automation:** Selenium WebDriver

---

## API Endpoints & Features

The RESTful API supports complete CRUD operations along with advanced query parameters for searching and filtering:

| Method | Endpoint | Description | Query Parameters |
| :--- | :--- | :--- | :--- |
| **GET** | `/products` | List all products / Search products | `name`, `category`, `available` |
| **GET** | `/products/<int:id>` | Retrieve a single product by ID | None |
| **POST** | `/products` | Create a new product in the catalog | None |
| **PUT** | `/products/<int:id>` | Update an existing product's details | None |
| **DELETE** | `/products/<int:id>` | Remove a product from the database | None |

---

## Repository Structure & Core Components

- `service/routes.py` — Core API route implementations and query-filtering logic.
- `service/models.py` — Database schema models and CRUD helpers.
- `tests/factories.py` — Mock data generation factories using `factory_boy`.
- `tests/test_models.py` — Unit tests for isolating model-level behaviors.
- `tests/test_routes.py` — HTTP status code and response verification tests.
- `features/products.feature` — Gherkin syntax BDD acceptance criteria scenarios.
- `features/steps/` — Step definitions connecting Gherkin scenarios to backend data loading and Selenium UI testing.

---

## Getting Started

### 1. Installation
To set up your local environment and install all necessary dependencies, run:
```bash
make install
