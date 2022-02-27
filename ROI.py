class ROIcalculator():
    def __init__ (self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment
    def ROI(self):
        cashflow = self.income-self.expenses
        NetProfit = self.income * 12 - self.expenses
        returnOfInv = (NetProfit/self.investment)*100
        print(f"Cash flow: ${cashflow}, Net Profit: ${NetProfit}, Return of investment: ${returnOfInv}")
income = int(input("What is your monthly income?: "))
expenses = int(input("What are your monthly expenses?: "))
investment = int(input("What is your investment?: "))

present = ROIcalculator(income, expenses, investment)
present.ROI()