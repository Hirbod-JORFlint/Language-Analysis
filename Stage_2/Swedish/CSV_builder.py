import csv
import os
import pandas as pd
import re

# remove everythong between first comma and singular
# Open dataset file
with open('your_dataset.txt', 'r') as f:
    lines = f.readlines()

# Perform the substitution on each line
new_lines = [re.sub(',.*?,Singular', ',Singular', line) for line in lines]

# Write the result back to the file
with open('ou1.txt', 'w') as f:
    f.writelines(new_lines)

# Only keep the nouns
with open('ou2.csv', 'r',encoding="utf-8") as csvfile, open('ou2.txt', 'w',encoding="utf-8", newline='') as outfile:
    data=csvfile.readlines()
    for i in data:
        if i.find('Singular')>-1:
            outfile.write(i)
            



#remove everything after bestämd form genitiv
with open('your_dataset.txt', 'r') as f:
    lines = f.readlines()
# Perform the substitution on each line
new_lines = [re.sub(',bestämd form genitiv.*', ',bestämd form genitiv', line) for line in lines]

# Write the result back to the file (or to a new file if you prefer)
with open('your_dataset.txt', 'w') as f:
    f.writelines(new_lines)

    
#find irregular columns
with open('ou1.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        if len(row) > 19:
            print(f"Row {i} has {len(row)} columns.")

#duplicate removal
def remove_duplicates(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = list(set(lines))
    with open(filename, 'w') as f:
        f.writelines(lines)

# Replace , with ; in paretheses regular expression
with open('your_dataset.txt', 'r') as f:
    # Read all lines from the file into a list
    lines = f.readlines()

# For each line in the list of lines
new_lines = [
    # Use a regular expression to find text within parentheses
    # For each match, replace commas with semicolons
    re.sub(r'\(([^)]*)\)', lambda m: m.group().replace(',', ';'), line) 
    for line in lines
]

# Open your dataset file in write mode
with open('your_dataset.txt', 'w') as f:
    # Write the modified lines back to the file
    f.writelines(new_lines)

# merge the datasets
files = ['ou1.csv', 'ou2.csv', 'ou3.csv', 'ou4.csv', 'ou5.csv']

# Read each file into a pandas DataFrame and store all DataFrames in a list
dfs = [pd.read_csv(file) for file in files]

# Concatenate all DataFrames in the list into one DataFrame
merged_df = pd.concat(dfs)

# Write the merged DataFrame to a new file
merged_df.to_csv('merged_dataset.csv', index=False)



    
filename = 'refined_out.csv'
tempfile = 'temp.csv'

# with open('refined_out.csv', 'r',encoding="utf-8") as csvfile, open(tempfile, 'w',encoding="utf-8", newline='') as outfile:
#     datareader = csv.reader(csvfile)
#     datawriter = csv.writer(outfile)
#     for row in datareader:
#         if not row[2]:
#             row.pop(2)
#             datawriter.writerow(row)
#         else:
#             datawriter.writerow(row)


 with open('merged_dataset.csv', 'r',encoding="utf-8") as csvfile, open('refined_out.csv', 'w',encoding="utf-8", newline='') as outfile:
     datareader = csv.reader(csvfile)
     datawriter = csv.writer(outfile)
     for row in datareader:
         if row[1]=="Singular obestämd":
             datawriter.writerow(row)

         elif row[1][:3]=="en ":
             row[1]=row[1][3:]
             row[2]=row[2][3:]
             row.append("en")
             datawriter.writerow(row)

         elif row[1][:4]=="ett ":
             row[1]=row[1][4:]
             row[2]=row[1][4:]
             row.append("ett")
             datawriter.writerow(row)
         else:
             row.append("Don")
             datawriter.writerow(row)
            
# Replace the original file with the temp file
#os.remove(filename)
#os.rename(tempfile, filename)

df = pd.read_csv('refined_out.csv',dtype=str)

def first_letter(w):
    w=w.replace("(", "").replace(")", "")
    return w[0]

def first_2_letters(w):
    w=w.replace("(", "").replace(")", "")
    if len(w)>1:
        return w[0:2]
    else:
        return w
    
def first_3_letters(w):
    w=w.replace("(", "").replace(")", "")
    if len(w)>2:
        return w[0:3]
    else:
        return w

def last_letter(w):
    w=w.replace("(", "").replace(")", "")
    return w[-1]

def last_2_letters(w):
    w=w.replace("(", "").replace(")", "")
    if len(w)>1:
        return w[-2:]
    else:
        return w

def last_3_letters(w):
    w=w.replace("(", "").replace(")", "")
    if len(w)>2:
        return w[-3:]
    else:
        return w

def vowel_ratio(w):
    swedish_vowels = 'aeiouyåäö'
    vowel_count = sum(1 for char in w if char.lower() in swedish_vowels)
    return vowel_count / len(w)



# applying functions to compute new dataframe.
df.fillna('NOP', inplace=True)

df["Obestämd Första Bokstav"]= df['Singular obestämd'].apply(first_letter)
df["Bestämd Första Bokstav"]= df['Singular bestämd'].apply(first_letter)

df["Obestämd Initial Två Bokstäver"]= df['Singular obestämd'].apply(first_2_letters)
df["Bestämd Initial Två Bokstäver"]= df['Singular bestämd'].apply(first_2_letters)

df["Obestämd Initial Tre Bokstäver"]= df['Singular obestämd'].apply(first_3_letters)
df["Bestämd Initial Tre Bokstäver"]= df['Singular bestämd'].apply(first_3_letters)

df["Obestämd Sista Bokstäver"]= df['Singular obestämd'].apply(last_letter)
df["Bestämd Sista Bokstäver"]= df['Singular bestämd'].apply(last_letter)

df["Obestämd Slutlig Två Bokstäver"]= df['Singular obestämd'].apply(last_2_letters)
df["Bestämd Slutlig Två Bokstäver"]= df['Singular bestämd'].apply(last_2_letters)

df["Obestämd Slutlig Tre Bokstäver"]= df['Singular obestämd'].apply(last_3_letters)
df["Bestämd Slutlig Tre Bokstäver"]= df['Singular bestämd'].apply(last_3_letters)

df["Obestämd Vokalratio"]= df['Singular obestämd'].apply(vowel_ratio)
df["Bestämd Vokalratio"]= df['Singular bestämd'].apply(vowel_ratio)

df["Obestämd Ord Längd"]= df['Singular obestämd'].apply(len)
df["Bestämd Ord Längd"]= df['Singular bestämd'].apply(len)

df.fillna('NOP', inplace=True)

df.to_csv('output_svenska.csv', encoding='UTF-8', index=False)


