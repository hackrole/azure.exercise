# run app using pure python in localhost

```bash
# enable virtaulenv
source venv/bin/activate

# run app
gunicorn web:app

# open http://127.0.0.1:8000/ in your browser
```

# build docker image

```bash
# enable virtaulenv
source venv/bin/activate

# build
invoke build
```

# run app using docker and run ab test

```bash
# enable virtaulenv
source venv/bin/activate

# run using docker
invoke run

# run ab test
invoke ab
```
