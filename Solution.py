# This Function reads all the Data-Files and returns the Dictionary
def read_data_file(filename):
    # 2 Empty Lists are created
    l1, l2 = [], []
    # Opening a File ina Read Mode
    fileHandle = open(filename, 'r')
    # Skiping the header file in each file
    next(fileHandle) 
    for line in fileHandle:
        # Spliting the field id the have a PIPE '|' Symbol
        field = line.split('|')
        # Append the particular Field Extracted from the file into LIST
        l1.append(field[0]) # Student IDis been retrieved here
        city_grade = field[2] + field[3] # City Name and Grades are extracted here
        l2.append(city_grade) 
    # Created a dictionary by zipping both the data lists
    data_dict = dict(zip(l1,l2))
    # Close the file
    fileHandle.close()
    # Returning the dictionary of the data
    return data_dict

# This Function reads the Scholarship File and returns the Dictionary
def read_scholar_file(filename):
    l1, l2 = [], []
    fileHandle = open(filename, 'r')
    next(fileHandle) # Skiping the header file in each file
    for line in fileHandle :
        # Spliting the field id the have a PIPE '|' Symbol
        field = line.split('|')
        # Check if the 'Family Income' is 'LESS' than 5000
        if int(field[1]) < 5000 :
            l2.append(field[1]) # Extract the Family-Income
            l1.append(field[0]) # Extract the Student-ID
    # Created a dictionary by zipping both the data lists        
    scholar_dict = dict(zip(l1,l2))
    fileHandle.close()
    return scholar_dict

# File names of all the data files are stored in a list
filenames = ['data_10.txt', 'data_11.txt','data_12.txt']
# Empty Dictionary is created 
final_dict = {}

# Iterate over the filenames and create a data dictionary
for filename in filenames:
    data_dict = read_data_file(filename)
    # Final Dictionary is updated with the data retuned from the data files
    final_dict.update(data_dict)

scholar_dict = read_scholar_file('scholarship.txt')

print "Student ID's who's Family income is less than 5000 with Grades 'C' or 'D' and based in mumbai as as follows : "

# Check that Student ID exist in the final dictionary and the Value has MumbaiC or MumbaiD
for stud_id in scholar_dict.keys(): 
    if stud_id in final_dict.keys() and (final_dict[stud_id] == "mumbaiC" or final_dict[stud_id] == "mumbaiD"):
        print stud_id
