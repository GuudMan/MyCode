package com.pn.spring5;

public class Order {
        private String oname;
        private String address;

        // 有参构造
        public Order(String oname, String address) {
            this.oname = oname;
            this.address = address;
        }

        public void testContruct(){
            System.out.println(oname + ":: " + address);
        }
}
