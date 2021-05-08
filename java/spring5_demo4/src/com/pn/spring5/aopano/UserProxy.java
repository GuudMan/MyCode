package com.pn.spring5.aopano;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Component
@Aspect  //生成代理对象
public class UserProxy {

    @Pointcut(value = "execution(* com.pn.spring5.aopano.User.add(..))")
    public void pointCut(){

    }

    // 前置通知
    // before注解
    @Before(value = "pointCut()")
    public void before(){
        System.out.println("before.....");
    }


    // after注解
    @After(value = "execution(* com.pn.spring5.aopano.User.add(..))")
    public void after(){
        System.out.println("after.....");
    }

    // afterReturning注解
    @AfterReturning(value = "execution(* com.pn.spring5.aopano.User.add(..))")
    public void afterReturning(){
        System.out.println("afterReturning.....");
    }

    // after注解
    @AfterThrowing(value = "execution(* com.pn.spring5.aopano.User.add(..))")
    public void afterThrowing(){
        System.out.println("AfterThrowing.....");
    }

    // after注解
    @Around(value = "execution(* com.pn.spring5.aopano.User.add(..))")
    public void around(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        System.out.println("around之前.....");
        proceedingJoinPoint.proceed();
        System.out.println("around之后.....");
    }



}
