const express = require('express');
const app = express();

app.use(express.json());

const orderRoutes = require('./routes/orderRoutes');
const inventoryRoutes = require('./routes/inventoryRoutes');

app.use('/orders', orderRoutes);
app.use('/inventory', inventoryRoutes);

module.exports = app;
