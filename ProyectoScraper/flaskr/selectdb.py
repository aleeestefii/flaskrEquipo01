import click
from .db import get_db, close_db, init_app
from flask import Flask

app = Flask(__name__)
app.config['DATABASE'] = 'schema.sql'

init_app(app)

@click.command('select_all')
def select_all():
    db = get_db()

    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = db.execute(tables_query).fetchall()

    for table in tables:
        table_name = table['name']

        select_query = f'SELECT * FROM {table_name};'
        rows = db.execute(select_query).fetchall()

        click.echo(f"Datos de la tabla '{table_name}':")
        for row in rows:
            click.echo(dict(row))
        click.echo("\n")  

    close_db()

app.cli.add_command(select_all)

if __name__ == '__main__':
    app.run(debug=True)
