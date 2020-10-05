# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:45:29 2020

@author: aksha
"""
total_cost = int(input("Total cost for which you want to save="))

annual_salary = int(input("Enter your salary="))

semi_annual_raise = int(input("Enter your semi-annual raise as a percentage="))

portion_down_payement = int(input("percentage of total cost your is the down-payement="))

rate_of_interest = int(input("rate of interest in which you made an investment="))

portion_saved = int(input("percentage of your montly salary you want to save="))


def month_of_saving(total_cost,annual_salary,portion_down_payement,rate_of_interest,portion_saved,semi_annual_raise): 
    monthly_salary = annual_salary/12
    rate_of_interest = rate_of_interest/100
    portion_saved = portion_saved/100
    portion_down_payement = portion_down_payement/100
    semi_annual_raise = semi_annual_raise/100
    
    
    down_payement_given = portion_down_payement * total_cost
    
    current_saving = 0
    m=0
    while current_saving <= down_payement_given:
        current_saving += ((portion_saved * monthly_salary) + (current_saving *(rate_of_interest/12)))
        #print(current_saving)
        m += 1
        if m%6 ==0 :
            monthly_salary += monthly_salary * semi_annual_raise
        
    return m

m= month_of_saving(total_cost, annual_salary,portion_down_payement,rate_of_interest,portion_saved,semi_annual_raise)
print(m)
