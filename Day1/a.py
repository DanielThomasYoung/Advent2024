with open("sample.txt", "r") as file:
  lines = file.readlines()
left = []
right = []
for line in lines:
    numbers = line.split()
