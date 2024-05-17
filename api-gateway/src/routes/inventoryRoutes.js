const express = require('express');
const router = express.Router();
const inventoryController = require('../controllers/inventoryController');

router.post('/', inventoryController.createProducts);
router.delete('/:id', inventoryController.deleteProductById);
router.get('/', inventoryController.listProducts);

module.exports = router;
