import runtimeEnv from '@mars/heroku-js-runtime-env';

const env = runtimeEnv();
const config = {
  apiBasePath: 'http://127.0.0.1:8000',
};

export default config;
