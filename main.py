"""
This module contains the main function that is called when the program is run.
"""

import os
import subprocess
import sys

if "datasets" in os.getcwd() or "deepnote" in os.getcwd():

    WORKING_DIRECTORY = "/work"

elif "/kaggle/input/" in os.getcwd():
    WORKING_DIRECTORY = "/kaggle/working"

elif "/gdrive" in os.getcwd():
    WORKING_DIRECTORY = "/content"
else:
    WORKING_DIRECTORY = os.getcwd()


os.chdir(WORKING_DIRECTORY)

# install gitpython
try:
    import git

    print("gitpython already installed")
except ImportError:
    print("gitpython not installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gitpython"])
    import git

except Exception as error:  # pylint: disable=broad-except
    print(error)
    print("Error")


REPO_NAME = "lyrics-meaning-using-chatgpt"


# check if the repo is already cloned
if not os.path.isdir(REPO_NAME):
    # clone the repo
    GIT_URL = f"https://chirag127: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@github.com/chirag127/{REPO_NAME}.git"  # pylint: disable=line-too-long
    git.Repo.clone_from(GIT_URL, REPO_NAME)

# change the working directory to the repo
print("Changing working directory to the repo")
os.chdir(REPO_NAME)
print("Changed working directory to", os.getcwd())


# pull the latest changes
print("Pulling the latest changes")
repo = git.Repo()
repo.remotes.origin.pull()
print("Pulled the latest changes")


# install the requirements
print("Installing the requirements")
try:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    )
except Exception as error:  # pylint: disable=broad-except
    print(error)
    print("Error")

WORKING_DIRECTORY = os.path.join(WORKING_DIRECTORY, REPO_NAME)
os.chdir(WORKING_DIRECTORY)

from csvprocess import main  # pylint: disable=wrong-import-position

if __name__ == "__main__":

    print("Starting")
    try:

        if "/work" in WORKING_DIRECTORY and "kaggle" not in WORKING_DIRECTORY:

            try:
                os.chdir(WORKING_DIRECTORY)
            except Exception as main_error:  # pylint: disable=broad-except
                print(main_error)
                print("Error")
            main()
            main()
            main()

        else:
            for _ in range(1, 100):
                try:
                    os.chdir(WORKING_DIRECTORY)
                except Exception as main_error:  # pylint: disable=broad-except
                    print(main_error)
                    print("Error")
                main()
    except Exception as main_error:  # pylint: disable=broad-except
        print(main_error)
        print("Error")
