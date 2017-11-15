package com.demo.log_jcl_jul;

import java.util.Iterator;
import java.util.ServiceLoader;

import org.apache.commons.logging.LogFactory;

public class SpiTest {
	public static void main(String[] args) {
		ServiceLoader<LogFactory> serviceLoader = ServiceLoader.load(LogFactory.class);
		Iterator<LogFactory> ite = serviceLoader.iterator();
		while (ite.hasNext()) {
			System.out.println(ite.next());
		}
	}
}
