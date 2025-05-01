import decimal
import logging
from importlib.metadata import requires

from pywebio.input import slider, FLOAT, NUMBER

from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

import shop_clients

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)
CHEESE_PRICE = decimal.Decimal(286.3)
POTATO_PRICE = decimal.Decimal(40)

user_id = pw_input('Enter your ID', requires=True)
user_id = user_id.strip()

# HEADER
put_html("<h1>Welcome to our shop</h1>")

if user_id in shop_clients.CLIENTS or shop_clients.OPEN_DOOR_DAY:
else:
    put_error("Wrong ID. Please register")
    new_client_id = pw_input("Enter your ID").strip()
    shop_clients.CLIENTS.append(new_client_id)
    # put_success(str(shop_clients.CLIENTS))
    registered_users = '\n'.join(shop_clients.CLIENTS)
    put_success(str(registered_users))


logging.debug("debug")
logging.info("info")

# INPUT SECTION

cheese_weight = slider(
    "Cheese", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True
)
cheese_weight = decimal.Decimal(cheese_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

potato_weight = pw_input("Potato", type=NUMBER, required=True, min=0, max=10, value=3)
potato_weight = decimal.Decimal(potato_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"{potato_weight=}")

cheese_cost = (CHEESE_PRICE * cheese_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
potato_cost = (POTATO_PRICE * potato_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = cheese_cost + potato_cost
put_success(
    f"Total cost: \ncheese_cost\t{cheese_cost} \npotato_cost\t{potato_cost} \ntotal_cost\t{total_cost}"
)

