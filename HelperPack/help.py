# this file contains standalone method that requires help to other classes.

def getStopWords():
    custom_stop_words = set()
    file_to_read = open('static/google_long_list_stop_words.txt','r')
    lines = file_to_read.readlines()
    file_to_read.close()

    for line in lines:
        custom_stop_words.add(line[:-1])

    return custom_stop_words