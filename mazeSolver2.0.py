maze = """
x xxxxxx
x x    x
x x x xx
x      x
xxxxxx x
""" 
lines = maze.split("\n")[1:-1]
lines = [list (line) for line in lines]

def solve(start, end, seen=None):
	if seen is None:
		seen = set()
	if start in seen:
		return False
	seen.add(start)

	x,y = start


	if x<0 or x>=len(lines[0]):
		return False
	if y<0 or y>=len(lines):
		return False
	if lines[y][x]!="x":
		lines[y][x] = "0"
		if start == end:
			print "end"
			return True 
		
		if solve((x+1,y),end, seen):
			return True
		if solve((x-1,y),end, seen):
			return True
		if solve((x,y+1),end, seen):
			return True
		if solve((x,y-1),end, seen):
			return True

	return False

print solve((1,0),(6,4))
print "\n".join("".join(line)for line in lines)
