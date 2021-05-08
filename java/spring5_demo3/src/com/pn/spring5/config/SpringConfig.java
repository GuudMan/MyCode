package com.pn.spring5.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration // 该类作为配置类，替代xml文件
@ComponentScan(basePackages = {"com.pn.spring5"})
public class SpringConfig {

}
