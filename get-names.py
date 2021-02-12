import random
def main():
	#print("Keep it logically awesome.")

	f = open("names.txt")
	names = f.readlines()
	#f.close();
	last = len(names)-1
	rand = random.randint(0, last)
	print(names[rand])

if __name__== "__main__":
  main()
