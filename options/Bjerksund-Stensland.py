# Bjerksund-Stensland American Option Pricing Model
# ------------------------------------------------
# Overview:
# This script calculates the price of an American option using the Bjerksund-Stensland model.
# The model provides a numerical approximation for the valuation of American-style options, 
# which can be exercised before expiration. It is an extension to the more commonly known Black-Scholes model
# but tailored for early exercise features.
#
# Desired Value:
# In the realm of options trading, the goal is generally to buy options at a low price and sell at a high price
# for buyers, and vice versa for sellers. A higher option price is usually beneficial for sellers, 
# while a lower option price is more favorable for buyers.

import math
from scipy.stats import norm

def BjerksundStensland(S, K, r, q, T, sigma, option_type="call"):
    def alpha(phi):
        return (-(phi-1)*K) / (1 - math.exp(-r * T))

    def beta(phi):
        if phi == 1:
            return float('inf')  # or some other large number
        return (phi / (phi - 1)) * S * math.exp((r - q) * T)
    
    def beta_star(phi):
        return max(beta(phi), alpha(phi))
    
    def I(phi):
        kappa = 2 * r / ((sigma ** 2) * (1 - math.exp(-r * T)))
        lambda_ = -(r - q + ((sigma ** 2) / 2) * phi * math.exp((r - q) * T)) / (sigma ** 2 * (1 - math.exp((r - q) * T)))
        d1 = -(math.log(S / K) + (beta(phi) - alpha(phi)) * (sigma ** 2 * T / 2)) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        return K * (1 - norm.cdf(d1)) - lambda_ * S * (1 - norm.cdf(d2))

    if option_type == "call":
        if S >= K:
            return max(S - K, 0)
        
        I_star = I(1)
        
        if S >= I_star:
            return max(S - K, 0)
        
        phi = 1
        b_star = beta_star(phi)
        
        return (alpha(1) - S + (beta(1) - alpha(1)) * ((1 - math.exp(-r * T)) / (r * T)) * (S / b_star) ** phi)
    
    elif option_type == "put":
        return BjerksundStensland(K, S, r, q, T, sigma, "call") - S + K * math.exp(-r * T)

def main():
    # Hard-coded values
    S = 11.32       # Current stock price
    K = 9.0       # Strike price
    days_to_expiry = 116
    T = days_to_expiry / 365.0  # Convert days to years
    r = 1.7702        # Risk-free rate (e.g., 5.0 for 5%)
    q = 5.5        # Dividend yield (e.g., 2.0 for 2%)
    sigma = 0.4695     # Volatility
    option_type = "call"  # Option type ('call' or 'put') # DEBUG: only 'put' gives an output
    
    # Convert r and q to percentage values for calculations
    r /= 100.0
    q /= 100.0
    
    option_price = BjerksundStensland(S, K, r, q, T, sigma, option_type)
    
    if option_price is not None:
        print(f"The Bjerksund-Stensland {option_type} option price is: ${option_price:.2f}")
    else:
        print(f"The {option_type} option price could not be calculated.")
    
    # Factors Influencing Output
    print(f"\nFactors that might influence the {option_type} option output:")
    
    if S > K:
        print(f"  - Stock Price (S): The stock is currently trading above the strike price.")
        print(f"    - Good for call options.")
        print(f"    - Bad for put options.")
    else:
        print(f"  - Stock Price (S): The stock is currently trading below the strike price.")
        print(f"    - Bad for call options.")
        print(f"    - Good for put options.")
    
    if r > q:
        print(f"  - Risk-Free Rate vs Dividend Yield: The risk-free rate is higher than the dividend yield.")
        print(f"    - Good for call options.")
        print(f"    - Bad for put options.")
    else:
        print(f"  - Risk-Free Rate vs Dividend Yield: The dividend yield is higher than the risk-free rate.")
        print(f"    - Bad for call options.")
        print(f"    - Good for put options.")
    
    if sigma > 0.2:
        print(f"  - Volatility (sigma): The stock is highly volatile.")
        print(f"    - Good for both call and put options.")
    else:
        print(f"  - Volatility (sigma): The stock has low volatility.")
        print(f"    - Bad for both call and put options.")
    
    if T > 1:
        print(f"  - Time to Expiry (T): The option has a longer time until expiration.")
        print(f"    - Good for both call and put options.")
    else:
        print(f"  - Time to Expiry (T): The option has a shorter time until expiration.")
        print(f"    - Bad for both call and put options.")
    
if __name__ == "__main__":
    main()
