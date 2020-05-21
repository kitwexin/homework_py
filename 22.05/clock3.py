import time
import datetime
def getNum(matrix):
	txt = matrix.replace('1', "\u2593")
	txt = txt.replace('0',' ')
	return [x for x in txt.split("\n") if x]
n0 = getNum("""
11111
10001
10001
10001
11111
""")
n1 = getNum("""
11100
00100
00100
00100
11111
""")
n2 = getNum("""
11111
00001
11111
10000
11111
""")
n3 = getNum("""
11111
00001
11111
00001
11111
""")
n4 = getNum("""
10001
10001
11111
00001
00001
""")
n5 = getNum("""
11111
10000
11111
00001
11111
""")
n6 = getNum("""
11111
10000
11111
10001
11111
""")
n7 = getNum("""
11111
00010
00100
01000
01000
""")
n8 = getNum(r"""
11111
10001
11111
10001
11111
""")
n9 = getNum(r"""
11111
10001
11111
00001
11111
""")
nd = getNum(r"""
00000
00100
00000
00100
00000
""")
TRANS = {
      '0': n0, '1': n1, '2': n2, '3': n3, '4': n4,
      '5': n5, '6': n6, '7': n7, '8': n8, '9': n9,
      ':': nd
}
while True:
	txt = ""
	for x in range(5):
		for y in datetime.datetime.now().strftime("%X"):
			txt += TRANS[y][x]
			txt += " "
		txt += "\n"
	print(txt)
	time.sleep(1)