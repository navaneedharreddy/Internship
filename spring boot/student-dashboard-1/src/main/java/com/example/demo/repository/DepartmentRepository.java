package com.example.demo.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.example.demo.model.Department;

public interface DepartmentRepository extends MongoRepository<Department, String> {

    List<Department> findByCollegeId(String collegeId);
}