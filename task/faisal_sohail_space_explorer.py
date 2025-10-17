# Step 1: 
alpha = 37
beta = 58

# Addition 
xor1   = alpha ^ beta
carry1 = (alpha & beta) << 1

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1

xor3   = xor2 ^ carry2
carry3 = (xor2 & carry2) << 1

sum_result = xor3  

#  Subtraction 

not_beta = ~beta

xor1   = not_beta ^ 1
carry1 = (not_beta & 1) << 1

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1

neg_beta = xor2 ^ carry2   

xor1   = alpha ^ neg_beta
carry1 = (alpha & neg_beta) << 1

xor2   = xor1 ^ carry1
carry2 = (xor1 & carry1) << 1

diff_result = xor2 ^ carry2  

print("Step 1: Sum =", sum_result, "Difference =", diff_result)

#  *** -------------------------- ***
# Step 2: 
red_signal = 110
green_signal = 220
blue_signal = 330

red_signal = red_signal + green_signal + blue_signal
green_signal = red_signal - (green_signal + blue_signal)
blue_signal = red_signal - (green_signal + blue_signal)
red_signal = red_signal - (green_signal + blue_signal)

print("Step 2: red =", red_signal, "green =", green_signal, "blue =", blue_signal)

#  *** -------------------------- ***
# Step 3: 
sensor_A = True
sensor_B = False
sensor_C = True

result = (sensor_A and sensor_B and not sensor_C) or \
         (sensor_A and sensor_C and not sensor_B) or \
         (sensor_B and sensor_C and not sensor_A)

print("Step 3: Exactly two sensors active:", result)
#  *** -------------------------- ***
# Step 4:
engine_power = 75
engine_power *= 4       # multiply by 4
engine_power //= 2      # integer divide by 2
engine_power ^= 15      # XOR with 15
engine_power &= 27      # AND with 27
engine_power += 10      # add 10
engine_power >>= 2      # right shift by 2

print("Step 4:Engine Power =", engine_power)

#  *** -------------------------- ***
# Step 5: 
alpha = 37
beta = 58
gamma = 21

step1 = alpha + beta
step2 = beta ^ gamma
step3 = step1 - step2
step4 = alpha | gamma
step5 = step3 * step4
denominator = beta & gamma

activation_code = (denominator and (step5 // denominator)) or None

print("Step 5: Final Activation Code =", activation_code)