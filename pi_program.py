from mpmath import mp

def calculate_pi_chudnovsky(digits=100):
    mp.dps = digits  # Set the number of decimal places
    return mp.pi

# Example usage
print("Value of Pi (Chudnovsky):", calculate_pi_chudnovsky(1000000))
