# Create/remove/navigate to a bunch of different directories using 
# Windows shell scripting. This is task/step 1. 2025-06-09 EJS

# Create directory 3 directories:
New-Item -Path "Monty" -ItemType directory
Write-Output "The directory Monty has been created."

New-Item -Path "Python" -ItemType directory
Write-Output "The directory Python has been created."

New-Item -Path "Spam" -ItemType directory
Write-Output "The directory Spam has been created."

# Remove directories Monty and Python.
# EJS: I looked up the `rmdir` command on stackoverflow.
rmdir "Monty"
rmdir "Python"

# Navigate to the directory Spam
cd ".\Spam"