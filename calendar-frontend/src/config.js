import runtimeEnv from '@mars/heroku-js-runtime-env';

const env = runtimeEnv();
console.log("env",process.env.REACT_APP_API_HOST);
console.log("env_bis",process.env.REACT_APP_API_PORT);
const config = {
  // apiBasePath: 'http://localhost:80' ,
  apiBasePath: `${process.env.REACT_APP_API_HOST}:${process.env.REACT_APP_API_PORT}` ,

};

export default config;
