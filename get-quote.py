import random
def main():
	#print("Keep it logically awesome.")

	f = open("quotes.txt","a+")
	for i in range(10):
		f.write("Learn Python \n"%(i+1))
	quotes = f.readlines()
	f.close()
	#last = 13
	last = len(quotes) - 1
	rand = random.randint(0, last)
	print(quotes[rand])

if __name__== "__main__":
  main()
