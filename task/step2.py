# Binary arithmetic using bitwise operations (no loops/functions)

alpha = 37  # 100101 (binary)
beta = 58   # 111010 (binary)

print(f"alpha = {alpha:2d} | binary = {bin(alpha)}")
print(f"beta  = {beta:2d} | binary = {bin(beta)}")
print("-" * 50)

# ADDITION: alpha + beta
print("ADDITION (alpha + beta):")

# Step 1
xor_sum = alpha ^ beta
carry = (alpha & beta) << 1
print(f"Step 1: xor = {xor_sum:2d} {bin(xor_sum):>8s} | carry = {carry:2d} {bin(carry):>8s}")

# Step 2
xor_sum, carry = xor_sum ^ carry, (xor_sum & carry) << 1
print(f"Step 2: xor = {xor_sum:2d} {bin(xor_sum):>8s} | carry = {carry:2d} {bin(carry):>8s}")

# Step 3
xor_sum, carry = xor_sum ^ carry, (xor_sum & carry) << 1
print(f"Step 3: xor = {xor_sum:2d} {bin(xor_sum):>8s} | carry = {carry:2d} {bin(carry):>8s}")

# Final result
addition_result = xor_sum ^ carry
print(f"RESULT: {addition_result} {bin(addition_result)}")
print()

# SUBTRACTION: alpha - beta
print("SUBTRACTION (alpha - beta):")

# First: Calculate -beta (two's complement)
not_beta = ~beta & 0xFFFFFFFF  # Mask to handle Python's unlimited precision
print(f"~beta = {not_beta} {bin(not_beta)}")

# Add 1 to get two's complement
xor_neg = not_beta ^ 1
carry_neg = (not_beta & 1) << 1
print(f"Step 1: xor = {xor_neg} | carry = {carry_neg}")

xor_neg, carry_neg = xor_neg ^ carry_neg, (xor_neg & carry_neg) << 1
print(f"Step 2: xor = {xor_neg} | carry = {carry_neg}")

neg_beta = xor_neg ^ carry_neg
print(f"-beta = {neg_beta} {bin(neg_beta)}")
print()

# Now: alpha + (-beta)
print("Adding alpha + (-beta):")

xor_sub = alpha ^ neg_beta
carry_sub = (alpha & neg_beta) << 1
print(f"Step 1: xor = {xor_sub} | carry = {carry_sub}")

xor_sub, carry_sub = xor_sub ^ carry_sub, (xor_sub & carry_sub) << 1
print(f"Step 2: xor = {xor_sub} | carry = {carry_sub}")

subtraction_result = xor_sub ^ carry_sub
print(f"RESULT: {subtraction_result} {bin(subtraction_result)}")

print("-" * 50)
print(f"Verification: {alpha} + {beta} = {alpha + beta} (calculated: {addition_result})")
print(f"Verification: {alpha} - {beta} = {alpha - beta} (calculated: {subtraction_result & 0xFFFFFFFF})")