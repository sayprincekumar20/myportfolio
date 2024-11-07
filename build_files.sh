 echo "BUILD START"
 Python3.12.0 -m pip install -r requirements.txt
 Python3.12.0  manage.py collectstatic --noinput --clear
 echo "BUILD END"