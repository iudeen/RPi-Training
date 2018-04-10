import urllib
def read_text():
    mytxt = open("C:\Users\DELL\Desktop\myfile.txt")
    readtxt = mytxt.read()
    mytxt.close()
    chkprof(readtxt)
    
def chkprof(toc):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+toc)
    op = conn.read()
    #print(op)
    conn.close()
    if "true" in op:
        print("Profanity")
    elif "false" in op:
        print("No Profanity")
    else:
        print("Error")
        
read_text()
