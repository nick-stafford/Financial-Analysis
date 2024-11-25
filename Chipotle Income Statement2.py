import requests
import matplotlib.pyplot as plt

api_key = 'JkDZAZaFAIcN4P9A6IjYhuxLKovdy4Qi'

company = "CMG"
years = 10 

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
income_statement = income_statement.json()


rev_10_years = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profit_10_years = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

plt.plot(rev_10_years, label = "Revenue")
plt.plot(profit_10_years, label = "Profit")
plt.legend(loc = "upper right")
plt.show()