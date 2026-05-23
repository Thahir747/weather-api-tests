@echo off
echo Initializing Git repository...
git init

echo Connecting to GitHub...
git remote add origin https://github.com/Thahir747/weather-api-tests.git

echo Adding all files...
git add .

echo Committing files...
git commit -m "Add Weather API test automation framework"

echo Pushing to GitHub...
git push -u origin master

echo Done! Check your GitHub repository!
pause