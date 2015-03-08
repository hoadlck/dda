"""Django Desktop Application Setup Module

This module freezes executables needed by this module.

Invoke with the following command:
    >> python manage.py collectstatic --noinput --verbosity=0
    >> python setup.py build_exe
"""
from cx_Freeze import setup, Executable
import sys
import os
import shutil
import manage


print("Pre-build cleanup.")

try:
    #Clean up build directory.
    shutil.rmtree("build")
except:
    pass

try:
    #Clean up install directory.
    shutil.rmtree("install/bin/dda")
except:
    pass

setup(
        name = "dda",
        version = manage.__version__,
        description = manage.module_name,
        executables = [Executable("manage.py", copyDependentFiles=True)]
     )

print("Copy executable to install area...")

try:
    #Copy executable to install staging area.
    shutil.copytree("build/exe.win32-3.4", "install/bin/dda")

    #Remove executable from freeze area.
    shutil.rmtree("build")
except:
    print("Error during executable copy to install area.")

    #Exit with error.
    sys.exit(1)

print("Copy executable to installer staging area...")

try:
    os.makedirs("install/bin/dda/dda", exist_ok=True)
    shutil.copy("dda/settings.py", "install/bin/dda/dda")
except:
    print("Error during executable copy to binary repo area.")

    #Exit with error.
    sys.exit(1)

print("Done With It All...")
