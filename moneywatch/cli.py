import click
from rich.console import Console
from rich.table import Table

console = Console()

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
    table = Table(title="Transactions")
    table.add_column("ID")
    table.add_column("Amount")
    table.add_column("Type")
    table.add_column("Category")
    table.add_column("Description")
    table.add_column("Date")

    for row in transactions:
        id, amount, category, description, type, date = row
        table.add_row(str(id),f"${amount:.2f}",type, category, description, date)
    
    console.print(table)
        
    
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
    table = Table(title = "Summary")
    table.add_column("Type")
    table.add_column("Category")
    table.add_column("Total")

    for rows in summary:
        type, category, total = rows
        if type == "income":
            total_income = total_income + total
        elif type == "expense":
            total_expense = total_expense + total
        table.add_row(type, category,f"${total:.2f}" )
    
    console.print(table)
    console.print(f"\nTotal Income: ${total_income:.2f}")
    console.print(f"Total Expenses: ${total_expense:.2f}")
    console.print(f"Net Balance: ${total_income - total_expense:.2f}")
