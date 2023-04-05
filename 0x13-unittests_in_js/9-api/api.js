const express = require('express');

const port = 7865;
const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
  const { id } = req.params;
  if(!(isNaN(Number(id)))) {
    res.send('Payment methods for cart ' + id);
  } else {
    res.status(404);
    res.end();
  }
});

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
