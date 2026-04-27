# Monorepo Python 10 Apps

Monorepo chứa 10 ứng dụng full-stack (FastAPI + React + PostgreSQL) chạy đồng thời bằng **một lệnh**:

```bash
docker compose up --build
```

## Danh sách ứng dụng
1. Task Manager (`app-01-task-manager`)
2. Inventory System (`app-02-inventory-system`)
3. CRM System (`app-03-crm-system`)
4. Booking System (`app-04-booking-system`)
5. E-commerce Admin (`app-05-ecommerce-admin`)
6. Learning Management (`app-06-learning-management`)
7. Expense Tracker (`app-07-expense-tracker`)
8. Helpdesk Ticketing (`app-08-helpdesk-ticketing`)
9. Blog CMS (`app-09-blog-cms`)
10. Analytics Dashboard (`app-10-analytics-dashboard`)

## Quick start
```bash
cp .env.example .env
docker compose up --build
```

## URL truy cập
- Reverse proxy root: http://localhost
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

### Frontend
- http://localhost/app-01
- http://localhost/app-02
- http://localhost/app-03
- http://localhost/app-04
- http://localhost/app-05
- http://localhost/app-06
- http://localhost/app-07
- http://localhost/app-08
- http://localhost/app-09
- http://localhost/app-10

### API
- http://localhost/api/app-01
- http://localhost/api/app-02
- http://localhost/api/app-03
- http://localhost/api/app-04
- http://localhost/api/app-05
- http://localhost/api/app-06
- http://localhost/api/app-07
- http://localhost/api/app-08
- http://localhost/api/app-09
- http://localhost/api/app-10

## Demo account
- email: `admin@example.com`
- password: `admin123`

## Chạy riêng từng app
```bash
make app APP=app-01
```

## Migration + Seed
```bash
make migrate
make seed
```

## Test + lint
```bash
make test
make lint
```
