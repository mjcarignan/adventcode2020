#advent code challenge: 20201204
import pandas as pd 
import re


def readfile(filepath):
	array2D = []
	f = open(filepath, "r")
	cred = str()
	count = 0
	for line in f:
		if line[0] != '\n':
			for character in line:
				if character != '\n':
					cred = cred + character
				else: cred = cred + ' '
		else: 
			array2D.append(cred.rstrip().split(' '))
			cred = ''
	array2D.append(cred.rstrip().split(' ')) #append the last credential
	return array2D

def explodeList(alist,required):
	cred_line = pd.DataFrame(columns=required)
	for i in range(len(alist)):
		split = alist[i].split(':')
		cred_line.loc[str(0) , split[0]] = split[1]
	return cred_line

def movetodf (data, required):
	cred_df = pd.DataFrame(columns=required)
	for i in range(len(data)):
		cred_df = cred_df.append(explodeList(data[i],required))
	return cred_df

def main():
	required = ['byr', 'iyr', 'eyr', 'hgt' , 'hcl', 'ecl', 'pid', 'cid']
	cred_df = movetodf(readfile("20201204_data"), required)
	countvalid = 0

#Part 1
	notnull = cred_df.loc[
		(cred_df['byr'].notnull()) &
		(cred_df['iyr'].notnull()) &
		(cred_df['eyr'].notnull()) &
		(cred_df['hgt'].notnull()) &
		(cred_df['hcl'].notnull()) &
		(cred_df['ecl'].notnull()) &
		(cred_df['pid'].notnull()) 
		]

	print("Part 1 Valid passwords: " + str(len(notnull)))
<<<<<<< HEAD:2020/20201204.py
<<<<<<< HEAD:2020/20201204.py

=======
=======
>>>>>>> parent of 16f4965... completed day 4:20201204.py
	#pd.set_option('display.max_rows', None)
	#print(notnull)
>>>>>>> parent of 16f4965... completed day 4:20201204.py
# Part 2
	valid = notnull.loc[
		(notnull['byr'].astype(int) >= 1920) & (notnull['byr'].astype(int) <= 2002) &
		(notnull['iyr'].astype(int) >= 2010) & (notnull['iyr'].astype(int) <= 2020) &
		(notnull['eyr'].astype(int) >= 2020) & (notnull['eyr'].astype(int) <= 2030) &
<<<<<<< HEAD:2020/20201204.py
<<<<<<< HEAD:2020/20201204.py
		((notnull['hgt'].str.match("[5][9]|[6][0-6]|[6-7][0-6]in") ) | (notnull['hgt'].str.match("\d+cm")) ) & 
		(notnull['hcl'].str[0] == '#') & (notnull['hcl'].str.len() == 7) & (notnull['hcl'].str.contains('#[a-f0-9]{6,6}')) &
=======
=======
>>>>>>> parent of 16f4965... completed day 4:20201204.py
		(notnull['hgt'].str.contains("cm") | (notnull['hgt'].str.contains("in"))) &
		(notnull['hcl'].str[0] == '#') & (notnull['hcl'].str.len() == 7) &
		
		#(notnull['hgt'].str.contains("[1][5-9][0-3]cm") | (notnull['hgt'].str.contains("[5][9]|[6][0-6]|[6-7][0-6]in")))  
		#(notnull['hcl'].str[0] == '#') & (notnull['hcl'].str.len() == 7) & (notnull['hcl'].str.contains("[0-9]" or "[a-f]"))&
>>>>>>> parent of 16f4965... completed day 4:20201204.py
		(notnull['ecl'].isin(['amb','blu','brn','gry','grn','hzl','oth'])) &
		(notnull['pid'].str.contains("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")) & (notnull['pid'].str.len() == 9) 
		]
	print("Part 2 Valid passwords: " + str(len(valid)))
	
<<<<<<< HEAD:2020/20201204.py
<<<<<<< HEAD:2020/20201204.py
=======
	print(valid)
>>>>>>> parent of 16f4965... completed day 4:20201204.py
=======
	print(valid)
>>>>>>> parent of 16f4965... completed day 4:20201204.py
import time
start_time = time.time() 
main()
print("Total time: %s milliseconds" % round((time.time() - start_time)*1000, 3))