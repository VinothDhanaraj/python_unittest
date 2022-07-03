import logging

def getstring(): #defining the function to be tested
    return "Vinoth"

def simple_interest(p,i,n): #defining the function to be tested
    return p*i*n
	
def divide_by_zero(a,b): #defining the function to be tested
	c=a/b
	return c
	

def loginfo(): #defining the function to be tested
	logger = logging.getLogger('Vinoth logs')
	logger.warning('Vinoth warning msg')
	logger.notset('Vinoth not set msg')
	logger.debug('Vinoth debug msg')
	logger.info('Vinoth info msg')
	logger.error('Vinoth error msg')

# ...

