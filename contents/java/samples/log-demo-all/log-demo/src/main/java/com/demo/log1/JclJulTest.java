package com.demo.log1;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class JclJulTest {
	private static Log logger = LogFactory.getLog(JclJulTest.class);

	public static void main(String[] args){
		if(logger.isTraceEnabled()){
			logger.trace("commons-logging-jcl trace message");
		}
		if(logger.isDebugEnabled()){
			logger.debug("commons-logging-jcl debug message");
		}
		if(logger.isInfoEnabled()){
			logger.info("commons-logging-jcl info message");
		}
	}
}
