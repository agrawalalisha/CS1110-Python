# Alisha Agrawal (aa3se) Hannah Bowen (heb6ct) Reese Quillian (rlq3fm)
import urllib.request
import re

# (\w+(\S+)?@\S+(\.)?(\S)?\.\w{2,})
# (\w+(\d+)?(-+)?(\.+)?(\w+)?@\S+(\.)?(\S)?\.\w{2,})
# (\w+(\d+)?(-+)?(\.+)?(\w+)?@\w+(-+)?(\.)?(\w+)?\.\w{2,})

search_email = r"(\w+((\d+)?(-+)?(\.+)?(\w+))+?(@| at )\w+(-+)?(\.)?(\w+)?\.[a-zA-Z]{2,})"
search_email_finder = re.compile(search_email)
stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')
new_list = []
for line in stream:
    decoded = line.decode('UTF-8').strip()
    matches = search_email_finder.finditer(decoded)
    for match in matches:
        if match.group(1) is not None:
            if match.group(1) not in new_list:
                if " at " in match.group(1):
                    match.group(1).replace(" at ", "@")
                new_list.append(match.group(1))

for email in new_list:
    print(email + "\n")