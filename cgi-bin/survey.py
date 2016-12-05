#!/usr/bin/python
import cgi
import cgitb
cgitb.enable(display=0, logdir="/log")

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Take a survey - Otaku High Five !</title>"
print "</head>"
print "<body bgcolor=\'white\' text=\'black\' background=\'../background.jpg\'>"
print "<center>"

try:
	f = open("../survey.ssv", "r")
	lines = f.readlines()
	print '<h1 style ="color:#330066; font-family:PERPETUA;">%s</h1>' % lines[0].strip()
	print '<form action="result.py" method="post">'
	print '<table width="80%" style ="color:#000000; font-family:PERPETUA;">'

	n = 0
	for line in lines[1:]:
		sline = line.strip()
		n += 1
		print "<tr>"
		print '<td width="50%%">Q%d. %s</td>' % (n, sline)
		print '<td width="15%%"><input type="radio" name="%d" value="1" checked>Strongly agreed</td>' % n
		print '<td width="10%%"><input type="radio" name="%d" value="2">Agreed</td>' % n
		print '<td width="10%%"><input type="radio" name="%d" value="3">Disagreed</td>' % n
		print '<td width="15%%"><input type="radio" name="%d" value="4">Disagreed strongly</td>' % n
		print '</tr>'

	print "</table>"
	print '<br><input type ="submit" value="Submit Survey">'
	print '<input type="hidden" name="fill" value="1">'
	print "</form>"
	print "<br>"
	print "<br>"
	print '<form action="result.py" method="post">'
	print '<input type ="submit" value="Skip Survey and see the result">'
	print '<input type ="button" value ="Return to Welcome Page" onclick ="location.href =\'../index.html\'" />'
	print '<input type="hidden" name="fill" value="0">'
	print "</form>"
	f.close()
	
except:
	print "<h1>Are you kidding me? There is NO SURVEY!</h1>"
print '<p><img src="../coverphoto.jpg" height="35%" width="80%"></p>'
print "</center>"
print "</body>"
print "</html>"
