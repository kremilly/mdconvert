#!/usr/bin/python3

import re

def find(string, find):
    if string.find(find) != -1:
        return True
    else:
        return False

def is_url(string, check_protocol = True):
    url_pattern_check_protocol = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    url_pattern = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    
    if check_protocol == True:
        if re.match(url_pattern_check_protocol, string) != None:
            return True
        else:
            return False
    elif check_protocol == False:
        if re.match(url_pattern, string) != None:
            return True
        else:
            return False

def removeExtension(file):
    return file.rsplit(".", 1)[0]
