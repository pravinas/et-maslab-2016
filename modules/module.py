# module.py
#
# Abstract superclass for the modules in this program.

class Module():
	
	## Start the module. Set initial conditions to useful values.
	def start(self):
		raise NotImplementedError

	## Run the module. This is called once each loop.
	#
	# @return	The next module which the program calls.
	def run(self):
		raise NotImplementedError

    ## Return True if there was an error in initialization, False otherwise.
	def checkForInitializationErrors(self):
		return False