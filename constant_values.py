class Constant(float):
    def __new__(cls, value, units, description, doc):
        self = float.__new__(cls, value)
        self.units = units
        self.doc = doc
        return self


# Constants with units
T_inf = Constant(300, 'K', 'Section 8 Page 152')  # Ambient Temperature
E_A = Constant(83.68, 'kJ/mol', 'Section 8 Page 152')  # Activation Energy
A = Constant(10 ** 9, '1/s', 'Barrow GM.Physical Chemistry. McGraw-Hill: New York, 1966')  # pre-exponential factor
rho = Constant(1.1774, 'kg/m^3', 'Section 8 Page 152')  # Atmospheric Pressure
C = Constant(1.0057, '(kJ/kg)K', 'Section 8 Page 152')  # Atmospheric Specific Heat
k = Constant(0.024, '(W/m)K', 'Section 8 Page 152')  # Atmospheric Thermal Conductivity
k_p_C = Constant(10 ** (-5), 'm^2/s', 'Section 8 Page 152')  # Magnitude for the Thermal Diffusivity
H = Constant(15900, 'kcal/kg', 'Section 8 Page 152')  # Heat of Combustion of Cellulose
# Note: in the paper they set heat of combustion q s.t. q = H*Y_0 / (C * T_inf) = 1

# Dimensionless constants
epsilon = Constant(0.03, 'Dimensionless', 'Section 8 Page 152')  # Non-dimensional inverse of the activation energy
alpha = Constant(10 ** (-3), 'Dimensionless', 'Section 8 Page 153')
t_0 = Constant(8987, 's', 'Section 8 Page 152')  # Characteristic temporal magnitude
l_0 = Constant(0.3, 'm', 'Section 8 Page 152')  # Characteristic spatial magnitude
Kappa = Constant(0.1, 'Dimensionless', 'Section 8 Page 153')
w_x = Constant(300, 'Dimensionless', 'Section 8 Page 153')
w_y = Constant(300, 'Dimensionless', 'Section 8 Page 153')

# Fuel models go below
# Each fuel model will have a density, specific heat, and thermal conductivity constant
