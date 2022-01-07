py -m pip install --upgrade pip
py -m pip install --user virtualenv
cd src 
py -m venv env

call .\env\Scripts\activate
pip install -r requirements.txt
pip install -e .