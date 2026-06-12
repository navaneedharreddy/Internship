package com.example.demo.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.example.demo.model.Student;

public interface StudentRepository extends MongoRepository<Student, String> {

    List<Student> findByDepartmentId(String departmentId);

    List<Student> findByCollegeId(String collegeId);
}