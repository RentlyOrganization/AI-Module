package com.example.AI;

import io.github.cdimascio.dotenv.Dotenv;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AiApplication {

	public static void main(String[] args) {
		Dotenv dotenv = Dotenv.load();
		System.setProperty("GROQ_API_KEY", dotenv.get("GROQ_API_KEY"));
		SpringApplication.run(AiApplication.class, args);
	}

}
