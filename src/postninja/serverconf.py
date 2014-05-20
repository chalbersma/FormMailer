# serverconf

from Tkinter import *
import xml.dom.minidom as mxml

class serverconf:
	def __init__(self, parent):

		top = self.top = Toplevel(parent)

		frame = Frame(top)
		frame.grid(column=0, row=0, columnspan=4)

		self.serverconflabel = Label(frame, text="Server")
		self.serverconflabel.grid(row=0)

		self.serverconftext = StringVar()
		self.serverconf = Entry(frame, textvariable=self.serverconftext)
		self.serverconf.grid(row=0, column=1)

		self.serverunamelabel = Label(frame, text="Username")
		self.serverunamelabel.grid(row=1)

		self.serverunametext = StringVar()
		self.serveruname = Entry(frame, textvariable=self.serverunametext)
		self.serveruname.grid(row=1, column=1)
		
		self.serverpaswdlabel = Label(frame, text="Password")
		self.serverpaswdlabel.grid(row=2)
		
		self.serverpaswdtext = StringVar()
		self.serverpaswd = Entry(frame, textvariable=self.serverpaswdtext, show="*")
		self.serverpaswd.grid(row=2, column=1)

		self.serverconfdo = Button(frame, text="Write New Server Info", command=self.do)
		self.serverconfdo.grid(row=3, column=0, columnspan=2)
		return

	def do(self):
		
		newdom = mxml.getDOMImplementation()
		
		root = newdom.createDocument(None, "serverconf", None)

		top_element = root.documentElement
		
		serverNameNode = root.createElement("Server")
		serverNameData = root.createTextNode(self.serverconftext.get())
		serverNameNode.appendChild(serverNameData)
		top_element.appendChild(serverNameNode)
		
		serverUNameNode = root.createElement("Uname")
		serverUNameData = root.createTextNode(self.serverunametext.get())
		serverUNameNode.appendChild(serverUNameData)
		top_element.appendChild(serverUNameNode)
		
		serverPaswdNode = root.createElement("Paswd")
		serverPaswdData = root.createTextNode(self.serverpaswdtext.get())
		serverPaswdNode.appendChild(serverPaswdData)
		top_element.appendChild(serverPaswdNode)
		
		xmlString = root.toprettyxml()
		print xmlString
		xmlFile = open("conf/serverconf.xml", 'w')
		xmlFile.write(xmlString)
		xmlFile.close()
		
		
		self.top.destroy()
		return

