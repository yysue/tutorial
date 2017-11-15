package com.demo.log_jcl_log4j2;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

public class Log4j2JclTest {
	private static Log logger=LogFactory.getLog(Log4j2JclTest.class);

	public static void main(String[] args){
		if(logger.isTraceEnabled()){
			logger.trace("commons-logging-log4j trace message");
		}
		if(logger.isDebugEnabled()){
			logger.debug("commons-logging-log4j debug message");
		}
		if(logger.isInfoEnabled()){
			logger.info("commons-logging-log4j info message");
		}
	}
}
