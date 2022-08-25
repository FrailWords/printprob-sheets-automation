import click
from .sheet import update_uuid_in_sheet_for_estc_number


@click.command()
@click.option("--estc_number", prompt="estc_number", help="Search ESTC using this number")
@click.option("--uuid", prompt="uuid", help="UUID value to update")
def main(estc_number, uuid):
    update_uuid_in_sheet_for_estc_number(estc_number, uuid)


if __name__ == "__main__":
    main()
