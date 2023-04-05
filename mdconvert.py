import argparse, pyfiglet
import pyfiglet.fonts
from core.engine import *
from colorama import init, Fore

version = "1.0.0"
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="File markdown to convert", required=True)
parser.add_argument("-s", "--style", help="Style CSS of file HTML", required=False)

args = parser.parse_args()

if __name__ == "__main__":
    init(autoreset=True)
    
    print(
        Fore.CYAN + pyfiglet.figlet_format("mdconvert")
    )
    
    print(f"\t\tv.{Fore.GREEN + version}")
    convert(args.file, args.style)
    