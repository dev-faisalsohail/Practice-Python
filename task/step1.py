alpha = 37        # 37 = 100101 (binary)
beta  = 58        # 58 = 111010 (binary)

print("alpha =", alpha, "binary =", bin(alpha))
print("beta  =", beta, "binary =", bin(beta))
print("")

# ---------------------------
# Step 1: Addition (alpha + beta)

xor1   = alpha ^ beta
carry1 = (alpha & beta) << 1
print("Addition Step 1 -> xor1 =", xor1, bin(xor1), ", carry1 =", carry1, bin(carry1))

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1
print("Addition Step 2 -> xor2 =", xor2, bin(xor2), ", carry2 =", carry2, bin(carry2))

xor3   = xor2 ^ carry2
carry3 = (xor2 & carry2) << 1
print("Addition Step 3 -> xor3 =", xor3, bin(xor3), ", carry3 =", carry3, bin(carry3))

sum_result = xor3 ^ carry3
print("Final Sum =", sum_result, bin(sum_result))
print("")


# ---------------------------
# Step 2: Subtraction (alpha - beta)
# پہلا step: -beta نکالیں

not_beta = ~beta
print("~beta =", not_beta, bin(not_beta))

xor1   = not_beta ^ 1
carry1 = (not_beta & 1) << 1
print("NegBeta Step 1 -> xor1 =", xor1, bin(xor1), ", carry1 =", carry1, bin(carry1))

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1
print("NegBeta Step 2 -> xor2 =", xor2, bin(xor2), ", carry2 =", carry2, bin(carry2))

neg_beta = xor2 ^ carry2
print("Final -beta =", neg_beta, bin(neg_beta))
print("")


# اب alpha + (-beta)

xor1   = alpha ^ neg_beta
carry1 = (alpha & neg_beta) << 1
print("Sub Step 1 -> xor1 =", xor1, bin(xor1), ", carry1 =", carry1, bin(carry1))

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1
print("Sub Step 2 -> xor2 =", xor2, bin(xor2), ", carry2 =", carry2, bin(carry2))

diff_result = xor2 ^ carry2
print("Final Difference =", diff_result, bin(diff_result))
