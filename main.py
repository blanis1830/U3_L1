#Blayne Hoy
#U3 Lab 1

def main(num):
  stack = []
  while num > 0:
    print(f"Recursing; num = {num}")
    stack.append(num)
    num -= 1
  print("\nBASE CASE REACHED\n")

  while stack:
    num = stack.pop()
    print(f"Returning; num = {num}")

if __name__ == "__main__":
  main(5)