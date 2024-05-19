package com.example.inventory.service;

import com.example.inventory.model.Product;
import com.example.inventory.repository.ProductRepository;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    public List<Product> createProducts(List<Product> products) {
        return productRepository.saveAll(products);
    }

    public void deleteProductById(Long id) {
        productRepository.deleteById(id);
    }

    public List<Product> listProducts() {
        return productRepository.findAll();
    }

    @RabbitListener(queues = "order_status")
    public void handleOrderStatusEvent(String message) {
        String[] parts = message.split(",");
        Long orderId = Long.parseLong(parts[0]);
        String status = parts[1];

        if ("Enviado".equals(status)) {
            List<Product> products = productRepository.findAll(); 
            for (Product product : products) {
                product.setStock(product.getStock() - 1);
                productRepository.save(product);
            }
        }
    }

    public void updateProductStatus(Long id, String status) {
        throw new UnsupportedOperationException("Unimplemented method 'updateProductStatus'");
    }
}
