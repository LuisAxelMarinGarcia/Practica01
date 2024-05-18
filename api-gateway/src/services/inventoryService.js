require('dotenv').config();
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: process.env.DB_PORT,
});

const createProducts = async (productsData) => {
  const connection = await pool.getConnection();
  try {
    const [results] = await connection.query('INSERT INTO products (name, price, stock) VALUES ?', [productsData.map(product => [product.name, product.price, product.stock])]);
    return results;
  } catch (error) {
    throw new Error(error.message);
  } finally {
    connection.release();
  }
};

const deleteProductById = async (productId) => {
  const connection = await pool.getConnection();
  try {
    const [results] = await connection.query('DELETE FROM products WHERE id = ?', [productId]);
    return results;
  } catch (error) {
    throw new Error(error.message);
  } finally {
    connection.release();
  }
};

const listProducts = async () => {
  const connection = await pool.getConnection();
  try {
    const [results] = await connection.query('SELECT * FROM products');
    return results;
  } catch (error) {
    throw new Error(error.message);
  } finally {
    connection.release();
  }
};

module.exports = {
  createProducts,
  deleteProductById,
  listProducts,
};
