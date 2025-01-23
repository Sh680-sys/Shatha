import time

def coinChange(coins, amount):
    if amount < 1:
        return 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != float('inf') else -1

def get_user_input():
    coins = list(map(int, input("Enter the coins (separated by spaces): ").split()))
    amount = int(input("Enter the target amount: "))
    return coins, amount

if __name__ == "__main__":
    coins, amount = get_user_input()
    start_time = time.time()
    result = coinChange(coins, amount)
    end_time = time.time()
    if result == -1:
        print("It is not possible to form the amount using the given coins.")
    else:
        print("Minimum number of coins required:", result)
    print("Execution time:", end_time - start_time, "seconds")