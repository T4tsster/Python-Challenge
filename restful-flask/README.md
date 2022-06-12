# Restful API with Flask

Restful API app that helps user manage finance, include 2 actions:
- Add income
- Get expense


## Test API

POST incomes request 
```
curl -X POST -H "Content-Type: application/json" -d '{ \"description\": \"lottery\", \"amount\": 1000.0}' http://localhost:5000/incomes
```