import sys, os

try:
  qasm_file = sys.argv[1]
except:
  print('Usage: {} <qasm file>'.format(sys.argv[0]))
  exit()

with open(qasm_file, 'r') as f:
  content = f.readlines()
  content = [line.replace('\n', '') for line in content]
  content = [line.replace(';', '') for line in content]
  content = [line.replace('],q', '] q') for line in content]
  content = [line.replace('cx', 'CX') for line in content]

  for idx, line in enumerate(content):
    if idx == 2:
      nqubit = int(line[7:-1])
      print('.qubit {}'.format(nqubit))
      for _ in range(nqubit):
        print('qubit q[{}]'.format(_))
      print('.begin')
    elif idx > 2:
      print(line)
  print('.end')

