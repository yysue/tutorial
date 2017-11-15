package com.demo.log0;

import java.util.logging.Logger;

//  jdk×Ô´øµÄlogging
public class JdkLoggingTest {
	private static final Logger logger = Logger.getLogger(JdkLoggingTest.class.getName());

	public static void main(String[] args) {
		logger.info("jdk logging info: a msg");
	}
}
