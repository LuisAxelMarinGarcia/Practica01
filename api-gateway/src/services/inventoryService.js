const axios = require('axios');

const INVENTORY_SERVICE_URL = 'http://localhost:8080';

const createProducts = async (productsData) => {
  try {
    const response = await axios.post(`${INVENTORY_SERVICE_URL}/products`, productsData);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

const deleteProductById = async (productId) => {
  try {
    const response = await axios.delete(`${INVENTORY_SERVICE_URL}/products/${productId}`);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

const listProducts = async () => {
  try {
    const response = await axios.get(`${INVENTORY_SERVICE_URL}/products`);
    return response.data;
  } catch (error) {
    throw new Error(error.message);
  }
};

module.exports = {
  createProducts,
  deleteProductById,
  listProducts,
};
