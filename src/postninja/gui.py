from Tkinter import *
import tkFileDialog as tkiowin
from data import vData
from staticdata import S_VIOLATIONS
from staticdata import S_STATES
from staticdata import S_MO
from serverconf import serverconf
import datetime
import os

class GUI:
	def __init__(self, master):
		
		self.upfromme=master
		
		frame = Frame(master)
		frame.grid(column=0, row=0, columnspan=4)
		#frame.pack()
		
		#Menu
		self.menu = Menu(master)
		master.config(menu = self.menu)
		
		self.filemenu = Menu(self.menu)
		self.menu.add_cascade(label="File", menu=self.filemenu)
		self.filemenu.add_command(label = "New", command=self.clearForm)
		self.filemenu.add_command(label = "Open...", command=self.openFile)
		self.filemenu.add_command(label = "Save As", command=self.saveFile)
		self.filemenu.add_command(label="Exit", command=quit)
		
		self.toolsmenu = Menu(self.menu)
		self.menu.add_cascade(label="Tools", menu=self.toolsmenu)
		self.toolsmenu.add_command(label = "Set Server", command=self.serverConf)
		
		
		#Name Framework
		self.fnametext = StringVar()
		self.fnamelabel = Label(frame, text="First Name")
		self.fnamelabel.grid(row=0)
		#self.fnamelabel.pack()
		self.fname = Entry(frame, textvariable = self.fnametext)
		self.fname.grid(row=0, column=1)
		#self.fname.pack()
		
		self.lnametext = StringVar()
		self.lnamelabel = Label(frame, text="Last Name")
		self.lnamelabel.grid(row=1)
		#self.lnamelabel.pack()
		self.lname = Entry(frame, textvariable = self.lnametext)
		self.lname.grid(row=1, column=1)
		#self.lname.pack()
		
		self.minittext = StringVar()
		self.minitlabel = Label(frame, text="Middle Initial")
		self.minitlabel.grid(row=2)
		#self.minitlabel.pack()
		self.minit = Entry(frame, width=1, textvariable = self.minittext)
		self.minit.grid(row=2, column=1)
		#self.minit.pack()
		
		self.prefixtext = StringVar()
		self.prefixlabel = Label(frame, text="Name Prefix")
		self.prefixlabel.grid(row=3)
		#self.prefixlabel.pack()
		self.prefix = Entry(frame, width=5, textvariable = self.prefixtext)
		self.prefix.grid(row=3, column=1)
		self.prefix.delete(0, END)
		self.prefix.insert(0, "Mr.")
		self.prefix.update()
		#self.prefix.pack()
		
		#end of getting the name
		#Check button for extra Mailing Address
		self.issameaddrvalue = IntVar()
		self.issameaddr = Checkbutton(frame, text = "Same Mailing Address?", variable=self.issameaddrvalue, command=self.disable_mail_address)
		self.issameaddr.grid(row=4, column=0, columnspan=2)
		
		
		#Get the Address
		self.addressonetext = StringVar()
		self.addressonelabel = Label(frame, text="Addr 1")
		self.addressonelabel.grid(row=5)
		self.addressone = Entry(frame, textvariable = self.addressonetext)
		self.addressone.grid(row=5, column=1)
		#self.addressonelabel.pack()
		#self.addressone.pack()
		#Mailing
		self.maddressonetext = StringVar()
		self.maddressonelabel = Label(frame, text="Mail Addr 1")
		self.maddressonelabel.grid(row=5, column=2)
		self.maddressone = Entry(frame, textvariable = self.maddressonetext)
		self.maddressone.grid(row=5, column=3)
		
		
		self.addresstwotext = StringVar()
		self.addresstwolabel = Label(frame, text="Addr2")
		self.addresstwolabel.grid(row=6)
		self.addresstwo = Entry(frame, textvariable = self.addresstwotext)
		self.addresstwo.grid(row=6, column=1)
		#self.addresstwolabel.pack()
		#self.addresstwo.pack()
		self.maddresstwotext = StringVar()
		self.maddresstwolabel = Label(frame, text="Mail Addr 2")
		self.maddresstwolabel.grid(row=6, column=2)
		self.maddresstwo = Entry(frame, textvariable = self.maddresstwolabel)
		self.maddresstwo.grid(row=6, column=3)
		
		
		self.citytext = StringVar()
		self.citylabel = Label(frame, text="City")
		self.citylabel.grid(row=7)
		self.city = Entry(frame, textvariable = self.citytext)
		self.city.grid(row=7, column=1)
		#self.citylabel.pack()
		#self.city.pack()
		self.mcitytext = StringVar()
		self.mcitylabel = Label(frame, text="Mail City")
		self.mcitylabel.grid(row=7, column=2)
		self.mcity = Entry(frame, textvariable=self.mcitytext)
		self.mcity.grid(row=7, column=3)
		
		self.statetext = StringVar()
		self.statetext.set(S_MO[0]) # Make Missouri Default
		self.statelabel = Label(frame, text = "State")
		self.statelabel.grid(row=8)
		self.state = OptionMenu(frame, self.statetext, *S_MO)
		self.state.grid(row=8, column=1)
		#self.statelabel.pack()
		#self.state.pack()
		self.mstatetext = StringVar()
		self.mstatetext.set(S_STATES[0]) # Make MO Default
		self.mstatelabel = Label(frame, text = "Mail State")
		self.mstatelabel.grid(row=8, column=2)
		self.mstate = OptionMenu(frame, self.mstatetext, *S_STATES)
		self.mstate.grid(row=8, column=3)
		
		
		
		self.zipcodetext = StringVar()
		self.zipcodelabel = Label(frame, text = "Zip")
		self.zipcodelabel.grid(row=9)
		self.zipcode = Entry(frame, textvariable = self.zipcodetext)
		self.zipcode.grid(row=9, column=1)
		#self.zipcodelabel.pack()
		#self.zipcode.pack()
		self.mzipcodetext = StringVar()
		self.mzipcodelabel = Label(frame, text = "Mail Zip")
		self.mzipcodelabel.grid(row=9, column=2)
		self.mzipcode = Entry(frame, textvariable = self.mzipcodetext)
		self.mzipcode.grid(row=9, column=3)
		
		
		# End address
		
		# Start Map,Viol,Date
		
		self.mapcodetext = StringVar()
		self.mapcodelabel = Label(frame, text = "Map Code")
		self.mapcodelabel.grid(row=10)
		self.mapcode = Entry(frame, textvariable = self.mapcodetext)
		self.mapcode.grid(row=10, column=1)
		#self.mapcodelabel.pack()
		#self.mapcode.pack()
		
		#Being Replaced with an Option Menu
		self.violationtext = StringVar()
		self.violationtext.set(S_VIOLATIONS[0]) # makes the first the default value
		self.violationlabel = Label(frame, text = "Violation Type")
		self.violationlabel.grid(row=11)
		self.violation = OptionMenu(frame, self.violationtext, *S_VIOLATIONS)
		self.violation.grid(row=11, column=1)
		#self.violationlabel.pack()
		#self.violation.pack()
		#Being Replaced with an Option Menu
		
		self.today = datetime.date.today()
		self.datemonthint = IntVar()
		self.datedayint = IntVar()
		self.dateyearint = IntVar()
		self.datelabel = Label(frame, text = "Date (MM DD YYYY):")
		self.datelabel.grid(row=12, sticky=W)
		#self.datemonthlabel = Label(frame, text="Month")
		#self.datemonthlabel.grid(row=12, column=1)
		self.datemonth = Entry(frame, width=2, textvariable = self.datemonthint)
		self.datemonth.grid(row=12, column=1, sticky=W)
		self.datemonth.delete(0, END)
		if self.today.month < 10 :
			self.datemonth.insert(1, self.today.month)
		else:
			self.datemonth.insert(0, self.today.month)
		self.datemonth.update()
		#self.datedaylabel = Label(frame, text="Day")
		#self.datedaylabel.grid(row=12, column=2)
		self.dateday = Entry(frame, width=2, textvariable = self.datedayint)
		self.dateday.grid(row=12, column=1)
		self.dateday.delete(0, END)
		if self.today.day < 10 :
			self.dateday.insert(1, self.today.day)
		else:
			self.dateday.insert(0, self.today.day)
		self.dateday.update()
		#self.dateyearlabel = Label(frame, text="Year")
		#self.dateyearlabel.grid(row=12, column=3)
		self.dateyear = Entry(frame, width=4, textvariable = self.dateyearint)
		self.dateyear.grid(row=12, column=1, sticky=E)
		self.dateyear.delete(0, END)
		self.dateyear.insert(0, self.today.year)
		self.dateyear.update()
		#self.datelabel.pack()
		#self.date.pack()
		
		
		self.button = Button(frame, text="Create Letter", command=self.gen_button)
		self.button.grid(row=13, columnspan=2)
		
		self.upload = Button(frame, text="Create & Upload", command=self.noplement)
		self.upload.grid(row=13, column=2, columnspan=2)
		#self.button.pack()
		
		
	def disable_mail_address(self):
		if self.issameaddrvalue.get() == 1:
			self.maddressone.config(state="disable")
			self.maddressone.update
			self.maddresstwo.config(state="disable")
			self.maddresstwo.update
			self.mcity.config(state="disable")
			self.mcity.update
			self.mstate.config(state="disable")
			self.mstate.update
			self.mzipcode.config(state="disable")
			self.mzipcode.update
		else:
			self.maddressone.config(state="normal")
			self.maddressone.update
			self.maddresstwo.config(state="normal")
			self.maddresstwo.update
			self.mcity.config(state="normal")
			self.mcity.update
			self.mstate.config(state="normal")
			self.mstate.update
			self.mzipcode.config(state="normal")
			self.mzipcode.update
			
		return
		
	def noplement(self):
		print "This feature is not yet implemented"
		return

	def grab_data(self):
		print "Grabbing the Data"
		guidata = vData()
		guidata.vFirstName = self.fnametext.get()
		guidata.vLastName = self.lnametext.get()
		guidata.vMidInitial = self.minittext.get()
		guidata.vNamePrefix = self.prefixtext.get()
		
		
		guidata.vAddressLineOne = self.addressonetext.get()
		guidata.vAddressLineTwo = self.addresstwotext.get()
		guidata.vCity = self.citytext.get()
		guidata.vState = self.statetext.get()
		guidata.vZipCode = self.zipcodetext.get()
	
		guidata.vMapNumber = self.mapcodetext.get()
	
		#Being Replaced with an Option Menu
		
		
		guidata.vViolation = self.violationtext.get()
		#Being Replaced with an Option Menu
		#Prepare Date Then get date
		print self.dateyearint.get(), self.datemonthint.get(), self.datedayint.get()
		tempdate = datetime.date(self.dateyearint.get(), self.datemonthint.get(), self.datedayint.get())
		guidata.vDate = tempdate
		
		if self.issameaddrvalue.get() == 1 :
			# Make the values from address the ones for mailing address
			guidata.vmAddressLineOne = self.addressonetext.get()
			guidata.vmAddressLineTwo = self.addresstwotext.get()
			guidata.vmCity = self.citytext.get()
			guidata.vmState = self.statetext.get()
			guidata.vmZipCode = self.zipcodetext.get()
		else:
			# Grab the values for the seperate and distinct mailing address
			guidata.vmAddressLineOne = self.maddressonetext.get()
			guidata.vmAddressLineTwo = self.maddresstwotext.get()
			guidata.vmCity = self.mcitytext.get()
			guidata.vmState = self.mstatetext.get()
			guidata.vmZipCode = self.mzipcodetext.get()
		
		#guidata.print_to_console()
  		return guidata

	def write_data(self, dataToWrite):
		
		#Update GUI with data from a vData Object
		self.fname.delete(0, END)
		self.fname.insert(0, dataToWrite.vFirstName)
		self.fname.update()
		
		self.minit.delete(0, END)
		self.minit.insert(0, dataToWrite.vMidInitial)
		self.minit.update()
		
		self.lname.delete(0, END)
		self.lname.insert(0, dataToWrite.vLastName)
		self.lname.update()
		
		self.prefix.delete(0, END)
		self.prefix.insert(0, dataToWrite.vNamePrefix)
		self.prefix.update()
		
		self.addressone.delete(0, END)
		self.addressone.insert(0, dataToWrite.vAddressLineOne)
		self.addressone.update()
		
		self.addresstwo.delete(0, END)
		self.addresstwo.insert(0, dataToWrite.vAddressLineTwo)
		self.addresstwo.update()
		
		self.city.delete(0, END)
		self.city.insert(0, dataToWrite.vCity)
		self.city.update()
		
		#self.state.delete(0, END)
		#State is always MO
		#self.statetext  = dataToWrite.vState
		self.state.update()
		
		self.zipcode.delete(0, END)
		self.zipcode.insert(0, dataToWrite.vZipCode)
		self.zipcode.update()
		
		if (dataToWrite.vmAddressLineOne == dataToWrite.vAddressLineOne and dataToWrite.vmAddressLineTwo == dataToWrite.vAddressLineTwo
			and dataToWrite.vmCity == dataToWrite.vCity and dataToWrite.vmState == dataToWrite.vState and dataToWrite.vmZipCode == dataToWrite.vZipCode):
			#Empty any Current Data
			self.maddressone.delete(0, END)
			self.maddressone.update()
			
			self.maddresstwo.delete(0, END)
			self.maddresstwo.update()
			
			self.mcity.delete(0, END)
			self.mcity.update()
			
			#self.mstate.delete(0, END)
			#self.mstate.update()
			
			self.mzipcode.delete(0, END)
			self.mzipcode.update()
			
			# Then check the box
			self.issameaddr.select()
			self.issameaddr.update()
			
			# Update bits and pieces
			self.disable_mail_address()
			
		else:
			# Then leave the box unchecked
			self.issameaddr.deselect()
			self.issameaddr.update()
			self.disable_mail_address()
			
			# And write the unique address
			self.maddressone.delete(0, END)
			self.maddressone.insert(0, dataToWrite.vmAddressLineOne)
			self.maddressone.update()
			
			self.maddresstwo.delete(0, END)
			self.maddresstwo.insert(0, dataToWrite.vmAddressLineTwo)
			self.maddresstwo.update()
			
			self.mcity.delete(0, END)
			self.mcity.insert(0, dataToWrite.vmCity)
			self.mcity.update()
			
			#self.mstate.delete(0, END)
			self.mstatetext.set(dataToWrite.vmState)
			self.mstate.update()
			
			self.mzipcode.delete(0, END)
			self.mzipcode.insert(0, dataToWrite.vmZipCode)
			self.mzipcode.update()
	
		self.mapcode.delete(0, END)
		self.mapcode.insert(0, dataToWrite.vMapNumber)
		self.mapcode.update()
			
		#self.violation.delte(0, END)
		self.violationtext.set(dataToWrite.vViolation)
		self.violation.update()
		
		self.datemonth.delete(0, END)
		self.datemonth.insert(0, dataToWrite.vDate.month)
		self.datemonth.update()
		
		
		self.dateday.delete(0, END)
		self.dateday.insert(0, dataToWrite.vDate.day)
		self.dateday.update()
			
		self.dateyear.delete(0, END)
		self.dateyear.insert(0, dataToWrite.vDate.year)
		self.dateyear.update()
		
		return

	def openFile(self):
		
		fileNameToOpen = tkiowin.askopenfilename(defaultextension=".xml", title="Open a Violation - PostNinja", filetypes = [("XML files" , "*.xml"), ("All Files" , "*.*")] )
		#print "Opening File"  + fileNameToOpen
		
		guidata = vData()
		guidata.read_from_xml(fileNameToOpen)
		self.write_data(guidata)
		
		return
	

		
	def saveFile(self):
		## Save the file to a specific point
		
		guidata = self.grab_data()
		filename = tkiowin.asksaveasfilename(defaultextension=".xml", title="Save the Violation - PostNinja", filetypes = [("XML files" , "*.xml"), ("All Files" , "*.*")] )
		guidata.save_to_xml(filename)
		
		
		return filename
		
	def clearForm(self):
		## Clear the variables
		self.fname.delete(0, END)
		self.fname.update()
		
		self.minit.delete(0, END)
		self.minit.update()
		
		self.lname.delete(0, END)
		self.lname.update()
		
		self.prefix.delete(0, END)
		self.prefix.update()
		
		self.addressone.delete(0, END)
		self.addressone.update()
		
		self.addresstwo.delete(0, END)
		self.addresstwo.update()
		
		self.city.delete(0, END)
		self.city.update()
		
		#self.state.delete(0, END)
		#State is always MO
		#self.statetext  = dataToWrite.vState
		self.state.update()
		
		self.zipcode.delete(0, END)
		self.zipcode.update()
		
		self.issameaddr.deselect()
		self.disable_mail_address()
		
		self.maddressone.delete(0, END)
		self.maddressone.update()
		
		self.maddresstwo.delete(0, END)
		self.maddresstwo.update()
		
		self.mcity.delete(0, END)
		self.mcity.update()
		
		#self.mstate.delete(0, END)
		#self.mstate.update()
		
		self.mzipcode.delete(0, END)
		self.mzipcode.update()
		
		# Then check the box
		self.issameaddr.select()
		self.issameaddr.update()
		
		# Update bits and pieces
		self.disable_mail_address()
	
		self.mapcode.delete(0, END)
		self.mapcode.update()
			
		self.violation.update()
		
		self.datemonth.delete(0, END)
		self.datemonth.update()
		
		
		self.dateday.delete(0, END)
		self.dateday.update()
			
		self.dateyear.delete(0, END)
		self.dateyear.update()
		
		
		
		return
		
	def launch_browser(self, guidata):
		guidata.save_to_xml("./pndata/tmp.xml")
		try:
			os.startfile("./pndata/tmp.xml")
		except:
			try: #Try Mozilla (we must be using a unix system)
				os.system("firefox ./pndata/tmp.xml &")
			except:
				try: #Try Chrome
					os.system("chrome ./pndata/tmp.xml &")
				except:
					try: #Try Opera
						os.system("opera ./pndata/tmp.xml &")
					except:
						try: #Try Konqueror
							os.system("konqueror ./pndata/tmp.xml &")
						except:
							pass #I've given up
			
		return
		
	def gen_button(self):
	
		guidata = self.grab_data()
		self.launch_browser(guidata)
	
	
		return
		
	def serverConf(self):
		
		popup = serverconf(self.upfromme)
		self.upfromme.wait_window(popup.top)
		
		return

	
