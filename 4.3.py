def val_password(pw):
  f = 1
  l = len(pw)
  if l > 4:
    letters = 0
    numbers = 0
    for i in range(len(pw)):
      if (ord(pw[i]) >= ord('a')) & (ord(pw[i]) <= ord('z')):
        letters += 1
      elif (ord(pw[i]) >= ord('0')) & (ord(pw[i]) <= ord('9')):
        numbers += 1
      else:
        f = 0
        break
    if letters % 2 == 0 | numbers % 2 == 1:
      f = 0
  else:
    f = 0
  return f


pw = str(input())
if val_password(pw):
  print('Valid password.')
else:
  print('Not a valid password!')