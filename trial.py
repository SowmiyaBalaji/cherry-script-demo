#!/usr/bin/env python3

import subprocess
import sys


source_branch = "development"


commits = [
    "345bb4dad9af434f0d2fa5d19663c08d57d480b0"
    
    
]


target_branch = "master"


def cherry_pick_commits():
    for commit in commits:
        result = subprocess.run(["git", "cherry-pick", commit], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error occurred while cherry-picking commit {commit}:")
            print(result.stderr)
            sys.exit(1)


def push_changes():
    subprocess.run(["git", "push", "origin", target_branch], check=True)


def main():
 
    subprocess.run(["git", "checkout", target_branch], check=True)

   
    cherry_pick_commits()

   
    push_changes()

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: ./cherry-pick.py")
        print("This script automates the cherry-picking process.")
        sys.exit(1)
    
    main()
