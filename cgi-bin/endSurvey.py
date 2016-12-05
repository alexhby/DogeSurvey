#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()   # enable debugging mode

print "Content-type:text/html\r\n\r\n"
print '<html><head><title>Your survey is DONE - Otaku High Five!</title></head>'
print '<body bgcolor="white" text="black" background="../background.jpg"><center>'
print '<h1 style="color:#FFB873; font-family:COURIER NEW; font-size:50;">Your survey is DONE</h1><center><img src="../doge_r.gif" />'

print '</table><h1 style ="color:#330066; font-family:PERPETUA;">Menu</h1>'
print '''<br><table width="60%"><tr><td align="right"><input type ="button" style="width: 200px;" value ="Go back to Welcome Page" onclick ="location.href ='../index.html'" /></td>'''
print '''<td align="center" width="210px"><input type ="button" style="width: 200px;" value ="Go to Create Survey Page" onclick ="location.href ='../createSurvey.html'"\/></td>'''
print '''<td align="left"><input type ="submit" style="width: 200px;" value ="Back to Take Survey" onclick ="location.href ='survey.py'"/></td></tr></table>'''


print '<p><img src="../coverphoto.jpg" width="85%" height="55%"/></p></center></body></html>'
