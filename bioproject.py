from decimal import Decimal

# Variable initializations
line_0 = "ATOM"
S = "  S   "
lastletter = "S"
value = "  1.00 "

file1 = raw_input("Please enter the filename (with .pdb extension): ")	



def Centroid_output1(file1):
	# This is the first part of the project

	lineNumber = 0
	k = 1
	asum = bsum = csum = 0
	blank = ""
	pre = []
	val = 0
	
	inputfile = open(file1,'r')
	outputfile = open("outputtask1.pdb",'wb')	
	
	for line in inputfile:
		line = line.split()
		if line_0 == line[0]:
			if len(line[2]) > 3:
				temp = line[2][:3]
				temp1 = line[2][3:]
				line[2] = temp
				line.insert(3,temp1)
			
			if line[2]!= "N" and line[2]!="CA" and line[2]!="C" and line[2]!="O" and line[2]!="H":
				#outputfile.write(line[0])
				if val != int(line[5]):
					if lineNumber != 0:
						avg_a = asum / lineNumber
						avg_b = bsum / lineNumber
						avg_c = csum / lineNumber
						last = last_sum / lineNumber
						blank = pre[5]
						a = str(round(Decimal(avg_a),3))
						b = str(round(Decimal(avg_b),3))
						c = str(round(Decimal(avg_c),3))
						x = str(round(Decimal(last),2))
						
						#print lineNumber, pre
						#print a, b, c, x
						
						outputfile.write ( line_0 + (6-len(str(k))) * " " + str(k) + S + str(pre[3]) + " " + str(pre[4]) + (4-len(str(blank))) * " " + str(blank) + (12-len(a)) * " " + a + (8-len(b)) * " " + b + (8-len(c)) * " " + c + value + str(x) + (16-len(str(x))) * " " + lastletter + "\n" )
						
						k+=1
						avg_a = avg_b = avg_c = last = 0
					
					
					lineNumber = 1
					
					val = int(line[5])
					asum = float(line[6])
					bsum = float(line[7])
					csum = float(line[8])
					last_sum = float(line[10])
					
					
				else:
					lineNumber = lineNumber + 1
					
					asum = asum + float(line[6])
					bsum = bsum + float(line[7])
					csum = csum + float(line[8])
					last_sum = last_sum + float(line[10])
				
				pre = line
	#last value
	avg_a = asum / lineNumber
	avg_b = bsum / lineNumber
	avg_c = csum / lineNumber
	last = last_sum / lineNumber
	
	blank = pre[5]
	
	a = str(round(Decimal(avg_a),3))
	b = str(round(Decimal(avg_b),3))
	c = str(round(Decimal(avg_c),3))
	x = str(round(Decimal(last),2))
	
	#Creating a new pdb file
	outputfile.write (line_0 + (6-len(str(k))) * " " + str(k) + S + str(pre[3]) + " " + str(pre[4]) + (4-len(str(blank))) * " " + str(blank) + (12-len(a)) * " " + a + (8-len(b)) * " " + b + (8-len(c)) * " " + c + value + str(x) + (16-len(str(x))) * " " + lastletter + "\n")
	
	outputfile.close()
	
	print "\t\t***output file outputtask1.pdb is generated.***"	
	

# Calling first function	
Centroid_output1(file1)


def Centroid_output2and3(file1):
	# This is the second part of the project
	
	helix_array = []
	array_file = {}
	keys = []
	
	inputfile = open(file1,"rb")
	
	outputfile = open('outputtask2.pdb','w')
	
	for line in inputfile:
		line = line.split()
		
		if "HELIX" == line[0]:
			helix_array.append(line)
			
	inputfile= open(file1,"rb")
	for line in inputfile:
		line = line.split()
		
		if line_0 == line[0]:
			if len(line[2]) > 3:
				temp = line[2][:3]
				temp1 = line[2][3:]
				line[2] = temp
				line.insert(3,temp1)
				
			if "CA" == line[2]:
				if int(line[5]) not in array_file.keys():
					array_file[int(line[5])] = line
					keys.append(int(line[5]))

	
	
	counter=1
	for line in helix_array:
		startline = int(line[5])
		endline = int(line[8])
		for i in array_file.keys():
			val1 = val2 = val3 = last = 0 

			if i >= startline and i <= endline - 3:
				ind = keys.index(i)
			
				val1+=  round((Decimal(array_file[i][6])+ Decimal(array_file[keys[ind+1]][6]) + Decimal(array_file[keys[ind+2]][6]) + Decimal(array_file[keys[ind+3]][6]))/4,3)
				
				val2+=  round((Decimal(array_file[i][7])+ Decimal(array_file[keys[ind+1]][7]) + Decimal(array_file[keys[ind+2]][7]) + Decimal(array_file[keys[ind+3]][7]))/4,3)
				
				val3+=  round((Decimal(array_file[i][8])+ Decimal(array_file[keys[ind+1]][8]) + Decimal(array_file[keys[ind+2]][8]) + Decimal(array_file[keys[ind+3]][8]))/4,3)
				
				last+=  round((Decimal(array_file[i][10])+ Decimal(array_file[keys[ind+1]][10]) + Decimal(array_file[keys[ind+2]][10]) + Decimal(array_file[keys[ind+3]][10]))/4,3)
				
				val1 = str(val1)
				val2 = str(val2)
				val3 = str(val3)
				last = str(last)
				
				outputfile.write( line_0 + (6-len(str(counter))) * " " + str(counter) + S + str(array_file[i][3]) + " " + str(array_file[i][4]) + (4-len(str(array_file[i][5]))) * " " + str(array_file[i][5]) + (12-len(val1)) * " " + val1 + (8-len(val2)) * " " + val2 + (8-len(val3)) * " " + val3 + value + str(last) + (16-len(str(last))) * " " + lastletter + "\n" )
				
				
				counter+=1
		
	
	outputfile.close()
	inputfile.close()
	
	print "\t\t***output file outputtask2.pdb is generated.***"

