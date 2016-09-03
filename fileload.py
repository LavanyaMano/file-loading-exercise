import json
with open('store_data.json', 'r') as data_file:
    data = json.loads(data_file.read())

class Fileload():

	def __init__(self):
		self.price =[]
		self.cost =[]
		self.sold =[]
		self.totalrev = 0
		self.totalcost= 0
		self.dept =[]
		self.dept_sold=[]
		self.eachdept = 0

	def listings(self):
		for item in data:
			self.price.append(item["price"])
			self.cost.append(item["cost_to_make"])
			self.sold.append(item["sold"])
			if item["department"] not in self.dept:
				self.dept.append(item["department"])
		return (self.price,self.cost,self.sold,self.dept)

	def sales(self):
		for i in data:
			self.totalrev += i["price"] * i["sold"]
			self.totalcost += i["cost_to_make"] * i["sold"]
		print("Total revenue is ${:.2f}".format(self.totalrev))
		print("Total profit is ${:.2f}".format(self.totalrev-self.totalcost))
		

	def sales_deptwise(self):
		print("Number sold by each department :\n")
		for item in data:
					for i in self.dept:
						if i== item["department"]:
							self.eachdept+= item["sold"]
					self.dept_sold.append(self.eachdept)
		for i in range(len(dept)):
			print("{} : {}nos".format(self.dept[i],self.dept_sold[i]))

	def best_dept(self):
		new_list = list(reversed(sorted(data,key=lambda k: k["sold"])))
		print("Top 10 best sellers are: \n")

		for i in range(10):
			print(new_list[i]["name"],":")
			print(new_list[i]["sold"])

	def high_price(self):
		self.listings()
		h=self.price.index(max(self.price))
		print("The most expensive product is {}: ${:.2f}".format(data[h]["name"], max(self.price)))

	def low_price(self):
		self.listings()
		l=self.price.index(min(self.price))
		print("The least expensive product is {}: ${:.2f}".format(data[l]["name"], min(self.price)))


store = Fileload()

print("-"*30)
store.sales()

print("-"*30)

store.high_price()
store.low_price()
print("-"*30)
store.best_dept()

print("-"*30)



