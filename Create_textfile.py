def main():
	f=open("My Bio Data.txt","w+")
	for i in range(10):
		f.write("My Name is Ghouse \nMy Age:24 %d\n"%(i+1))
	f.close()
	
if __name__=="__main__":
	main()