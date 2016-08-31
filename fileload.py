import json
with open('store_data.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())



price =[]
cost =[]
sold =[]
totalrev = 0
totalcost= 0
dept =[]
dept_sold=[]
eachdept = 0




for item in data:
	price.append(item["price"])
	cost.append(item["cost_to_make"])
	sold.append(item["sold"])
	if item["department"] not in dept:
		dept.append(item["department"])

for i in data:
	totalrev += i["price"] * i["sold"]
	totalcost += i["cost_to_make"] * i["sold"]

for item in data:
	for i in dept:
		if i== item["department"]:
			eachdept+= item["sold"]
	dept_sold.append(eachdept)


print("-"*30)

print("Number sold by each department :")

for i in range(len(dept)):
	print("{} : {}nos".format(dept[i],dept_sold[i]))


h=price.index(max(price))
l=price.index(min(price))

print("-"*30)

print("Total revenue is ${:.2f}".format(totalrev))

print("Total profit is ${:.2f}".format(totalrev-totalcost))
print("-"*30)

print("The most expensive product is {}: ${:.2f}".format(data[h]["name"], max(price)))

print("The least expensive product is {}: ${:.2f}".format(data[l]["name"], min(price)))

print("-"*30)

new_list = sorted(data,key=lambda k: k["sold"])
print("Top 10 best sellers are: ")

for i in range(10):
	print(new_list[i]["name"])

