# dokku-simple-python-vue-spa

## Usage

xxx

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
mkdir backend && cd backend
python3 -mvenv pyenv
. pyenv/bin/activate
```

### Credits

Inspiration: https://github.com/oleg-agapov/flask-vue-spa
