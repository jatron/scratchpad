r = 0.05
tax_rate = 0.3
one_year_medical_expenses = 350
first_year_fsa_contribution = 500

# In a given year:
# take_home_pay_no_fsae                     =                      salary * (1 - tax_rate) - one_year_medical_expenses
# take_home_pay_fsa                         = (salary - fsa_contribution) * (1 - tax_rate)
# take_home_pay_no_fsae - take_home_pay_fsa = - one_year_medical_expenses + fsa_contribution * (1 - tax_rate)

def npv_no_fsa(years):
	# Greater FSA contribution on the first year
	npv = - one_year_medical_expenses + first_year_fsa_contribution * (1 - tax_rate)
	for i in range(1, years):
		npv += (- one_year_medical_expenses + one_year_medical_expenses * (1 - tax_rate)) / (1 + r)**i
	return npv

my_years = 10
print("No FSA: ", npv_no_fsa(my_years))


def jorge_no_fsa(years, salary):
	npv = 0
	for i in range(years):
		npv += (salary * (1 - tax_rate) - one_year_medical_expenses) / (1 + r)**i
	return npv

def jorge_fsa(years, salary):
	# Greater FSA contribution on the first year
	npv = (salary - first_year_fsa_contribution) * (1 - tax_rate)
	for i in range(1, years):
		npv += ((salary - one_year_medical_expenses) * (1 - tax_rate)) / (1 + r)**i
	return npv

# You'll notice that the value of my_salary doesn't make a difference
my_salary = 500000
print("No FSA: ", jorge_no_fsa(my_years, my_salary) - jorge_fsa(my_years, my_salary))
