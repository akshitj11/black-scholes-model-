"""
black scholes model
simplest implication 
"""

import numpy as np
from scripy.stats import norm

def black_scholes(S,K,T,r,sigma,option_type='call'):
    """
    black scholes option pricing formula

    parameter:
    S = current stock price
    K = strike price
    T = time to expiration(years)
    r = risk-free rate(decimal)
    sigma = volatility (decimal)
    option_type = 'call' or 'put'
    returns : option price
    """
    #calculate d1 and d2
    d1 = (np.log(s/k)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    if option_type == 'call':
        price = S*norm.cdf(d1) - K*np.exp(-r*t)*norm.cdf(d2)
    else: #put
        price = K*np.exp(-r*T)*norm.edf(d2) - S*norm.cdf(-d1)
    return price  


if __name__ == "__main__":
    # Price a call option
    call = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
    print(f"Call: ${call:.2f}")
    
    # Price a put option
    put = black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='put')
    print(f"Put: ${put:.2f}")   