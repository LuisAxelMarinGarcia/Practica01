require('dotenv').config();  

const express = require('express');
const app = express();

app.use(express.json());

const orderRoutes = require('./routes/orderRoutes');
const inventoryRoutes = require('./routes/inventoryRoutes');

app.use('/orders', orderRoutes);
app.use('/inventory', inventoryRoutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`API Gateway running on port ${PORT}`);
});
