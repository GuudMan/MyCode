package com.pn.spring5.factoryBean;

import org.springframework.beans.factory.FactoryBean;

public class MyBean implements FactoryBean {

    // 定义返回的bean
    @Override
    public Object getObject() throws Exception {
        return null;
    }

    @Override
    public Class<?> getObjectType() {
        return null;
    }

    @Override
    public boolean isSingleton() {
        return false;
    }
}
