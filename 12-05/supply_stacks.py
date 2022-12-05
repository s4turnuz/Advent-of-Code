import re
from collections import defaultdict

f = open('12-05/stacks.txt').readlines()

def after_moves(s, a, f, t, control_key):
  move = s[f][:a][::-1] if control_key else s[f][:a]
  s[t] = move + s[t]
  s[f] = s[f][a:]


def get_first(stack):
  return ''.join([v[0] for _, v in sorted(stack.items())])

array, stack_1 = [], defaultdict(str)

for line in f:
    if line[0] == 'm':
      array.append(list(map(int, re.findall('\d+', line))))
    else:
      for i, char in enumerate(line):
        if not char.isalpha():
          continue
        stack_1[i//4+1] += char

stack_2 = stack_1.copy()

for a, f, t in array:
    after_moves(stack_1, a, f, t, True)
    after_moves(stack_2, a, f, t, False)


print(get_first(stack_1))
print(get_first(stack_2))
