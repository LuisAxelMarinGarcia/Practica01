const axios = require('axios');

const ORDER_SERVICE_URL = process.env.ORDER_SERVICE_URL;

const createOrder = async (orderData) => {
  try {
    const response = await axios.post(`${ORDER_SERVICE_URL}/orders`, orderData);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

const listOrders = async () => {
  try {
    const response = await axios.get(`${ORDER_SERVICE_URL}/orders`);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

const updateOrderStatus = async (orderId, statusData) => {
  try {
    const response = await axios.patch(`${ORDER_SERVICE_URL}/orders/${orderId}/status`, statusData);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

module.exports = {
  createOrder,
  listOrders,
  updateOrderStatus,
};
