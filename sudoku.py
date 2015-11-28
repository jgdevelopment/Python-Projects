boardString = """
.5...4...
.....2.9.
13..685.2
3.78.9.5.
..2.1.9..
.4.6.31.7
8.394..65
.7.3.....
...2...3."""
  
validNum = []
for r in range(9):
	row = []
	for c in range(9):
		row.append(range(1,10))
	validNum.append(row)
row = 0
col = 0
for char in boardString:
	if char == "\n":
		continue
	if char != ".":
		validNum[row][col] = [int(char)]
	col+=1
	if (col==9):
		row+=1
		col = 0	

def propagate(row, col):
	singleton = validNum[row][col][0]
	for x in xrange(0,9):
		if x == col:
			continue
		if singleton in validNum[row][x]:
			validNum[row][x].remove(singleton)
			if len(validNum[row][x])==1:
				propagate(row,x)

	for y in xrange(0,9):
		if y == row:
			continue
		if singleton in validNum[y][col]:
			validNum[y][col].remove(singleton)
			if len(validNum[y][col])==1:
				propagate(y,col)

	for i in xrange():


for x in range(9):
	for y in range(9):
		if (len(validNum[y][x])==1):
			propagate(y,x)

print validNum
