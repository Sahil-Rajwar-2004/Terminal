import subprocess
import datetime
import webbrowser
from about import author,version,homepage
import sys
import os

current_date = datetime.date.today()
current_day = current_date.strftime("%A")
print(f"{current_date} {current_day}")

running = True

while running:
    cwd = os.getcwd()
    cmd = input(f"[{cwd}]: ")
    if cmd.startswith("exit"):
        running = False

    if cmd.startswith("about"):
        about = f"""author {author}
version: {version}
homepage: {homepage}
"""
        print(about)
        continue

    if cmd.startswith("version"):
        print(version)
        continue

    if cmd.startswith("homepage"):
        webbrowser.open(homepage)
        continue

    if cmd.startswith("author"):
        print(author)
        continue

    if cmd.startswith("search "):
        name = cmd[7:].strip()
        url = "https://www.bing.com/search?q="+name
        webbrowser.open(url)
        continue

    if cmd.startswith("cd "):
        dir_ = cmd[3:].strip()
        try:
            os.chdir(dir_)
        except FileNotFoundError:
            print(f"directory not found! {dir_}")
        continue

    try:
        result = subprocess.run(cmd,shell = True,capture_output = True,text = True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr,file = sys.stderr)
    except FileNotFoundError:
        print(f"invalid command: {cmd}")

