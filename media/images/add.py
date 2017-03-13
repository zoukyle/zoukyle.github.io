import os
f = []
for (_, _, filenames) in os.walk('.'):
  f.extend(filenames)
  break
prefix = '641C'
images = []
for i in f:
  if '.JPG' not in i or prefix not in i:
    continue
  try:
    n = int(i.split('.')[0].replace(prefix, '').replace('-Edit', ''))
  except ValueError:
    continue
  if n < 4936 or n > 5087:
    continue
  images.append(i)
counter = 0
output = ''
for i in images:
  counter = counter + 1
  if (counter % 4 == 0):
    output += "'%s',\n" %i
  else:
    output += "'%s', " % i
print(output)
