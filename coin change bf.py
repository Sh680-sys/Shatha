import time

def coinChangeBruteForce(coins, amount):
   n = len(coins)
   
   def backtrack(index, remaining):
       if remaining == 0:
           return 0
       if remaining < 0 or index >= n:
           return float('inf')

       take = 1 + backtrack(index, remaining - coins[index])
       skip = backtrack(index + 1, remaining)
       return min(take, skip)

   result = backtrack(0, amount)
   return result if result != float('inf') else -1

coins = list(map(int, input("Enter coins (space-separated): ").split()))
amount = int(input("Enter amount: "))

start_time = time.time()
result = coinChangeBruteForce(coins, amount)
end_time = time.time()

print("Minimum number of coins required:", result)
print("Execution time:", end_time - start_time, "seconds")