package com.demo.test;

import java.util.List;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import com.demo.config.SpringConfig;
import com.demo.entity.User;
import com.demo.service.UserService;

// 该示例演示了通过 Java 配置的方式进行配置 Spring，并且实现了 Spring IOC 功能。
public class MainTest {
	
	public static void main(String[] args) {
		// 通过Java配置来实例化Spring容器
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);

		// 在Spring容器中获取Bean对象
		UserService userService = context.getBean(UserService.class);

		// 调用对象中的方法
		List<User> list = userService.queryUserList();
		for (User user : list) {
			System.out.println(user.getUsername() + ", " + user.getPassword() + ", " + user.getPassword());
		}

		// 销毁该容器
		context.destroy();
	}
}
