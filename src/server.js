/* eslint no-console: "off", global-require: "off" */
import path from 'path';
import express from 'express';

const app = express();

let port = process.env.PORT || 3000;
let homepage = path.join(__dirname, 'client/index.html');

const config = require('./webpack.config.dev');
const compiler = require('webpack')(config);
app.use(require('webpack-dev-middleware')(compiler, {
  noInfo: true,
  publicPath: config.output.publicPath
}));
app.use(require('webpack-hot-middleware')(compiler, {
  log: console.log,
  path: '/__webpack_hmr',
  heartbeat: 10 * 1000
}));


app.get('*', (req, res) => {
  res.sendFile(homepage);
});

app.listen(port, () => {
  console.log('Magic happening at: ', port);
});
