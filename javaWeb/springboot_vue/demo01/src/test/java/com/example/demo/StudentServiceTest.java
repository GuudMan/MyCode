package com.example.demo;

import com.example.demo.entity.Student;
import com.example.demo.repository.StudentRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import java.util.List;
import java.util.Optional;

@SpringBootTest
public class StudentServiceTest {

    @Autowired
    private StudentRepository studentRepository;

    @Test
    public void testFindAll() {

        List<Student> student = studentRepository.findAll();
        System.out.println(student);
    }

    @Test
    public void testFinAllPage(){
        // 查找所有学生信息
        Pageable pageable = PageRequest.of(0, 3);
        Page<Student> student = studentRepository.findAll(pageable);
        System.out.println("---student----");
        System.out.println(student.toString());
        }


    @Test
    public void save(){
        // 查找所有学生信息
        Student student = new Student();
        student.setAge(12);
        student.setName("刘璋");
        student.setGender("男");
        studentRepository.save(student);
    }


    @Test
    public void findById(){
        // 查找所有学生信息
       Integer id = 2;
       Optional<Student> student = studentRepository.findById(id);
        System.out.println(student.get());
    }

}
