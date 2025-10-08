from setuptools import setup, Extension
import sys
import os
import glob
import platform

def find_cpp():
    cpp_files = [f for f in glob.glob("*.cpp") if f != "main.cpp"]
    if not cpp_files:
        print("❌ No .cpp file found in this folder!")
        sys.exit(1)
    if len(cpp_files) > 1:
        print("❌ Multiple .cpp files found! Please keep only one for this build.")
        sys.exit(1)
    return cpp_files[0]

def get_ext_name(filename):
    return os.path.splitext(os.path.basename(filename))[0]

def get_ext_suffix():
    plat = sys.platform
    if plat.startswith("win"):
        return ".pyd"
    elif plat.startswith("linux") or plat.startswith("darwin"):
        return ".so"
    else:
        return ".so"

if __name__ == "__main__":
    cpp_file = find_cpp()
    module_name = get_ext_name(cpp_file)

    # Extra compile args if you want
    extra_args = []
    if not sys.platform.startswith("win"):
        extra_args.append("-std=c++17")

    ext = Extension(
        module_name,
        sources=[cpp_file],
        language="c++",
        extra_compile_args=extra_args
    )

    print(f"\n[+] Detected OS: {platform.system()} {platform.machine()}")
    print(f"[+] Building module from {cpp_file} as {module_name}{get_ext_suffix()} ...\n")

    setup(
        name=module_name,
        ext_modules=[ext],
        script_args=['build_ext', '--inplace'],
        zip_safe=False,
    )

    print(f"\n✅ Build finished! You can now run:  python run.py")
    print(f"[*] Your module is importable as:  import {module_name}\n")
