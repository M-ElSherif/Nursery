class Expense:

    def __int__(self, category: str, exp_type: str, cost: float, date: str, description: str = ""):
        self.category = category
        self.description = description
        self.exp_type = exp_type
        self.cost = cost
        self.date = date
