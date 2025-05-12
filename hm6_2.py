seconds = int(input())

day_sec = 24 * 60 * 60
hour_sec = 60 * 60
minute_sec = 60

days, remaining = divmod(seconds, day_sec)
hours, remaining = divmod(remaining, hour_sec)
minutes, secs = divmod(remaining, minute_sec)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

result = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"


print(result)

