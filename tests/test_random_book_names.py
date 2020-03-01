from random_book_names.cli import CLI


def test_for_number_parameter():
    cli = CLI()
    args = cli.parse(["--number", "20"])
    assert args.number == 20
