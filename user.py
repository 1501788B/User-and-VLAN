#!/usr/bin/python

import vymgmt

def createuser(name, fullname, userlevel, password):
	vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos',port=22)
	vyos.login()
	vyos.configure()
	vyos.set("system login user %a fullname %a" %(name, fullname))
	vyos.set("system login user %a authentication plaintext-password %a" %(name, password))
	vyos.set("system login user %a level %a" %(name, userlevel))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def deleteuser(name):
	vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("system login user %a" %(name))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def readuser():
	vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.run_op_mode_command("show system login users")
	vyos.commit()
	vyos.save()
	vyos.exit() 
	vyos.logout()

def updateuser(name, fullname, password, userlevel):
	vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete ( "system login user %a" %(name))
	vyos.set("system login user %a fullname %a" %(name, fullname))
	vyos.set("system login user %a authentication plaintext-password %a" %(name, password))
	vyos.set("system login user %a level %a" %(name, userlevel))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()