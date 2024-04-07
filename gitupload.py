import subprocess
import os

def git_upload(commit_message):
    try:
        # Add all files in the current directory to the staging area
        subprocess.run(["git", "add", "."])

        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message])

        # Push the changes to the remote repository
        subprocess.run(["git", "push"])

        print("Files uploaded to GitHub successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for commit message
    commit_message = input("Enter the commit message: ")

    # Call function to upload files to GitHub
    git_upload(commit_message)
