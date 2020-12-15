"""
 I think that towards the end of that paper there's a discussion of an experiment
 they conduct. In it they lay out a bunch of constants, and their dimensionless equivalents.
 Could you create a separate Python module for physical constants?
 Make use of scipy.constants where you can, but use a simple class where you cant.
 Put references for values in the file, as part of the doc string.
 Include a number of different fuel types. This was what I was going to use:
 """


class Constant(float):
    def __new__(cls, value, units, description, doc):
        self = float.__new__(cls, value)
        self.units = units
        self.doc = doc
        return self


T_inf = Constant(300, 'K', 'Section 8 Page 152')  # Ambient Temperature
epsilon = Constant(0.03, 'Dimensionless', 'Section 8 Page 152')  # Non-dimensional inverse of the activation energy
E_A = Constant(83.68, 'kJ/mol', 'Section 8 Page 152')  # Activation Energy
A = Constant(10 ** 9, '1/s', 'Barrow GM.Physical Chemistry. McGraw-Hill: New York, 1966')  # pre-exponential factor
atmo_rho = Constant(1.1774, 'kg/m^3', 'Section 8 Page 152')  # Atmospheric Pressure
atmo_C = Constant(1.0057, '(kJ/kg)K', 'Section 8 Page 152')  # Atmospheric Specific Heat
atmo_k = Constant(0.024, '(W/m)K', 'Section 8 Page 152')  # Atmospheric Thermal Conductivity
k_p_C = Constant(10 ** (-5), 'm^2/s', 'Section 8 Page 152')  # Magnitude for the Thermal Diffusivity
H = Constant(15900, 'kcal/kg', 'Section 8 Page 152')  # Heat of Combustion of Cellulose
