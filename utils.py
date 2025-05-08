from ctypes import HRESULT


def get_unique_values(
    some_inerable: list[str, bool, int, float] | str | set,
) -> set[str, bool, int, float]:
    unique_values = set(some_inerable)
    return unique_values


def get_division(dividend: int, divisor: int) -> int | float:
    """
    we return 0 if divisor 0 because of task #56565
    """
    if not divisor:
        return 0.0
    result = dividend / divisor
    return result


def send_email(recipient: str, email_body: str) -> None:
    print("sending email to {}...".format(recipient))


def send_email_to_manager() -> None:
    manager_email = "example@ukr.net"
    text = "bla bla"
    send_email(manager_email, text)


def validate_not_hashable(value) -> None:
    hash(value)
