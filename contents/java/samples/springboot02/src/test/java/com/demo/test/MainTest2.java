package com.demo.test;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.sql.DataSource;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.demo.config.SpringConfig2;

// 读取外部的资源配置文件
public class MainTest2 {
	
	public static void main(String[] args) {
		// 通过Java配置来实例化Spring容器
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig2.class);

		// 在Spring容器中获取Bean对象
		// UserService userService = context.getBean(UserService.class);
		DataSource datasource = context.getBean(DataSource.class);

		// 调用对象中的方法
		try {
			Connection conn = datasource.getConnection();
			Statement stmt = conn.createStatement();
			stmt.executeQuery("select now() now from dual;");
			ResultSet rs = stmt.getResultSet();
			while (rs.next()) {
				String now = rs.getString("now");
				System.out.println(now);
			}
			rs.close();
			stmt.close();
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}

		// 销毁该容器
		context.destroy();
	}
}
