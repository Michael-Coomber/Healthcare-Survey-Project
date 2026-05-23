class User:

    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def to_dict(self):
        return {
            "Age": self.age,
            "Gender": self.gender,
            "Income": self.income,
            "Utilities": self.expenses.get("utilities", 0),
            "Entertainment": self.expenses.get("entertainment", 0),
            "School Fees": self.expenses.get("school_fees", 0),
            "Shopping": self.expenses.get("shopping", 0),
            "Healthcare": self.expenses.get("healthcare", 0)
        }