package com.example.demo.controller;

import com.example.demo.model.College;
import com.example.demo.service.CollegeService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/colleges")
public class CollegeController {

    private final CollegeService collegeService;

    // Manual constructor instead of @RequiredArgsConstructor
    public CollegeController(CollegeService collegeService) {
        this.collegeService = collegeService;
    }

    @GetMapping
    public List<College> getAllColleges() {
        return collegeService.getAllColleges();
    }

    @PostMapping
    public College addCollege(@RequestBody College college) {
        return collegeService.addCollege(college);
    }

    @GetMapping("/{id}")
    public ResponseEntity<College> getById(@PathVariable String id) {
        return collegeService.getById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable String id) {
        collegeService.delete(id);
        return ResponseEntity.noContent().build();
    }
}