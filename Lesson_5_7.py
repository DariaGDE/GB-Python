import json

profits = {}
with open('new_file_4.txt', 'r') as f:
    for line in f:
        profit = int(line.split()[-2]) - int(line.split()[-1])
        if profit > 0:
            profits[line.split()[0]] = profit
print(profits)
summary = 0
for value in profits.values():
    summary += value
new_list = [profits, {'summary':summary}]
print(new_list)

with open('profits.json', 'w') as f:
    json.dump(new_list, f)
