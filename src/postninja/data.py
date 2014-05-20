import sys
import xml.dom.minidom as mxml
import datetime



class vData:
	
	
	
	vFirstName = ''
	vMidInitial = ''
	vLastName = ''
	vNamePrefix = ''
	
	#Violation Address
	vAddressLineOne = ''
	vAddressLineTwo = ''
	vCity = ''
	vState = ''
	vZipCode = ''
	
	#Mailing Address
	vmAddressLineOne = 'Hey quit failing'
	vmAddressLineTwo = ''
	vmCity = ''
	vmState = ''
	vmZipCode = ''
	
	
	vMapNumber = ''
	
	vViolation = ''
	
	vDate = ''
	
	def print_to_console(self):
		print "FirstName: " , self.vFirstName
		print "MI: " , self.vMidInitial
		print "Last Name: " , self.vLastName
		print "Name Prefix: " , self.vNamePrefix
		print "Address 1: " , self.vAddressLineOne
		print "Address 2: " , self.vAddressLineTwo
		print "City: " , self.vCity
		print "State: " , self.vState
		print "Zip: " , self.vZipCode
		print "Map Code: " , self.vMapNumber
		print "Violation: " , self.vViolation
		print "Date: " , self.vDate
		print "Mailing Address"
		print "Address 1: ", self.vmAddressLineOne
		print "Address 2: ", self.vmAddressLineTwo
		print "City: ", 	self.vmCity
		print "State: ",  self.vmState
		print "Zip: " , self.vmZipCode
		
		return
		
	def save_to_xml(self, filename_string):

		newdom = mxml.getDOMImplementation()

		root = newdom.createDocument(None, "violation_record", None)

		top_element = root.documentElement
		xsltinfo = root.createProcessingInstruction('xml-stylesheet', 'type="text/xsl" href="config/standard.xsl"')
		
		root.insertBefore(xsltinfo, top_element)
		
		firstNameNode = root.createElement("FName")
		firstNameData = root.createTextNode(self.vFirstName)
		firstNameNode.appendChild(firstNameData)
		top_element.appendChild(firstNameNode)
		
		minitNode = root.createElement("MINIT")
		minitData = root.createTextNode(self.vMidInitial)
		minitNode.appendChild(minitData)
		top_element.appendChild(minitNode)
		
		lastNameNode = root.createElement("LName")
		lastNameData = root.createTextNode(self.vLastName)
		lastNameNode.appendChild(lastNameData)
		top_element.appendChild(lastNameNode)
		
		namePrefixNode = root.createElement("Prefix")
		namePrefixData = root.createTextNode(self.vNamePrefix)
		namePrefixNode.appendChild(namePrefixData)
		top_element.appendChild(namePrefixNode)
	
		#Violation Address
		addressOneNode = root.createElement("Addr1")
		addressOneData = root.createTextNode(self.vAddressLineOne)
		addressOneNode.appendChild(addressOneData)
		top_element.appendChild(addressOneNode)
		
		addressTwoNode = root.createElement("Addr2")
		addressTwoData = root.createTextNode(self.vAddressLineTwo)
		addressTwoNode.appendChild(addressTwoData)
		top_element.appendChild(addressTwoNode)
		
		cityNode = root.createElement("City")
		cityData = root.createTextNode(self.vCity)
		cityNode.appendChild(cityData)
		top_element.appendChild(cityNode)
		
		stateNode = root.createElement("State")
		stateData = root.createTextNode(self.vState)
		stateNode.appendChild(stateData)
		top_element.appendChild(stateNode)
	
		zipCodeNode = root.createElement("Zip")
		zipCodeData = root.createTextNode(self.vZipCode)
		zipCodeNode.appendChild(zipCodeData)
		top_element.appendChild(zipCodeNode)
	
		mailAddressOneNode = root.createElement("MAddr1")
		mailAddressOneData = root.createTextNode(self.vmAddressLineOne)
		mailAddressOneNode.appendChild(mailAddressOneData)
		top_element.appendChild(mailAddressOneNode)
		
		mailAddressTwoNode = root.createElement("MAddr2")
		mailAddressTwoData = root.createTextNode(self.vmAddressLineTwo)
		mailAddressTwoNode.appendChild(mailAddressTwoData)
		top_element.appendChild(mailAddressTwoNode)
		
		mailCityNode = root.createElement("MCity")
		mailCityData = root.createTextNode(self.vmCity)
		mailCityNode.appendChild(mailCityData)
		top_element.appendChild(mailCityNode)
		
		mailStateNode = root.createElement("MState")
		mailStateData = root.createTextNode(self.vmState)
		mailStateNode.appendChild(mailStateData)
		top_element.appendChild(mailStateNode)
		
		mailZipCodeNode = root.createElement("MZip")
		mailZipCodeData = root.createTextNode(self.vmZipCode)
		mailZipCodeNode.appendChild(mailZipCodeData)
		top_element.appendChild(mailZipCodeNode)
		
		mapNode = root.createElement("Map")
		mapData = root.createTextNode(self.vMapNumber)
		mapNode.appendChild(mapData)
		top_element.appendChild(mapNode)
	
		violationNode = root.createElement("Violation")
		violationData = root.createTextNode(self.vViolation)
		violationNode.appendChild(violationData)
		top_element.appendChild(violationNode)
		
		viocssNode = root.createElement("viocss")
		if (self.vViolation == "Hazardous Materials Violation"):
			viocssText = "config/hazMatViolation.css"
		elif (self.vViolation == "Trash Violation"):
			viocssText = "config/trashViolation.css"
		elif (self.vViolation == "Lawn Violation"):
			viocssText = "config/lawnViolation.css"
		viocssData = root.createTextNode(viocssText)
		viocssNode.appendChild(viocssData)
		top_element.appendChild(viocssNode)
	
		#print self.dateyearint.get(), self.datemonthint.get(), self.datedayint.get()
		dateNode = root.createElement("Date")
		dateNodeMonthNode = root.createElement("Month")
		dateNodeMonthData = root.createTextNode(str(self.vDate.month))
		dateNodeMonthNode.appendChild(dateNodeMonthData)
		dateNode.appendChild(dateNodeMonthNode)
		dateNodeDayNode = root.createElement("Day")
		dateNodeDayData = root.createTextNode(str(self.vDate.day))
		dateNodeDayNode.appendChild(dateNodeDayData)
		dateNode.appendChild(dateNodeDayNode)
		dateNodeYearNode = root.createElement("Year")
		dateNodeYearData = root.createTextNode(str(self.vDate.year))
		dateNodeYearNode.appendChild(dateNodeYearData)
		dateNode.appendChild(dateNodeYearNode)
		top_element.appendChild(dateNode)
	
		xmlString = root.toprettyxml()
		print xmlString
		xmlFile = open(filename_string, 'w')
		xmlFile.write(xmlString)
		xmlFile.close()
		
		return
	
	def read_from_xml(self, filename_string):
		
		xmlFile = open(filename_string, 'r')
		xmlDOM = mxml.parse(xmlFile)
		
		# Get Values and strip xml whitespace
		fnameNode = xmlDOM.getElementsByTagName('FName')
		self.vFirstName = fnameNode[0].firstChild.nodeValue.strip()
		
		minitNode = xmlDOM.getElementsByTagName('MINIT')
		self.vMidInitial = minitNode[0].firstChild.nodeValue.strip()
		
		lnameNode =  xmlDOM.getElementsByTagName('LName')
		self.vLastName = lnameNode[0].firstChild.nodeValue.strip()
		
		prefixNode = xmlDOM.getElementsByTagName('Prefix')
		self.vNamePrefix = prefixNode[0].firstChild.nodeValue.strip()
		
		addressoneNode = xmlDOM.getElementsByTagName('Addr1')
		self.vAddressLineOne = addressoneNode[0].firstChild.nodeValue.strip()
		
		addresstwoNode = xmlDOM.getElementsByTagName('Addr2')
		self.vAddressLineTwo = addresstwoNode[0].firstChild.nodeValue.strip()
		
		cityNode = xmlDOM.getElementsByTagName('City')
		self.vCity = cityNode[0].firstChild.nodeValue.strip()
		
		stateNode = xmlDOM.getElementsByTagName('State')
		self.vState = stateNode[0].firstChild.nodeValue.strip()
		
		zipNode = xmlDOM.getElementsByTagName('Zip')
		self.vZipCode = zipNode[0].firstChild.nodeValue.strip()
	
		maddressoneNode = xmlDOM.getElementsByTagName('MAddr1')
		self.vmAddressLineOne = maddressoneNode[0].firstChild.nodeValue.strip()
		
		maddresstwoNode = xmlDOM.getElementsByTagName('MAddr2')
		self.vmAddressLineTwo = maddresstwoNode[0].firstChild.nodeValue.strip()
		
		mcityNode = xmlDOM.getElementsByTagName('MCity')
		self.vmCity = mcityNode[0].firstChild.nodeValue.strip()
		
		mstateNode = xmlDOM.getElementsByTagName('MState')
		self.vmState = mstateNode[0].firstChild.nodeValue.strip()
		
		mzipNode = xmlDOM.getElementsByTagName('MZip')
		self.vmZipCode = mzipNode[0].firstChild.nodeValue.strip()
		
	
		mapNode = xmlDOM.getElementsByTagName('Map')
		self.vMapNumber = mapNode[0].firstChild.nodeValue.strip()
		
		violationNode = xmlDOM.getElementsByTagName('Violation')
		self.vViolation = violationNode[0].firstChild.nodeValue.strip()
		
		#Date Shenanigans
		datemonthNode = xmlDOM.getElementsByTagName('Month')
		month = int(datemonthNode[0].firstChild.nodeValue)
		
		datedayNode = xmlDOM.getElementsByTagName('Day')
		day = int(datedayNode[0].firstChild.nodeValue)
		
		dateyearNode = xmlDOM.getElementsByTagName('Year')
		year = int(dateyearNode[0].firstChild.nodeValue)
		
		self.vDate = datetime.date(year, month, day)
		
		"""
		print "---------------Equality Testing--------------------"
		print "Remove for final Release"
		if self.vAddressLineOne != self.vmAddressLineOne:
			print "fail Addr1"
		if self.vAddressLineTwo != self.vmAddressLineTwo:
			print "fail Addr2"
		if self.vCity != self.vmCity:
			print "fail City"
		if self.vState != self.vmState:
			print "fail State"
		if self.vZipCode != self.vmZipCode:
			print "fail Zip"
		"""
		return
