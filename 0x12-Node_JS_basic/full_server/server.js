import router from './routes';

const express = require('express');

const port = 1245;
const app = express();
export default app;

app.use('/', router);

app.listen(port);
