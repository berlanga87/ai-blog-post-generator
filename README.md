# AI-Powered Blog Post Generator

## Introduction
The AI-Powered Blog Post Generator is a Flask application that utilizes Together AI's generative AI capabilities to create engaging and informative blog posts based on user input. This project demonstrates the integration of AI technology within a web application, showcasing how to dockerize a Flask app for consistent deployment across environments.

## Features
- Generate blog posts based on user-provided topics.
- Simple and intuitive web interface.
- Dockerized application for easy setup and deployment.
- Utilizes Together AI for advanced content generation.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)
- An API key from Together AI. [Register for an API key](https://together.ai/)

## Installation and Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/ai-blog-post-generator.git
   cd ai-blog-post-generator


2. **Export your Together AI API key as an environment variable:***
   ```export TOGETHER_API_KEY='api_key'

3. **Build the Docker Image**

   ```docker build -t ai-article-generator .

4. **Run the container
docker run -p 5000:5000 -e TOGETHER_API_KEY=$TOGETHER_API_KEY ai-article-generator

