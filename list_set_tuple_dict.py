# nums = [1, 2, 2, 3, 4, 4, 5]
# print(list(set(nums)))

# points = (10, 20)
# for point in points:
#     print (point)
# #points[0] = 30 #'tuple' object does not support item assignment
# #print (points)

# texts = "apple banana apple orange banana apple"
# texts = texts.split(" ")

# count = {}
# for text in texts:
#     if count.get(text) == None:
#         count[text] = 1
#     else:
#         count[text] = count[text]+1

# print(count)

# users = ["alice", "bob", "alice", "charlie"]
# users = set(users)
# dict = {}
# for user in users:
#     dict[user] = True
# print(dict)

# logins = ["alice", "bob", "alice", "charlie", "bob"]

# log_in_user = {}
# result = {}
# for user in logins:
#     result[user] = result.get(user, {"count": 0, "status": "inactive"})
#     result[user]["count"] += 1
#     if result[user]["count"] > 1:
#         result[user]["status"] = "active"

# print(result)


transactions = [
    {"user": "alice", "amount": 100},
    {"user": "bob", "amount": 50},
    {"user": "alice", "amount": 200}
]
new_data = {"user": "alice", "amount": 100}

modified_data = transactions.append(new_data)
print (transactions)

user_transaction_tracking = {}
for transaction in transactions:
    user = transaction["user"]
    print (user)
    user_transaction_tracking[user] = user_transaction_tracking.get(user,{"total":0, "transactions":0})
    user_transaction_tracking[user]["transactions"] += 1

for transaction in transactions:
    user = transaction["user"]
    user_transaction_tracking[user]["total"] += transaction["amount"]
print(user_transaction_tracking)

l = [4,5,3,3,2,1]
print (set(l))
s = {10, 1, 7, 3, 20}
print(s)