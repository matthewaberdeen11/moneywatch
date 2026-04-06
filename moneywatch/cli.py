import click

from moneywatch.db import init_db, add_transaction, get_transactions, delete_transaction, get_summary

@click.group()
def  cli():
    """MoneyWatch - Personal Finance Tracker"""
    init_db()

@cli.command()
@click.option("--amount", prompt = "amount", type = float)
@click.option("--category", prompt = "category of purchase")
@click.option("--description", prompt = "description of transaction")
@click.option("--type", prompt = "type of transaction", type=click.Choice(["income","expense"]))

def add(amount,category,description,type):
    add_transaction(amount,category,description,type)
    click.echo("Transaction added!")

@cli.command("list")
def list_transactions():
    transactions = get_transactions()
    for row in transactions:
        id, amount, category, description, type, date = row
        click.echo(f'#{id} | {type} | ${amount:.2f} | {category}| {description} | {date}')
    
@cli.command()
@click.argument("transaction_id", type=int)
def delete(transaction_id):
    delete_transaction(transaction_id)
    click.echo("Transaction Deleted!")

@cli.command("summary")
def transactions_summary():
    summary = get_summary()
    total_income = 0
    total_expense = 0
    for rows in summary:
        type, category, total = rows
        if type == "income":
            total_income = total_income + total
        elif type == "expense":
            total_expense = total_expense + total
        click.echo(f'{type} | {category} | {total:.2f}')

    click.echo(f'Total income: {total_income:.2f} \n Total expense: {total_expense:.2f} \n Net Balance: {total_income - total_expense:.2f}')
