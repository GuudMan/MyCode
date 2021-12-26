package com.pn.pojo;

import lombok.Data;

import java.util.List;

@Data
public class Vo {

	private int code;
	private String msg;
	private int count;
	private List<Object> data;
}
