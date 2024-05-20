
import datetime

def get_upfront_fees(fee_percentage, amount_invested):
    return fee_percentage * amount_invested * 5

def get_membership_fee(amount_invested):
    if amount_invested > 50000:
        return 0
    return 3000

def get_yearly_fees(investment_date, fee_percentage, amount_invested, years):
    total_fees = []
    first_year_fee = (get_date_of_investment_date(investment_date) / get_days_in_year(investment_date)) * fee_percentage * amount_invested
    total_fees.append(first_year_fee)

    if is_before_threshold_year(investment_date):
        for year in range(2, years + 1):
            yearly_fee = fee_percentage * amount_invested
            total_fees.append(yearly_fee)    
    else:
        for year in range(2, years + 1):
            yearly_fee = (fee_percentage - get_percentage_year_value(year)) * amount_invested
            total_fees.append(yearly_fee)
      


    return total_fees


def get_percentage_year_value(year): 
    percentage_rates = {
        2: 0, 
        3: 0.002, 
        4: 0.005, 
        5: 0.01
    }
    if year in percentage_rates.keys():
        return percentage_rates[year]
    else:
        return 0.01

def get_date_of_investment_date(investment_date):
    end_year_date = datetime.date(investment_date.year, 12, 31)
    return (end_year_date - investment_date).days

def get_days_in_year(date):
    if is_before_threshold_year(date):
        return 365
    else:
        number_of_days_in_year = (datetime.date(date.year + 1 + 1, 1, 1) - datetime.date(date.year , 1, 1)).days
        return number_of_days_in_year

def is_before_threshold_year(date):
    threshold_date = datetime.date(2019, 4, 1)
    return date < threshold_date