# my_file = open("game.py")
# my_file.close()

# only reading
# with open("game.py", mode="r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)


# writing
# number = 5656
# with open("shop_plan.txt", mode="w", encoding="utf-8") as file:
#     for position in range(1, 10 +1):
#       file.write(f"data{position}\n")
# file.write("the end")

with open("shop_plan.txt", mode="a", encoding="utf-8") as file:
    for position in range(1, 10 +1):
      file.write(f"data{position}\n")
file.write("the end"\n)





