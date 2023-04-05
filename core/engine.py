#!/usr/bin/python3

import sys
from core.utils import *
from urllib import request
import markdown2, pathlib, os
from colorama import init, Fore
from urllib.request import urlopen

init(autoreset=True)

def download_read_delete(url):
    file_location = pathlib.Path.home() / "Downloads\style.css"
    request.urlretrieve(url, file_location)
    content = open(file_location).read()
    os.remove(file_location)
    return content

def get_css(input):
    if find(input, 'css'):
        if is_url(input):
            try:
                return download_read_delete(input)
            except:
                print(f"{Fore.RED}Error: {input} not exist")
        else:
            cssin = open(input)
            return cssin.read()
    else:
        sys.exit(f"{Fore.RED}Error: This is not a css file")
    
def convert(file, style):
    if find(file, 'md') != True:
        sys.exit(f"{Fore.RED}Error: This is not a markdown file")
        
    if not style or style == "no-style":
        css = ""
    else:
        css = get_css(style)
    
    DEFAULT_EXTRAS = [
        'fenced-code-blocks',
        'footnotes',
        'metadata',
        'cuddled-lists',
        'pyshell',
        'smarty-pants',
        'spoiler',
        'tables'
    ]

    output = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <style type="text/css">
    """

    output += css

    output += """
        </style>
    </head>
    <body>
    """
    mkin = open(file, errors="ignore")
    output += markdown2.markdown(mkin.read(), extras=DEFAULT_EXTRAS)

    output += """</body>
    </html>
    """

    htmlfile = removeExtension(file) + ".html"

    outfile = open(htmlfile, "w")
    outfile.write(output)
    outfile.close()
    
    print("-" * 60)
    print(f"{Fore.GREEN}[*] File converted with successfully.")
    print("-" * 60)
    
    print(f"[*] Input file: {Fore.BLUE + file}")
    
    if style and style != "no-style":
        print(f"[*] Style CSS file: {Fore.MAGENTA + style}")
        
    print(f"[*] Output file: {Fore.CYAN + htmlfile}")