from commons.string_utils import string_concat


def test_string_concat() -> None:
    result = string_concat('hello', 'world')
    assert result == 'helloworld'
