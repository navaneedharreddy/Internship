package com.example.demo.service;

import com.example.demo.model.College;
import com.example.demo.repository.CollegeRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class CollegeService {

    private final CollegeRepository collegeRepository;

    public CollegeService(CollegeRepository collegeRepository) {
        this.collegeRepository = collegeRepository;
    }

    public List<College> getAllColleges() {
        return collegeRepository.findAll();
    }

    public College addCollege(College college) {
        return collegeRepository.save(college);
    }

    public Optional<College> getById(String id) {
        return collegeRepository.findById(id);
    }

    public void delete(String id) {
        collegeRepository.deleteById(id);
    }
}