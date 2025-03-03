#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  fileInput = input("Enter file name: ")
  textFile = open(fileInput, 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    for char in line:
      if char == "\n":
        letterCount = letterCount - 1
      letter = len(char)
      letterCount = letterCount + letter

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
  

if __name__ == '__main__':
  main()
