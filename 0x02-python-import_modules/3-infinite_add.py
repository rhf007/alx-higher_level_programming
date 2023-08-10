#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv) - 1
argsum = 0
for i in range(n):
    argsum += int(sys.argv[i + 1])
print(argsum)
