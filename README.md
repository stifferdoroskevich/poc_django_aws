# define the app port in the .env file. PORT parameter

#####  Without Docker
1. $ `python3 -m venv .venv`
2. $ `source .venv/bin/activate`
3. $ `pip3 install -r requirements.txt`
4. complete .env file with data connection
5. $ `export $(cat .env | grep -v '#')`
6. $ `cd core`
7. $ `gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker`
8. Open browser with the port defined in .env PORT

##### Using Docker
