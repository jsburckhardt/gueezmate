import pandas as pd


class ExpenseRecordExcel:
    def __init__(self, date, store, category, amount, exclude, description):
        self.date = date
        self.store = store
        self.category = category
        self.amount = amount
        self.exclude = exclude
        self.description = description
    
    def print_record(self):
        print(f"date: {self.date}")
        print(f"store: {self.store}")
        print(f"category: {self.category}")
        print(f"amount: {self.amount}")
        print(f"exclude: {self.exclude}")
        print(f"description: {self.description}")


df = pd.read_excel(
    "./src/import_data/try_expenses.xlsm",
    sheet_name="Expenses DB",
    header=9,
    usecols="J,Q:U",
    parse_dates=True,
)

a = df.to_dict()
for index in range(df.shape[0]):
    record = ExpenseRecordExcel(
        a["Date"][index],
        a["Store"][index],
        a["Category"][index],
        a["Amount"][index],
        a["Exclude in WE"][index],
        a["Description"][index],
    )
    record.print_record()