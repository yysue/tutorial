package com.demo.log_jcl_jul;

import java.util.logging.LogManager;
import java.util.logging.Logger;

//  jdk自带的logging
public class JdkLoggingTest {
	private static final Logger logger = Logger.getLogger(JdkLoggingTest.class.getName());

	LogManager lm;
	
	public static void main(String[] args) {
		logger.info("jdk logging info: a msg");
	}
}
