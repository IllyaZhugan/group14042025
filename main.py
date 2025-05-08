from utils import (
    get_unique_values,
    get_division,
    validate_not_hashable,
    send_email_to_manager,
)

my_unique_values1 = get_unique_values("some_inerable")
my_unique_values2 = get_unique_values([56])
my_unique_values3 = get_unique_values({5, 6})


validate_not_hashable(5)
send_email_to_manager()

fraction = get_division(10, 0)
print(fraction)

