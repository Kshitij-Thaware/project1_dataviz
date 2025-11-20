# project1_dataviz
Streamlit web app for data visualization

# Steps

# 1 - Create a repository on github.com and create a branch and then clone the branch on local computer

# 1a - sign up and login to github.com
# 1b - click on "new repository" and we create a new repo with name as project1_dataviz, gitignore, readme and license file
# 1c - create a branch with "pranav"
# 1d - copy the branch url for cloning in vs code
# 1e - vs code click "file", "new window", then "clone git repo", then select folder destination and clone
# 1f - open the folder

# 2 - Create virtual environment

# 2a - go to "terminal" , "new terminal", type in terminal  ->> python -m venv myenv
# 2b - if python not found error is coming then add system environment variables
# 2c - if python not found error is coming then Ctrl+shift+P then select Python create environment, then venv, then enter
# 2d - install python from python.org
# 2e - after venv is created then type in terminal myenv/Scripts/activate
       (or .venv/Scripts/activate)
# 2f - ONLY IF problems in activating virtual environment then do open "powershell" in admin mode and type Set-ExecutionPolicy RemoteSigned

# 3 - Go to branch
# 3a - write in terminal ->> git checkout pranav
  (because my branch name is pranav)
# 3b - add to gitignore file the foldername of virtual evironment
       (myenv/)

# 4 - install python libraries/packages
# 4a - type in terminal -> pip install streamlit, pipreqs
# or type in terminal below two lines (one after another) 
#       pip install streamlit
#       pip install pipreqs

# 5 - aim: to create a website on which user will upload a file dataset.csv
# further user will select a column
# if column type is numeric then display the histogram
# if column type is nominal then display the bar chart

# 5a - create a file named "main.py" and a folder "services"

# in main.py write the code
# execute main.py by typing in terminal -> streamlit run main.py
# after few seconds you will see the python website in the web browser window (chrome/edge)
# to stop streamlit website press Ctrl+C/Ctrl+Z/Ctrl+V

# 6 - add-commit-push to github

# 6aa - 

Set your username: write in terminal
replace your username

git config --global user.name "username"

Set your email address: write in terminal
replace your email

git config --global user.email "MY_NAME@example.com"


# 6a - click on "source control" then "click on + in changes" then write commit message then click commit then click sync changes and then click ok

# 6b - check on github.com in your branch if the code files are updated

#7 - create requirements.txt

# 7a - type in terminal -> pipreqs --ignore myenv/
  (replace your virtualenvironment foldername)

# 7b - add, commit, push and pull request with main

#Note - to install packages with correct version you can type in terminal 
pip install -r requirements.txt