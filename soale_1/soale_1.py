# 1.Process Text File Data:

# A short section of an aticle about artificial intelligence
list1=[]
# Read a text file containing sentences
# Open the text file
with open('file.txt', 'r') as file:
    for line in file:
        print(line)
print('\n')






# Extract all unique words using list comprehension.

# Open the text file
with open('file.txt', 'r') as file:
    line = file.read()
    # Split into lines
    lines=line.split()
    for i in lines:
        if i not in list1:
            list1.append(i)
    print(list1)
print('\n')

# Create a dictionary where keys represent unique words and values
# indicate the lengths of the words.

# Create the dictionary

dict ={}
for i in list1:
    dict[i]=len(i)
        # Print the dictionary
print(dict)
print('\n')


# Sort the dictionary by values in the results
results = sorted(dict.items(), key=lambda x:x[1])

# Print the results
print(results)
print('\n')

# save the results to a new text file,
# the file name is nextfile
with open('results.txt', 'w') as nextfile:
# step 1: Sort the dictionary by values
    nextfile.write(str(results))
    nextfile.write('\n\n')
# step 2: sort the dictionary
    for i in results:
        nextfile.write(i[0])
        nextfile.write(' ')

















