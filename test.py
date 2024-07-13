from xml.dom.minidom import parseString

f = open("test.html", "r")
contents = f.read()
f.close()

document = parseString(contents)
all_li = document.getElementsByTagName("li")
all_projects_li = all_li[4:-1]
new_msg = "Projects: \n"
for project_li in all_projects_li:
    new_msg += f"{project_li.getAttribute('status')} - {project_li.getAttribute('name')}\n"
new_msg += """---
✅ - Source code of project is available, and it works/worked
⚠️ - Maybe broken
⏳ - Currently working on it
❌ - I decided to not do this project
🗓 - Planned project
"""
print(new_msg)