# Program that gets all the coins in the counter and divides them to reach a target amount in each counter.

COINS = [1, 5, 10, 20, 50, 100, 200]
coin_names = ["Shekels", "Fives", "Tens", "Twenties",
              "Fifties", "Hundreds", "Two Hundreds"]


def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("→ Please enter a valid integer.")


print("=== Dividing Money to Cashiers ===\n")
num_kupot = get_valid_int("How many cashiers are there? ")
target_per_kupa = get_valid_int("How much should be in each cashier? ")

total_coins = [0] * len(COINS)   # [שקלים, 5, 10, 20, 50, 100, 200]

for k in range(1, num_kupot + 1):
    print(f"\Cashier num {k}:")
    for i, coin in enumerate(COINS):
        cnt = get_valid_int(
            f"How many {coin_names[i]} ({coin} ₪) are in the cashier? ")
        total_coins[i] += cnt

total_money = sum(c * v for c, v in zip(total_coins, COINS))
needed = num_kupot * target_per_kupa
print(f"\Total money: {total_money:,} ₪")
print(f"Total required: {needed:,} ₪")

if total_money < needed:
    print("→ There is not enough money to reach the target in all cashiers!")
    exit()

remaining = total_coins[:]   # עותק – נוריד ממנו
result_per_kupa = []

for _ in range(num_kupot):
    current = [0] * len(COINS)
    remaining_value = target_per_kupa
    # מתחילים מהקטן לגדול
    for i in range(len(COINS)):
        value = COINS[i]
        # כמה מטבעות מהסוג הזה אפשר לשים?
        can_use = min(remaining_value // value, remaining[i])
        current[i] = can_use
        remaining[i] -= can_use
        remaining_value -= can_use * value

    result_per_kupa.append(current)

# חישוב עודף
leftover_value = sum(r * v for r, v in zip(remaining, COINS))
leftover_coins = remaining
print("\n" + "="*50)
print("Expected Distribution (each cashier reaches the target):")
for idx, coins_in_kupa in enumerate(result_per_kupa, 1):
    print(f"\nCashier {idx}:")
    for i, cnt in enumerate(coins_in_kupa):
        if cnt > 0:
            print(f"  {cnt:3} × {COINS[i]} ₪  ({coin_names[i]})")
print("\nLeftover that did not fit in any cashier:")
for i, cnt in enumerate(leftover_coins):
    if cnt > 0:
        print(f"  {cnt:3} × {COINS[i]} ₪  ({coin_names[i]})")
print(f"Total leftover: {leftover_value:,} ₪")
