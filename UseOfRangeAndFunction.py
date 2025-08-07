def to_celsius(x):
  return (x-32)*5/9

#
# Syntax:
#  range(stop)
#  range(start, stop)
#  range(start, stop, step)
#
#  start (optional): The starting value of the sequence (inclusive). Defaults to 0 if not provided.
#  stop (required): The ending value of the sequence (exclusive).
#  step (optional): The difference between each number in the sequence. Defaults to 1 if not provided.


for x in range(0,101,10):
  print(x, to_celsius(x))