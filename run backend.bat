cd src
call env\Scripts\activate.bat
uvicorn main:app --host 0.0.0.0
pause