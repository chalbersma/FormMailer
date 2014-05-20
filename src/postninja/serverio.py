# Server I/O materials
from data import vData
import xml.dom.minidom as mxml

class serverIO:
	#add universal data bits and pieces
	
	self.serveraddress
	
	self.serveruname
	
	self.serverpaswd
	
	# This should include all the neccessary functions to connect to the psql db

	def load_serverconf(self):
		
		xmlFile = open("conf/serverconf.xml", 'r')
		
		xmlDOM = mxml.parse(xmlFile)
		
		serverNameNode = xmlDOM.getElementsByTagName('Server')
		self.vFirstName = serverNameNode[0].firstChild.nodeValue.strip()
		
		unameNode = xmlDOM.getElementsByTagName('Uname')
		self.serveruname = unameNode[0].firstChild.nodeValue.strip()
		
		paswdNode =  xmlDOM.getElementsByTagName('Paswd')
		self.serverpaswd = paswdNode[0].firstChild.nodeValue.strip()
		
		return
		
