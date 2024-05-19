package com.example.inventory.controller;

import com.example.inventory.model.Product;
import com.example.inventory.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/products")
public class ProductController {

    @Autowired
    private ProductService productService;

    @PostMapping
    public ResponseEntity<List<Product>> createProducts(@RequestBody List<Product> products) {
        return ResponseEntity.ok(productService.createProducts(products));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProductById(@PathVariable Long id) {
        productService.deleteProductById(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping
    public ResponseEntity<List<Product>> listProducts() {
        return ResponseEntity.ok(productService.listProducts());
    }

    @PatchMapping("/{id}/status")
    public ResponseEntity<Void> updateProductStatus(@PathVariable Long id, @RequestBody String status) {
        productService.updateProductStatus(id, status);
        return ResponseEntity.noContent().build();
    }
}
