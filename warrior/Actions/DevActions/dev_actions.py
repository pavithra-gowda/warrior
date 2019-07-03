import Framework.Utils as Utils
from Framework.Utils import data_utils
from Fremework.Utils.testcase_Utils import pNote




class MyActions(object):

    """" Default __init__ field must be used when using classes for keywords """
    def __init__(self):
        self.resultfile = Utils.config_Utils.resultfile
        self.datafile = Utils.config_Utils.datafile
        self.logsdir = Utils.config_Utils.logsdir
        self.filename = Utils.config_Utils.filename
        self.logfile = Utils.config_Utils.logfile

    def full_name(self, student, first_name= 'first', last_name= 'last', full_name= 'first last'):
        """
        combine first and last name
        """
        # status will be used to save the status of the test that wheather it is failed or pass
        status = True
        # we will return the dictionary of keys and value to maintain the logs
        log_dic={}
        wdesc= 'combine first and last name'
        full_name = None

        data = data_Utils.get_credentials(self.datafile, student, [first_name, last_name, full_name])
        if first_name and last_name:
            pNote("first name is {0}".format(first_name))
            pNote("last name is {0}".format(last_name))
            temp_full_name = first_name + ' ' + last_name
            if temp_full_name != full_name:
                status= False
            pNote('full name is {0}'.format(full_name))
        else:
            pNote("names are not provided")
            status = False

        log_dic["student"]= student
        log_dic["first_names"]= first_name
        log_dic["second_name"]= second_name
        log_dic["full_name"]= full_name
        return status, log_dic
