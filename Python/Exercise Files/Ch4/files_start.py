#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("textfile.txt","w+")

  # Open the file for appending text to the end
  f = open("textfile.txt","r")

  # write some lines of data to the file
  # for i in range(10):
  #   f.write("this is the line"+str(i)+"\r\n")


  
  # close the file when done
  # f.close
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    fl = f.readlines()
    for x in fl:
      print(x)
    #  contents = f.read()

    #  print(contents)

  f.close  
if __name__ == "__main__":
  main()