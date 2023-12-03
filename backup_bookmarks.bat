@echo off
setlocal enabledelayedexpansion


REM Define the source path (where Chrome stores bookmarks)
set SOURCE=%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Bookmarks


REM Get the current date and time and format it as YYYY-MM-DD_HH-MM-SS
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "datetime=%%a"
set "formattedDate=!datetime:~0,4!-!datetime:~4,2!-!datetime:~6,2!_!datetime:~8,2!-!datetime:~10,2!-!datetime:~12,2!"


REM Define the destination path (where you want to copy the bookmarks) with datetime suffix
set DEST=D:\application\Dropbox\Tools\bookmarks\BookmarksBackup_!formattedDate!.json

echo Source: "%SOURCE%"
echo Destination: "%DEST%"

REM Check if Chrome is running
REM tasklist | find /i "chrome.exe" > nul
REM if %ERRORLEVEL%==0 (
REM    echo Please close Google Chrome before proceeding.
REM    exit /b
REM )


REM Copy the bookmarks file to the desired location
copy "%SOURCE%" "%DEST%"


REM Check if the copy operation was successful
if %ERRORLEVEL%==0 (
    echo Bookmarks successfully copied to %DEST%
) else (
    echo An error occurred while copying bookmarks.
)


endlocal
