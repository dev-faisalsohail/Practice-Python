# Python script to demonstrate command line arguments
import sys

# sys.argv contains the list of command line arguments
print("Number of arguments:", len(sys.argv))
print("Arguments:", sys.argv)


n = len(sys.argv)
print("Total arugments passed:", n)
print("\nName of Python script:", sys.argv[0]) # name of the current script

print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")