import time

def coinChangeGreedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    remaining = amount
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            count += 1
    return count if remaining == 0 else -1

def get_user_input():
    coins = list(map(int, input("Enter the coins (separated by spaces): ").split()))
    amount = int(input("Enter the target amount: "))
    return coins, amount

if __name__ == "__main__":
    coins, amount = get_user_input()
    start_time = time.time()
    result = coinChangeGreedy(coins, amount)
    end_time = time.time()
    if result == -1:
        print("It is not possible to form the amount using the given coins.")
    else:
        print("Minimum number of coins required:", result)
    print("Execution time:", end_time - start_time, "seconds")
    