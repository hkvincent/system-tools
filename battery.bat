@echo off
powercfg /batteryreport /output C:\Users\Vincent\battery_report.html
SET DD=%date:~0,2%
SET MM=%date:~3,2%
SET YY=%date:~8,2%
SET YYYY=%date:~6,4%
SET DT=%YYYY%_%MM%_%DD%
SET filename=battery_report_%date%.html
echo "%DD%"
echo "%MM%"
echo "%YYYY%"
echo "%DT%"
echo "%date%"
echo "%filename%"

move /y "C:\Users\Vincent\battery_report.html" 	"D:\document\batteryreport\%filename%"