# This is the third part of the project - N, CA, C and N
	
	B_array = []
	S_array = []
	sheet_array = []
	array_file={}
	Beta_keys =[]
	
	#to show the extraction of N, CA, C and O lines only	
	#testfile = open('test.pdb','w')  
	
	inputfile = open(file1,"rb")
	
	#Checking for "Sheets" only 
	for line in inputfile:
		S_array = line.split()
		if "SHEET" == S_array[0]:
			startline = S_array[6]
			endline = S_array[9]
			sheet_array.append(startline)
			sheet_array.append(endline)
	inputfile.close()
	
	output = open('outputtask3.pdb','w')
	input = open(file1,"rb")
	input.readline()
	
	
	for line in input:
		B_array = line.split()
	
		#Extracting only the N, CA and C atoms from the pdb file
		if line_0 == B_array[0]:
			if B_array[2] == 'N' or B_array[2] == 'CA' or B_array[2] == 'C':
				if int(B_array[5]) not in array_file.keys():
					array_file[int(B_array[5])] = [B_array]
					#testfile.write(line_0 + (6-len(str(counter))) * " " + str(B_array[1]) +(4-len(str(B_array[1]))) * " " + B_array[2] + (4-len(str(B_array[2]))) * " " + str(B_array[3]) + " " + str(B_array[4]) + (4-len(str(B_array[4]))) * " " + str(B_array[5]) + "\n")
					
				else:
					array_file[int(B_array[5])].append(B_array)
					#testfile.write(line_0 + (6-len(str(counter))) * " " + str(B_array[1]) +(4-len(str(B_array[1]))) * " " + B_array[2] + (4-len(str(B_array[2]))) * " " + str(B_array[3]) + " " + str(B_array[4]) + (4-len(str(B_array[4]))) * " " + str(B_array[5]) + "\n")
					
				
				if int(B_array[5]) not in Beta_keys:
					Beta_keys.append(int(B_array[5]))
				
				
				
	counter=1
	for i in range(0,len(sheet_array),2):
		for j in array_file.keys():
			if int(sheet_array[i]) <= int(array_file[j][0][5]) and  int(array_file[j][0][5]) <= int(sheet_array[i + 1]):
				ind1 = Beta_keys.index(int(array_file[j][0][5]))
				try:
		
					val1 =  round((Decimal(array_file[j][0][6])+ Decimal(array_file[j][1][6]) + Decimal(array_file[j][2][6]) + Decimal(array_file[Beta_keys[ind1+1]][0][6]))/4,3)
			
					val2 =  round((Decimal(array_file[j][0][7])+ Decimal(array_file[j][1][7]) + Decimal(array_file[j][2][7]) + Decimal(array_file[Beta_keys[ind1+3]][0][7]))/4,3)
			
					val3 =  round((Decimal(array_file[j][0][8])+ Decimal(array_file[j][1][8]) + Decimal(array_file[j][2][8]) + Decimal(array_file[Beta_keys[ind1+3]][0][8]))/4,3)
			
					last =  round((Decimal(array_file[j][0][10])+ Decimal(array_file[j][1][10]) + Decimal(array_file[j][2][10]) + Decimal(array_file[Beta_keys[ind1+3]][0][10]))/4,3)
			
				
					#print val1, val2, val3, last
			
					
					val1 = str(val1)
					val2 = str(val2)
					val3 = str(val3)
					last = str(last)
					x = 1
					output.write( line_0 + (6-len(str(counter))) * " " + str(counter) + S + str(array_file[j][0][3]) + " " + str(array_file[j][0][4]) + (4-len(str(array_file[j][0][5]))) * " " + str(array_file[j][0][5]) + (12-len(val1)) * " " + val1 + (8-len(val2)) * " " + val2 + (8-len(val3)) * " " + val3 + value + str(last) + (16-len(str(last))) * " " + lastletter + "\n" )
					
					counter+=1
					
				except:
					x = 0
	output.close()
	input.close()
	print "\t\t***output file outputtask3.pdb is generated***"

	
#Calling second function
Centroid_output2and3(file1)