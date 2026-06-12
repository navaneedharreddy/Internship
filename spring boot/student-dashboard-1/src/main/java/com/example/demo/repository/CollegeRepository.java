package com.example.demo.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.example.demo.model.College;

public interface CollegeRepository extends MongoRepository<College, String> {

}