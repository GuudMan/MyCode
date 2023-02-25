package com.example.demo.controller;

import com.example.demo.entity.Student;
import com.example.demo.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/student")
public class StudentController {

    @Autowired
    private StudentRepository studentRepository;

    // 查找所有学生信息
    @GetMapping("/findAll/{page}/{size}")
    public Page<Student> findAllStudent(@PathVariable("page") Integer page, @PathVariable("size") Integer size){
        Pageable pageable = PageRequest.of(page-1, size);
        Page<Student> student = studentRepository.findAll(pageable);
        return student;
    }

@PostMapping("/save")
    public String save(@RequestBody Student student){
        Student student1 =studentRepository.save(student);
        if(student1 != null){
            return "success";
        }else {
            return "error";
        }
    }


    @PostMapping("/update")
    public String update(@RequestBody Student student){
        Student student1 =studentRepository.save(student);
        if(student1 != null){
            return "success";
        }else {
            return "error";
        }
    }


    @GetMapping("/findById/{id}")
    public Student findById(@PathVariable("id") Integer id){
        return studentRepository.findById(id).get();
    }

    @DeleteMapping("/deleteById/{id}")
    public void deleteById(@PathVariable("id") Integer id){
        studentRepository.deleteById(id);
    }



}
