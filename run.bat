@echo off
setlocal
cd /d "%~dp0" || exit /b 1

where.exe ruby.exe >nul 2>&1
if errorlevel 1 if exist "C:\Ruby40-x64\bin\ruby.exe" set "PATH=C:\Ruby40-x64\bin;%PATH%"
where.exe ruby.exe >nul 2>&1
if errorlevel 1 goto missing_ruby

ruby.exe -S bundle exec jekyll serve --host 127.0.0.1 --port 4000 --watch --force_polling
if not errorlevel 1 exit /b 0
echo.
echo Jekyll could not start. See the error above.
pause
exit /b 1

:missing_ruby
echo Ruby was not found. Install RubyInstaller with Devkit and reopen this window.
pause
exit /b 1
