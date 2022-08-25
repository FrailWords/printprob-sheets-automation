import click
from .sheet import print_sheet


@click.command()
@click.option("--estc_number", prompt="estc_number", help="Search ESTC using this number")
@click.option("--uuid", prompt="uuid", help="UUID value to update")
def main(estc_number, uuid):
    print("hello")
    print_sheet(estc_number, uuid)


if __name__ == "__main__":
    main()
