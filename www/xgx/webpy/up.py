#!/usr/bin/python  
import cgi, cgitb  
import MySQLdb  

form = cgi.FieldStorage()  

name = form.getvalue('name')
passwd  = form.getvalue('passwd')  

'''
db = MySQLdb.connect("localhost","root","123456","web")
cursor = db.cursor()
cursor.execute("insert into users (name,passwd) values( '%s',%s);"%(name,passwd))
db.commit()
db.close()
'''

print "Content-type:text/html\r\n\r\n"  
print "<html>"  
print "<head>"  
print "<title>Hello - CGI</title>"  
print "</head>"  
print "<body>"  
print "<h2>Hello %s %s</h2>" % (name, passwd)  
print "</body>"  
print "</html>" 
