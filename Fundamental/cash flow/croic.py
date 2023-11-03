# Cash Return on Invested Capital (CROIC)
# ---------------------------------------
# Overview:
# CROIC measures the cash returns generated by a company on its invested capital. 
# It gives insight into the efficiency of a company's operations in terms of cash generation. 
# By focusing on cash returns instead of earnings, CROIC can provide a clearer picture of 
# how effectively a company is using its capital to generate real, tangible returns.
#
# Desired Value:
# A higher CROIC is generally favorable as it indicates that the company is efficiently 
# generating cash returns on its invested capital. However, it's essential to compare CROIC 
# values across the industry to get a relative understanding of a company's performance.

# Function to Calculate Cash Return on Invested Capital
def calculate_croic(free_cash_flow, invested_capital):
    """Calculate the Cash Return on Invested Capital."""
    if invested_capital == 0:
        raise ValueError("Invested capital should not be zero to calculate the CROIC.")
    return free_cash_flow / invested_capital

# Hardcoded values for the company
free_cash_flow_company = 45.00  # Company's Free Cash Flow, e.g., $45 million
invested_capital_company = 300.00  # Company's invested capital, e.g., $300 million

# Hardcoded values for industry average
free_cash_flow_industry_avg = 40.00  # Industry average Free Cash Flow, e.g., $40 million
invested_capital_industry_avg = 320.00  # Industry average invested capital, e.g., $320 million

croic_company = calculate_croic(free_cash_flow_company, invested_capital_company) * 100  # Convert to percentage
croic_industry_avg = calculate_croic(free_cash_flow_industry_avg, invested_capital_industry_avg) * 100  # Convert to percentage

# Output
print(f"Company's Free Cash Flow: ${free_cash_flow_company:.2f} million")
print(f"Company's Invested Capital: ${invested_capital_company:.2f} million")
print(f"Company's Cash Return on Invested Capital (CROIC): {croic_company:.2f}%")

print(f"\nIndustry Average Free Cash Flow: ${free_cash_flow_industry_avg:.2f} million")
print(f"Industry Average Invested Capital: ${invested_capital_industry_avg:.2f} million")
print(f"Industry Average Cash Return on Invested Capital (CROIC): {croic_industry_avg:.2f}%\n")

# Interpretation
if croic_company > croic_industry_avg:
    print("The company's CROIC is above the industry average, suggesting more efficient cash generation relative to peers. Potential factors influencing this might include:")
    print("- Superior operational efficiencies leading to higher cash generation.")
    print("- Prudent capital allocation decisions that yield higher returns.")
    print("- Effective management of working capital.")
    print("- Lower capital expenditures relative to cash flows, leading to higher free cash flow.")
    
elif croic_company == croic_industry_avg:
    print("The company's CROIC aligns with the industry average, indicating it's generating cash returns similar to its peers. This can suggest:")
    print("- Standard industry practices in capital allocation and operational management.")
    print("- Consistent return patterns relative to industry norms.")
    print("- No significant outliers in terms of investments or operational costs impacting cash generation.")
    
else:
    print("The company's CROIC is below the industry average, raising some concerns about its efficiency in cash generation compared to peers. Potential areas of concern might be:")
    print("- High capital expenditures relative to cash flows, lowering free cash flow.")
    print("- Potential inefficiencies in operations leading to lower cash generation.")
    print("- Recent significant investments or acquisitions that have yet to yield returns.")
    print("- Challenges in managing working capital efficiently.") 
