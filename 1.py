"""
Advent of Code 2024
Day 1
Historian Hysteria
"""


with open("1_input.txt") as f:
  raw = f.read()
lines = raw.split("\n")
l1 = []
l2 = []
for line in lines:
  temp_line = line.split("   ")
  try:
    l1.append(temp_line[0])
    l2.append(temp_line[1])
  except:
    l1.remove("")
l1.sort()
l2.sort()


def p1():
  total = 0
  for i in range(len(l1)):
    total += abs(int(l1[i]) - int(l2[i]))
  
  print(total)


def p2():
  similarity = 0
  m2 = {}
  for num in l2:
    m2[num] = 0
  for num in l2:
    m2[num] += 1
  
  for num in l1:
    try:
      similarity += int(num) * m2[num]
    except:
      continue

  print(similarity)


p1()
p2()
