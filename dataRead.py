#imports our created LinkedList class
import LinkedList

#make function to read in all the data
def readIn():
	#initializes list of CSV files
	datfilespeed = list()
	datfiledist = list()

	#adds the CSV files to the list
	datfilespeed.append('Speed2.csv')
	datfilespeed.append('Speed3.csv')
	datfilespeed.append('Speed4.csv')
	datfilespeed.append('Speed5.csv')

	datfiledist.append('Distance1.csv')
	datfiledist.append('Distance2.csv')
	datfiledist.append('Distance3.csv')
	datfiledist.append('Distance4.csv')

	#strings for regex
	speed1 = 'Counter for vehicle speed within (105-120 kph)'
	speed2 = 'Counter for vehicle speed within (120-135 kph)'
	speed3 = 'Counter for vehicle speed within (135-150 kph)'

	distance1 = 'Counter for FCA gap setting at (Near)'
	distance2 = 'Counter for FCA gap setting at (Medium)'
	distance3 = 'Counter for FCA gap setting at (Far)'
	distance4 = 'Counter for FCA gap setting at (Off)'

	#initialize errors and found
	errors = 0
	found = False

	#creates linked list 
	valueList = LinkedList.LinkedList()

	#loops through all the files
	for fh in datfilespeed:
		#opens the file and reads in data
		f = open(fh, 'r')

		#goes through each line
		for line in f:
			#sets values equal to an array of each variable in the line

			values = line.split(',')
			if (speed1 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[4]):
						if (int(values[2]) > 0):
							Node.speed1 = 1
						found = True

				if (not found) :
					#if it isn't, then add vin to linked list and set speed to 1
					valueList.add_first(LinkedList.Node(values[4][0:6]))
					if (int(values[2]) > 0):
						valueList.head.speed1 = 1
				found = False

			elif (speed2 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[4]):
						if (int(values[2]) > 0):
							Node.speed2 = 1
						found = True

				if (not found) :
					#if it isn't, then add vin to linked list and set speed to 1
					valueList.add_first(LinkedList.Node(values[4][0:6]))
					if (int(values[2]) > 0):
						valueList.head.speed2 = 1

				found = False

			elif (speed3 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[4]):
						if (int(values[2]) > 0):
							Node.speed3 = 1
						found = True

				if (not found) :
					#if it isn't, then add vin to linked list and set speed to 1
					valueList.add_first(LinkedList.Node(values[4][0:6]))
					if (int(values[2]) > 0):
						valueList.head.speed3 = 1
				found = False

		f.close()

	for fh in datfiledist:
		#opens the file and reads in data
		f = open(fh, 'r')

		#goes through each line
		for line in f:
			values = line.split(',')
			if (distance1 in values[0]):
				
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[5]):
						if (int(values[2]) > 0):
							Node.near = int(values[2])+Node.near
						found = True

				#if it isn't, then increment the errors, as we don't have that vin in the list from speed
				if (not found):
					errors = errors + 1
				found = False

			elif (distance2 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[5]):
						if (int(values[2]) > 0):
							Node.medium = int(values[2])+Node.medium
						found = True

				#if it isn't, then increment the errors, as we don't have that vin in the list from speed
				if (not found):
					errors = errors + 1
				found = False
			
			elif (distance3 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[5]):
						if (int(values[2]) > 0):
							Node.far = int(values[2])+Node.far
						found = True

				#if it isn't, then increment the errors, as we don't have that vin in the list from speed
				if (not found):
					errors = errors + 1
				found = False

			elif (distance4 in values[0]):
				#iterate through to see if vin exists in linked list, and if so add speed
				for Node in valueList:
					if (Node.vin in values[5]):
						if (int(values[2]) > 0):
							Node.off = int(values[2])+Node.off
						found = True

				#if it isn't, then increment the errors, as we don't have that vin in the list from speed
				if (not found):
					errors = errors + 1
				found = False
		f.close()

#set the setting to the one (near far medium or off) with the highest counter
	for Node in valueList:
		if (Node.far > Node.near and Node.far > Node.medium and Node.far > Node.off): 
			Node.setting = 'Far'
		elif (Node.near > Node.far and Node.near > Node.medium and Node.near > Node.off): 
			Node.setting = 'Near'
		elif (Node.medium > Node.far and Node.medium > Node.near and Node.medium > Node.off): 
			Node.setting = 'Medium'
		elif (Node.off > Node.far and Node.off > Node.near and Node.off > Node.medium ):
			Node.setting = 'Off'
		else :
			errors = errors + 1
			valueList.remove_node(Node.vin)
	return valueList

	#prints out the linked list to make sure it is correct
	print(valueList)
	#errors are cars that have no setting numbers--all are set to 0!
	print(errors)
