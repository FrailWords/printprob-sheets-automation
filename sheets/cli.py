import click
from .sheet import update_uuid_in_sheet_for_estc_number, get_full_printer_name_for_short_name


@click.command()
@click.option("--estc_number", prompt="estc_number", help="Search ESTC using this number")
@click.option("--uuid", prompt="uuid", help="UUID value to update")
def main(estc_number, uuid):
    update_uuid_in_sheet_for_estc_number(estc_number, uuid)
    # print(get_full_printer_name_for_short_name('sroycroft'))


if __name__ == "__main__":
    main()
