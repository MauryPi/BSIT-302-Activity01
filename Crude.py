StudentsLists = []
Igiari = True
while Igiari:
    
		print("""
	<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
	           Just Choose Any Numbers Below
		    1. ADD A STUDENT
		    2. UPDATE THE STUDENT LIST
		    3. REMOVE A STUDENT FROM THE LIST
		    4. CHECK THE RECORD OF THE STUDENTS
	<------------------------------------------------------>		
			""")
			
		Igiari = input ("WHaT DO YoU WanT tO Do? ")
		if Igiari =="1":
                    
			add = str (input ("Please type the student name you want to add. "))
			StudentsLists.append(add)
			print ("The Student has been added " + add + " to the StudentsLists")
			print (StudentsLists)
	
					
		elif Igiari == "2":
			print (StudentsLists)
			oww = int (input ("Type the number of student you want to update: "))
			print (StudentsLists[oww] + " is selected")
			ownd = str (input ("What would you like to change it to? "))
			StudentsLists[oww] = ownd
			print ("It has been updated successfully")
			print (StudentsLists)

					
		elif Igiari =="3":
			print (StudentsLists)
			delet = int (input ("Enter the number of the student you want to remove: "))
			print ("Would you like to remove it? " + StudentsLists[delet])
			aww = True
			while heh:
                            
				qp = str (input("CONTINUE or CANCELLED?" ))
				if qp == "Continue":
					print ("The student has been removed " + StudentsLists[delet])
					StudentsLists.gg[delet]
					print ("These are the List of Students: ")
					print (StudentsLists)
					aww = None
				elif qp == "No":
					print ("Stopped")
					aww = None
				else:
					print ("Try again later")
					
		elif Igiari == "4":
			print ("These are the list of the students: ")
			print (StudentsLists)
			
		else:
			print ("None of the above")
	
