import os
import uuid
import click
import dataset

db = dataset.connect(os.getenv('DB_DSN', 'sqlite:///data.db'))
table = db["dummy_data"]


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    """Insert some dummy data in DB."""
    if len(table) > 0:
        click.echo("No need to import data, skipping.")
        return
    click.echo("Importing data...")
    for x in range(20):
        table.insert({
            "uuid": str(uuid.uuid4()),
            "slug": f"user-{x}"
        })
    click.echo("Done.")


if __name__ == "__main__":
    cli()
