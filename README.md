# dokku-simple-python-vue-spa

Demonstrates a simple python api with a postgres database and a vuejs SPA, deployed on dokku.

## Usage

### Development

Launch backend:

```
python3 -mvenv pyenv
. pyenv/bin/activate
cd backend
python cli.py init-db
FLASK_DEBUG=1 FLASK_APP=app flask run
```

Launch frontend:

```
cd frontend
yarn serve
```

The frontend is available on http://localhost:8080 and uses the API available at http://localhost:5000.

### Production (dokku)

This project uses two buildpacks, `node` and `python`, to build and install both frontend and backend.

On the dokku server, prepare the postgres database and create the app:

```
dokku apps:create simple-spa
dokku postgres:create simple-spa
dokku postgres:link simple-spa simple-spa
```

On local copy:

```
git remote add dokku dokku@{host}:simple-spa
git push dokku master
```

The deployment process will run `init-db` thanks to the Procfile.

:rocket: http://simple-spa.{host}/api

## Initial setup

How this repo has been built (result is commited).

### frontend

```
yarn global add @vue/cli @vue/cli-service-global
vue create frontend
# vue features: vuex, router w/ history mode
```

```
rm -rf frontend/.git
git init
```

In `frontend/vue.config.js`:

```json
module.exports = {
  outputDir: '../dist',
  assetsDir: 'static'
}
```

```
cd frontend && yarn build
```

### backend

```
python3 -mvenv pyenv
. pyenv/bin/activate
mkdir backend && cd backend
# write code :-)
```

### Credits

Inspiration: https://github.com/oleg-agapov/flask-vue-spa
