"""
Analytical Chemistry & Formulation Calculator
Calculates molarity, stock dilutions, and molecular weights for pharmaceutical compounds.
"""

# 1. Ascorbic Acid Standard Solution Molarity
mass_g = 4.5
molar_mass_ascorbic = 176.12  # g/mol
volume_L = 0.25

moles = mass_g / molar_mass_ascorbic
molarity = moles / volume_L
print(f"Ascorbic Acid Molarity: {molarity:.4f} M")

# 2. Stock Solution Dilution (C1 * V1 = C2 * V2)
c1_ppm = 100.0
c2_ppm = 15.0
v2_mL = 50.0

v1_mL = (c2_ppm * v2_mL) / c1_ppm
print(f"Required Stock Volume (V1): {v1_mL:.2f} mL")

# 3. Molar Mass of Nifedipine (C17H18N2O6)
atomic_weights = {"C": 12.011, "H": 1.008, "N": 14.007, "O": 15.999}
mw_nifedipine = (
    17 * atomic_weights["C"]
    + 18 * atomic_weights["H"]
    + 2 * atomic_weights["N"]
    + 6 * atomic_weights["O"]
)
print(f"Nifedipine Molecular Weight: {mw_nifedipine:.2f} g/mol")
