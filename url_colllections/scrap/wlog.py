import logging



def log_info(filename):
	
    logging.basicConfig(filename=filename,level= logging.INFO)


def result(e:Exception):
    logging.exception(str (e))