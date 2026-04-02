import click

from moneywatch.db import init_db, add_transaction, get_transactions

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
        click.echo(row)