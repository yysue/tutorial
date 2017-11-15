package com.demo.log_jcl_logback;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class LogbackTest {
	private static Log logger = LogFactory.getLog(LogbackTest.class);

	public static void main(String[] args) {
		if (logger.isTraceEnabled()) {
			logger.trace("commons-logging-jcl trace message");
		}
		if (logger.isDebugEnabled()) {
			logger.debug("commons-logging-jcl debug message");
		}
		if (logger.isInfoEnabled()) {
			logger.info("commons-logging-jcl info message");
		}
	}
}
