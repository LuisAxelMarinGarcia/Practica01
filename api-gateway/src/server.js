require('dotenv').config();
const express = require('express');
const morgan = require('morgan');
const app = require('./app');

const PORT = process.env.PORT || 3000;

app.use(morgan('dev'));

app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});
