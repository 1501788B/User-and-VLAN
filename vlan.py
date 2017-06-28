#!/usr/bin/python

import vymgmt

def createvlan(interface, number, description, address):
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.set("interfaces ethernet %b vif %b description %b" %(interface, number, description))
	vyos.set("interfaces ethernet %b vif %b address %b" %(interface, number, address))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def deletevlan( interface, number):
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("interfaces ethernet %b vif %b" %(interface, number))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def readvlan():
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
	vyos.login()
	print vyos.run_op_mode_command("show interface")
	vyos.exit()
	vyos.logout()

def updatevlan(interface, number, description, address):
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("interfaces ethernet %b vif %b" %(interface, number))
	vyos.set("interfaces ethernet %b vif %b description %b" %(interface, number, description))
	vyos.set("interfaces ethernet %b vif %b address %b" %(interface, number, address))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()
