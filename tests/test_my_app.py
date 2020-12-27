from src.my_app import main, square, __version__
from unittest.mock import Mock

# To test the entire project and print output, run this from the root directory:
# python -m pytest -s


def setup():
    # This should execute at the start of each test.
    print("Executing Setup")


def teardown():
    # This should execute at the end of each test.
    print("Executing Teardown")


# To test a specific function...
# python -m pytest -s tests/test_my_app.py::test_app_square
def test_app_square():
    y = square(5)
    assert y == 25


# To test a specific function...
# python -m pytest -s tests/test_my_app.py::test_app_main
def test_app_main():

    # This is how we can 'fake' the input/functionality of dependant modules.

    # Mock the arguments.
    mock_args = Mock()
    mock_args.version = True
    mock_args.square = 0

    # Mock the parser.
    mock_parser = Mock()
    mock_parser.add_argument = Mock()
    mock_parser.parse_args = Mock(return_value=mock_args)

    # If we call main() with a version argument, it should be returned.
    returned_version = main(mock_parser)
    assert __version__ == returned_version
