#!/usr/bin/env python3
import sys
import subprocess

REQUIRED = [
    "flask",
    "requests",
    "beautifulsoup4",
    "rich"
]

def ensure_packages():
    import importlib
    for pkg in REQUIRED:
        try:
            if pkg == "beautifulsoup4":
                importlib.import_module("bs4")
            else:
                importlib.import_module(pkg)
        except ImportError:
            print(f"[INFO] Installing missing dependency: {pkg}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def main():
    try:
        ensure_packages()
        import zerotrace
        # If your main script is in zerotrace.py, and you want to call its main():
        if hasattr(zerotrace, "main"):
            zerotrace.main()
        else:
            print("[INFO] zerotrace module imported. Add 'def main():' in zerotrace.py to run automatically.")
    except ModuleNotFoundError as e:
        print(f"[ERROR] zerotrace.py not found or not importable. Make sure zerotrace.py is in this folder. Details: {e}")
    except Exception as ex:
        print(f"[ERROR] An error occurred: {ex}")

if __name__ == "__main__":
    print("""
███████╗███████╗██████╗  ██████╗ ████████╗██████╗  █████╗  ██████╗███████╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
  ███╔╝ █████╗  ██████╔╝██║   ██║   ██║   ██████╔╝███████║██║     █████╗  
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
███████╗███████╗██║  ██║╚██████╔╝   ██║   ██║  ██║██║  ██║╚██████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝

                 ZeroTrace - Beautiful Criminal Tracker
                 Author: mrxvaau (github.com/mrxvaau)
    """)
    main()
