from test_headless import main
import pickle
studentAns=[]
for i in range(1,6):
	print(i)
	studentAns.append(main(i))

# Open a file and use dump()
with open('minmaxAlphaBeta.pkl', 'wb') as file:
      
    # A new file will be created
    pickle.dump(studentAns, file)

# Open the file in binary mode
with open('minmaxAlphaBeta.pkl', 'rb') as file:
      
    # Call load method to deserialze
    actualAns = pickle.load(file)

# print("\t",studentAns)  
for x in range(len(actualAns)):
	if (actualAns[x] == studentAns[x]).all():
		print("Test case ",x+1, "- Pass")
	else:
		print("Test case ",x+1, "- Failed")