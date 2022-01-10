#!/usr/bin/env python3
import os
import re

print("HTTP/1.0 200 OK")
print("Content-type: text/html\n")
print("<html><body>")
print("Hello Python Script!<br>")

print("<hr>")
print("<pre>")
for env in sorted(os.environ):
    if re.match('^HTTP',env):
        print('["' + env +  '"] => ' +os.environ.get(env))

print("")
 
for env in sorted(os.environ):
    if not re.match('^HTTP',env):
        print('["' + env +  '"] => ' +os.environ.get(env))

print("")
print("</pre>")
print("</body></html>")
