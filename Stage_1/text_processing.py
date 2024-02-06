from collections import Counter
import pickle

with open("Cardinals2.txt",mode="r",encoding='utf-8') as f:
    follow=f.readlines()

# remove newline characters
follow2=[m2.replace('\n','') for m2 in follow]

"""I discovered that the seperator is the last item of every line that is not
a multiply of 9"""
# find the seperators
dictionary_plot=dict()

for i, line in enumerate(follow2):
    if (i) % 9 == 0:  # Check if the line number is a multiple of 9
        #remove useless markers
        l2=line.replace('{','')
        l2=l2.replace('}','')
        dict_key=l2  # Append the entire line without splitting
    else:
        # Split the line based on your identified separators and append to the list
        # last element of the line is seperator
        # for the lines whose sum of digits equal to 8 use the
        #previous seperator
        length=len(line)
        if (i+1) % 9 !=0:
            sep=line[length-1]
        split_line = line.strip().split(sep)

        # Check if the key exists in the dictionary
        if dict_key in dictionary_plot:
            # If the key exists, extend the existing list
            dictionary_plot[dict_key]=dictionary_plot[dict_key]+(split_line)
        else:
            # If the key doesn't exist, create a new key with the split line
            dictionary_plot[dict_key] = split_line

    #strip each elements of the line from their white space
    #to save computation we do it on the last line before the keys
    if ((i+1) % 9 ==0 and i!=0):
        dictionary_plot[dict_key]=[white.strip() for white in dictionary_plot[dict_key]]

# Remove all instances of nothingness (empty strings) from the values associated with each key
for key in dictionary_plot.keys():
    dictionary_plot[key] = [value for value in dictionary_plot[key] if value != '']

with open('dictionary_data.pkl', 'wb') as pi_dump:
    pickle.dump(dictionary_plot, pi_dump)
