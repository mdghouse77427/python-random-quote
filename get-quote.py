import random
def main():
	#print("Keep it logically awesome.")

	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()
	last = 13
	last = len(quotes) - 1
	rand = random.randint(0, last)
	print(quotes[rand])

if __name__== "__main__":
  main()
