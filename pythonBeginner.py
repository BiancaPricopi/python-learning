x = [4, True, 'hi']
x.extend([1, 3, 4])
x.pop(0)
# x si y pointeaza la aceeasi referinta so daca modific x, y o sa aiba si el modificarea
# y = x[:] ca sa fac o copie a lui x
y = x
x[0] = 'eh'
print('x=', x)
print('y=', y)
