def wordCount(t):
  """ Retrieves data from a text file and returns a dictionary """
  dict = {}
  with open (t, 'r') as f:
    #this loop iterates over each line in the file
    for lineNum, line in enumerate(file, start=1):
      #This splits the line into words and then iterates over each word
      words = line.split()
      for word in words:
        #If the word is in the dictionary then it appends the line number to the list
        if word in dict:
          dict[word].append(lineNum)
        #If not then it creates a new entry in the dictionary.
        else:
          dict[word] = [lineNum]
  return dict

if __name__ == "__main__":
  print(wordCount('test2.txt'))
