import numpy as np

def gilbert_correlation(pressure, choke_size, C=15, n=0.546):
    """
    Estimate oil flow rate using Gilbert’s Correlation.
    Q = C * (P ^ n)
    :param pressure: Flowing wellhead pressure (psi)
    :param choke_size: Choke size (inches)
    :param C: Empirical coefficient (default 15 for oil)
    :param n: Empirical exponent (default 0.546 for oil)
    :return: Estimated oil flow rate (bbl/day)
    """
    return C * (pressure ** n) * choke_size

def gas_flow_rate(pressure, choke_size, Cg=3, ng=0.7):
    """
    Estimate gas flow rate using a modified Gilbert-like correlation.
    :param pressure: Flowing wellhead pressure (psi)
    :param choke_size: Choke size (inches)
    :param Cg: Empirical coefficient for gas (default 3)
    :param ng: Empirical exponent for gas (default 0.7)
    :return: Estimated gas flow rate (MSCF/day)
    """
    return Cg * (pressure ** ng) * choke_size

def water_flow_rate(oil_rate, water_cut):
    """
    Estimate water flow rate based on water cut.
    :param oil_rate: Estimated oil flow rate (bbl/day)
    :param water_cut: Water cut (fraction, e.g., 0.3 for 30%)
    :return: Estimated water flow rate (bbl/day)
    """
    return oil_rate * water_cut / (1 - water_cut)

# Example inputs
pressure = 1000  # psi
temperature = 150  # °F (not used in basic correlations)
choke_size = 0.5  # inches
water_cut = 0.3  # 30% water cut

# Calculating flow rates
oil_rate = gilbert_correlation(pressure, choke_size)
gas_rate = gas_flow_rate(pressure, choke_size)
water_rate = water_flow_rate(oil_rate, water_cut)

# Display results
print(f"Estimated Oil Flow Rate: {oil_rate:.2f} bbl/day")
print(f"Estimated Gas Flow Rate: {gas_rate:.2f} MSCF/day")
print(f"Estimated Water Flow Rate: {water_rate:.2f} bbl/day")