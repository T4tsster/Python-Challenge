from flask import Flask, jsonify, request
from sqlalchemy import false, true

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route("/incomes", methods=['GET', 'POST'])
def incomes_api():
    if request.method == 'GET':
        schema = IncomeSchema(many=True)
        incomes = schema.dump(
            filter(lambda t: t.type == TransactionType.INCOME, transactions)
        )
        return jsonify(incomes)
    else:
        income = IncomeSchema().load(request.get_json())
        transactions.append(income)
        return '',204


@app.route("/expenses", methods=['GET', 'POST'])
def expenses_api():
    if request.method == 'GET':
        schema = ExpenseSchema(many=true)
        expenses = schema.dump(
            filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
        )
        return jsonify(expenses)
    else:
        expense = ExpenseSchema().load(request.get_json())
        transactions.append(expense)
        return '',204


if __name__ == "__main__":
    app.run()