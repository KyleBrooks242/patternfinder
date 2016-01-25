import StringIO, sys, os

''' The goal of this program is to determine if "random" user input contains
any patterns. It will read from a text file of user-generated input, and, given
a segment size, will divide the input into segments of the specified size. The
program will then look for simple patterns in the input and record these values
in a two-dimensional array with the structure [x][y]. Each x value will represent
the pattern, and the y value will represent the number of occurances in the input.
This program will not support any complex patterns, it will only register segments
that contain the same sequence. It is important that the user input file is a
single line, containing no newline characters or spaces'''


'''TODO''''''
Take found patterns and insert them into a two dimensional array
Figure out how to shift segments so all patterns might be found?
e.g. 123 312 312 300/if this is even necessary/logical'''



# Global general pathname that can be modified in functions
PATH = os.getcwd()

## MAIN FUNCTION -------------------------------------------------------

def main():
  
  file_name= sys.argv[1]

  # This determines the length of 'pattern' segments the string will be broken
  # into
  SEG_SIZE = int(sys.argv[2])

  # Count of all characters in the input file
  CHAR_COUNT= count_chars(file_name)

  # Array of the text that will be iterated through
  # created from text in file
  text = create_text_array(file_name)
  

  # Chunks of text, the 'segments' dividied like this so they can be accessed 
  seg_array = div_into_segs(text, SEG_SIZE)

##  pad_last_seg(seg_array, SEG_SIZE)

  find_patterns(text, seg_array, CHAR_COUNT, SEG_SIZE)
  

# COUNT CHARS ------------------------------------------------------------

# Simply returns the length of the text file
def count_chars(file_name):
  file_path = os.path.abspath(os.path.join(PATH, file_name))
  text= open(file_path, 'r').read()
  return len(text)

# CREATE_TEXT_ARRAY -------------------------------------------------------

# Creates the text array, so each value can be accesed 
def create_text_array(file_name):
  file_path = os.path.abspath(os.path.join(PATH, file_name))
  text = open(file_path, 'r').read()
  return text

# DIV_INTO_SEGMENTS -------------------------------------------------------

# Divides the text input into the segments of specified length
def div_into_segs(text, SEG_SIZE):
  
  seg_array = [text[i:i+SEG_SIZE] for i in range(0, len(text), SEG_SIZE)]
  return seg_array

# FIND_PATTERNS -----------------------------------------------------------

#heart of the program, finds the patterns 
def find_patterns(text, seg_array, CHAR_COUNT, SEG_SIZE):

  # Not sure what length to make the pattern array, for now it is simply
  # a guess that there will be less patterns than half the length of the text
  patterns = [[None for x in range(2)] for x in range(CHAR_COUNT / 2)]
  
  seg_ptr = 0
  text_ptr = SEG_SIZE
  
  
  for i in range (0, (len(seg_array)-1), 1):

    # if an equivalent segment has already been checked
    # this will prevent matches being counted more than once
    if (repeat_seg(seg_array, seg_ptr, i)):
      # grab the next segment in array  
      seg_ptr += 1
      # move text pointer to the array index after seg_ptr
      text_ptr = (seg_ptr + 1) * SEG_SIZE
      continue
    
    for j in range (text_ptr, (len(text)-SEG_SIZE), 1):
##      print("i is: " + str(i))
##      print(text_ptr)
      comp_value = text[text_ptr]
      for i in range (1, SEG_SIZE, 1):
        comp_value = comp_value + text[text_ptr + i]
      
      if (seg_array[seg_ptr] == comp_value):        
        insert_val(seg_array[seg_ptr], patterns)
        
      text_ptr += 1

    # grab the next segment in array  
    seg_ptr += 1
    # move text pointer to the array index after seg_ptr
    text_ptr = (seg_ptr + 1) * SEG_SIZE

  patterns = sorted(patterns, key= lambda x: patterns[3])
  print_patterns(patterns)
  num_patterns = count_patterns(patterns)
  print("Number of patterns: "),
  print(num_patterns)
  print("Length of input: "),
  print(len(text))


# INSERT_VAL ---------------------------------------------------------------

def insert_val(val, patterns):
  i = 0
  while (patterns[i][0] != None):
    if (val == patterns[i][0]):
      patterns[i][1] +=1
      return
    i += 1
  patterns[i][0] = val
  patterns[i][1] = 2
      
  
                 
# REPEAT_SEG ---------------------------------------------------------------

def repeat_seg(seg_array, seg_ptr, index):
  for i in range (0, index, 1):
    if (seg_array[i] == seg_array[index]):
      return True

  return False

# PRINT_PATTERNS -----------------------------------------------------------

def print_patterns(patterns):
  
  i = 0
  while (patterns[i][0] != None):
    for j in range (0, len(patterns[0]), 1):
      print(patterns[i][j]),
    print('')
    i += 1

# COUNT_PATTERNS -----------------------------------------------------------

def count_patterns(patterns):
  i = 0
  while (patterns[i][0] != None):
    i += 1

  return i

# PAD_LAST_ARRAY -----------------------------------------------------------

##def pad_last_seg(seg_array, SEG_SIZE):
##  if(len(seg_array[-1]) == SEG_SIZE):
##    return
##  else:
##    ## Not sure what to do here


  
if __name__ == "__main__":
  main()
