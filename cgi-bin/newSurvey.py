#!/usr/bin/python
import cgi
import cgitb
import ps


cgitb.enable(display=0, logdir="/log")

form = cgi.FieldStorage() 
title  = form.getvalue('surveyName')


#open file for overwriting



try:
	f = open("../survey.ssv", "w")
	f.write(str(title))
	f.write("\n")
	f.close()
	
	print "Content-type:text/html\r\n\r\n"
	print '<html><head><title>Create Survey - Otaku High Five!</title></head>'
	print '<body bgcolor="white" text="black" background="../background.jpg"><center>'
	print '<h1 style="color:#FFB873; font-family:COURIER NEW; font-size:50;">Create a Survey</h1><center><img src="../doge_r.gif" />'
	print '<p style ="color:#333399; font-family:PERPETUA;">Directions on how to create a survey:<br>'
	print '1. Think a name of your survey.<br>2.Then, input your questions :D<br>3.  Using ADD to add a question<br>4.  Using NEW to create a new survey <br></p>'
	print '<table><tr><td><form name="input2" action="./addQuestion.py" method="get" style ="color:#333399; font-family:PERPETUA;">'
	ps.ps()
	print "Question#?: <input type='text' name='question'> <br><br>"
	print "<center><input type='submit' value='ADD'></center><br><br></form></td></tr></table>"
	print "<br><form name='input3' action='./cgi-bin/endSurvey.py' method='get'><input type='Submit' value='Done'></form>"
	print '<a href="index.html">Go back to Welcome Page</a>'
	print '<p><img src="../coverphoto.jpg" height="35%" width="80%"></p></center></body></html>'
	
	f = open("../results.ssv", "w") #Deleted the old result data
	f.close()
except IOError:
	print 'error: Cannot create the survey'


