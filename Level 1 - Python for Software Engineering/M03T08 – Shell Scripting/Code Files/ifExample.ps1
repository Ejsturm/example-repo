# Using the if-else construction, create a new directory. The if-else
# determines the name of the new directory. This covers tasks 2 and 3. 
# 2025-06-09 EJS

if (Test-Path -Path "new_folder"){
	New-Item -Path "if_folder" -ItemType Directory
}

if (Test-Path -Path "if_folder") {
	New-Item -Path "hyperionDev" -ItemType Directory
} 
else {
	New-Item -Path "new-projects" -ItemType Directory
}