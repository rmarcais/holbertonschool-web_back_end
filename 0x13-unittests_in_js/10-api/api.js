const express = require('express');
const bodyParser = require('body-parser');

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

app.get('/available_payments', (req, res) => {
  res.send({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/login', (req, res) => {
  const { userName } = req.body;
  if (userName) {
    res.send('Welcome ' + userName);
  } else {
    res.status(404);
    res.end();
  }
});

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
