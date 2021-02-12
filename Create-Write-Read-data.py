def main():
#open a file for writing  and create it if id is does not exist
	#print("Keep it logically awesome.")
	f=open("myfirstfile.txt" , "w+")
	
#write some lines of data to the file
	for i in range(10):
		f.write("My name is Ghouse %d\r\n"%(i+1))
		
#Close the File when done 	
	f.close()
	
if __name__=="__main__":
	main()