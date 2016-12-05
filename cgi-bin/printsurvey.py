def ps():
	f = open("../survey.ssv", "r")
	lines = f.readlines()
	f.close()
	print '<h1 style ="color:#330066; font-family:PERPETUA;">%s</h1>' % lines[0].strip()
	print '<table width="80%" style ="color:#000000; font-family:PERPETUA;">'
	n = 0
	for line in lines[1:]:
		sline = line.strip()
		n += 1
		print "<tr>"
		print '<td width="100%%">Q%d. %s</td>' % (n, sline)
		print '</tr>'
	print "</table>"
