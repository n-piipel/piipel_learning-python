import json

with open("./telnum/results/tel_spider.json") as f:
    nums = json.load(f)

result = set()

for num in nums:
    for i in num['tel_num']:
        if i:
            result.add(i)

result = list(sorted(result))

with open('tel_num.txt', 'w') as f:
    for i in result:
        f.write(i + '\n')
