#!/usr/bin/python
import cgi
import cgitb
cgitb.enable(display=0, logdir="/log")
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Take a survey - Otaku High Five !</title>"
print "</head>"
print "<body bgcolor=\'white\' text=\'black\' background=\'../background.jpg\'>"
print "<center>"

f = open("../survey.ssv", "r")
lines = f.readlines()
f.close()

g = open("../results.ssv", "a+")
if form.getvalue('fill') == '1':
	for n in range(len(lines)-2):
		tmp = form.getvalue(str(n+1))
		g.write(tmp)
		g.write(" ")
	tmp = form.getvalue(str(len(lines)-1))
	g.write(tmp)
	g.write("\n")
	
g.seek(0)
stat = []
for n in range(len(lines)-1):
	stat.append({'1':0, '2':0, '3':0, '4':0})
for line in g:
	tline = line.split()
	for n,ch in enumerate(tline):
		stat[n][ch] += 1
g.close()

print '<h1 style ="color:#330066; font-family:PERPETUA;">%s</h1>' % lines[0].strip()
print '<table width="80%" style ="color:#000000; font-family:PERPETUA;">'
n = 0
for line in lines[1:]:
	sline = line.strip()
	maxcount = -1
	avg = (stat[n]['1']+stat[n]['2']*2+stat[n]['3']*3+stat[n]['4']*4)/float(stat[n]['1']+stat[n]['2']+stat[n]['3']+stat[n]['4'])
	options = ['Strongly agreed', 'Agreed', 'Disagreed', 'Disagreed strongly']
	print "<tr>"
	print '<td width="50%%">Q%d. %s</td>' % (n+1, sline)
	print '<td width="50%%">Strongly agreed: %d, Agreed: %d, Disagreed: %d, Disagreed strongly: %d,<br> Average: %.2f close to %s</td>' % (stat[n]['1'], stat[n]['2'], stat[n]['3'], stat[n]['4'], avg, options[int(round(avg))-1])
	
	print '</tr>'
	n += 1
print "</table>"

print "<br>"
print "<br>"
print '<input type ="button" value ="Return to Welcome Page" onclick ="location.href =\'../index.html\'" />'

print '<p><img src="../coverphoto.jpg" height="35%" width="80%"></p>'
print "</center>"
print "</body>"
print "</html>"
