# Problem Statement : 

# 6.5 Write code using find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

 # Code is Written By Krishna

# The code below almost works

text = "X-DSPAM-Confidence:    0.8475"
ind=text.find("  ")
pos=text.find('5')
print(float(text[ind:pos+1]))
