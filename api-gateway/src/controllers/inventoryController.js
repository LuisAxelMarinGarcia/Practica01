const inventoryService = require('../services/inventoryService');

exports.createProducts = async (req, res) => {
  try {
    const products = await inventoryService.createProducts(req.body);
    res.status(201).json(products);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.deleteProductById = async (req, res) => {
  try {
    const result = await inventoryService.deleteProductById(req.params.id);
    res.status(200).json(result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.listProducts = async (req, res) => {
  try {
    const products = await inventoryService.listProducts();
    res.status(200).json(products);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
