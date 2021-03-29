import numpy as np
from matplotlib import pyplot as plt

default_number_of_years = 10
default_initial_cash = 1000
default_currency_exchange_cost = 0.022
default_commission = 0.008
default_average_annual_return = 0.10
default_etf_expense_ratio = 0.0059
default_mutual_fund_expense_ratio_clp = 0.0119
default_mutual_fund_expense_ratio_usd = 0.02975
# Average investment income of iShares MSCI Chile ETF (2016 - 2020)
default_etf_distributions = (0.0210 + 0.0174 + 0.0155 + 0.0168 + 0.0220) / 5

def invest_usa(initial_cash, currency_exchange_cost, average_annual_return, etf_expense_ratio, number_of_years):
	value = initial_cash * (1 - currency_exchange_cost)
	value = value * ((1 + average_annual_return - etf_expense_ratio)**number_of_years)

	return value

def invest_chile_etf(initial_cash, commission, average_annual_return, etf_expense_ratio, etf_distributions, mutual_fund_expense_ratio, number_of_years):
	etf = initial_cash * (1 - commission * 1.19) * (1 - 0.01)
	mutual_fund = 0

	for i in range(number_of_years):
		etf *= (1 + average_annual_return - etf_expense_ratio - etf_distributions)
		mutual_fund *= (1 + average_annual_return - mutual_fund_expense_ratio)
		mutual_fund += etf * etf_distributions
		if (mutual_fund > 1000):
			etf += mutual_fund * (1 - commission)
			mutual_fund = 0

	return etf * (1 - commission) + mutual_fund

def invest_chile_mutual_fund(initial_cash, average_annual_return, mutual_fund_expense_ratio, number_of_years):
	return initial_cash * ((1 + average_annual_return - mutual_fund_expense_ratio)**number_of_years)

# Sweep number of years
number_of_years = np.arange(1, 21)
end_value_usa = np.zeros(20)
end_value_chile_etf = np.zeros(20)
end_value_chile_mutual_fund = np.zeros(20)
for i in range(20):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, number_of_years[i])
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, number_of_years[i])
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, number_of_years[i])
plt.figure(0)
plt.title("Sweep Number of Years")
plt.ylabel("End Value")
plt.plot(number_of_years, end_value_usa, 'b')
plt.plot(number_of_years, end_value_chile_etf, 'r')
plt.plot(number_of_years, end_value_chile_mutual_fund, 'g')

# Sweep initial cash
initial_cash = np.arange(0, 2000, 20)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(initial_cash[i], default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(initial_cash[i], default_commission, default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(initial_cash[i], default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(1)
plt.title("Sweep Initial Cash")
plt.ylabel("End Value")
plt.plot(initial_cash, end_value_usa, 'b')
plt.plot(initial_cash, end_value_chile_etf, 'r')
plt.plot(initial_cash, end_value_chile_mutual_fund, 'g')

# Sweep currency_exchange_cost
currency_exchange_cost = np.arange(0, 0.06, 0.0006)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, currency_exchange_cost[i], default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(2)
plt.title("Sweep Currency Exchange Cost")
plt.ylabel("End Value")
plt.plot(currency_exchange_cost, end_value_usa, 'b')
plt.plot(currency_exchange_cost, end_value_chile_etf, 'r')
plt.plot(currency_exchange_cost, end_value_chile_mutual_fund, 'g')

# Sweep commission
commission = np.arange(0, 0.016, 0.00016)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, commission[i], default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(3)
plt.title("Sweep Commission")
plt.ylabel("End Value")
plt.plot(commission, end_value_usa, 'b')
plt.plot(commission, end_value_chile_etf, 'r')
plt.plot(commission, end_value_chile_mutual_fund, 'g')

# Sweep average annual return
average_annual_return = np.arange(0, 0.10, 0.001)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, average_annual_return[i], default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, average_annual_return[i], default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, average_annual_return[i], default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(4)
plt.title("Sweep Average Annual Return")
plt.ylabel("End Value")
plt.plot(average_annual_return, end_value_usa, 'b')
plt.plot(average_annual_return, end_value_chile_etf, 'r')
plt.plot(average_annual_return, end_value_chile_mutual_fund, 'g')

# Sweep etf expense ratio
etf_expense_ratio = np.arange(0, 0.0118, 0.000118)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, etf_expense_ratio[i], default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, etf_expense_ratio[i], default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(5)
plt.title("Sweep ETF Expense Ratio")
plt.ylabel("End Value")
plt.plot(etf_expense_ratio, end_value_usa, 'b')
plt.plot(etf_expense_ratio, end_value_chile_etf, 'r')
plt.plot(etf_expense_ratio, end_value_chile_mutual_fund, 'g')

# Sweep mutual fund expense ratio (CLP)
mutual_fund_expense_ratio_clp = np.arange(0, 0.0238, 0.000238)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, mutual_fund_expense_ratio_clp[i], default_number_of_years)
plt.figure(6)
plt.title("Sweep Mutual Fund Expense Ratio (CLP)")
plt.ylabel("End Value")
plt.plot(mutual_fund_expense_ratio_clp, end_value_usa, 'b')
plt.plot(mutual_fund_expense_ratio_clp, end_value_chile_etf, 'r')
plt.plot(mutual_fund_expense_ratio_clp, end_value_chile_mutual_fund, 'g')

# Sweep mutual fund expense ratio (USD)
mutual_fund_expense_ratio_usd = np.arange(0, 0.0595, 0.000595)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, default_etf_expense_ratio, default_etf_distributions, mutual_fund_expense_ratio_usd[i], default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(7)
plt.title("Sweep Mutual Fund Expense Ratio (USD)")
plt.ylabel("End Value")
plt.plot(mutual_fund_expense_ratio_usd, end_value_usa, 'b')
plt.plot(mutual_fund_expense_ratio_usd, end_value_chile_etf, 'r')
plt.plot(mutual_fund_expense_ratio_usd, end_value_chile_mutual_fund, 'g')

# Sweep ETF Distributions
etf_distributions = np.arange(0, 0.03708, 0.0003708)
end_value_usa = np.zeros(100)
end_value_chile_etf = np.zeros(100)
end_value_chile_mutual_fund = np.zeros(100)
for i in range(100):
	end_value_usa[i] = invest_usa(default_initial_cash, default_currency_exchange_cost, default_average_annual_return, default_etf_expense_ratio, default_number_of_years)
	end_value_chile_etf[i] = invest_chile_etf(default_initial_cash, default_commission, default_average_annual_return, default_etf_expense_ratio, etf_distributions[i], default_mutual_fund_expense_ratio_usd, default_number_of_years)
	end_value_chile_mutual_fund[i] = invest_chile_mutual_fund(default_initial_cash, default_average_annual_return, default_mutual_fund_expense_ratio_clp, default_number_of_years)
plt.figure(8)
plt.title("Sweep ETF Distributions")
plt.ylabel("End Value")
plt.plot(etf_distributions, end_value_usa, 'b')
plt.plot(etf_distributions, end_value_chile_etf, 'r')
plt.plot(etf_distributions, end_value_chile_mutual_fund, 'g')

plt.show()
