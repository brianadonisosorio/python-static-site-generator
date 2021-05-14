import typer

from ssg.site import Site

def main(source="contnet", dest="dist"):
    config = {
        "source": source,
        "dest": dest,
    }

    Site(**config).build()

typer.run(main)


