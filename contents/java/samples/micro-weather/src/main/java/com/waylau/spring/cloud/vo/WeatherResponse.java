package com.waylau.spring.cloud.vo;

import java.io.Serializable;

/**
 * 返回消息对象.
 * 
 * @since 1.0.0 2017年9月2日
 * @author <a href="https://waylau.com">Way Lau</a>
 */
public class WeatherResponse implements Serializable {

	private static final long serialVersionUID = 1L;

	private Weather data; // 消息数据
	private String status; // 消息状态 接口调用的返回状态，返回值“1000”,意味着数据是接口正常
	private String desc; // 消息描述 接口状态的描述，“OK”代表接口正常 不是“1000”的情况,说明，这个接口调用异常了。

	public Weather getData() {
		return data;
	}

	public void setData(Weather data) {
		this.data = data;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getDesc() {
		return desc;
	}

	public void setDesc(String desc) {
		this.desc = desc;
	}

}
