# WordWeave

## Introduction
WordWeave is a Flask application that uses Together AI's inference capabilities to create blogposts. This project shows the integration of Together AI within a Flask web application, which is then dockerized for consistent deployment across environments.

## Features
- Generates blog posts based on user-provided topics.
- Uses Together AI for content. generation using open-source models
- Dockerized application for easy setup and deployment.


## Prerequisites
- Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/)
- An API key from Together AI. [Register for an API key](https://together.ai/)

## Installation and Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/berlanga87/ai-blog-post-generator.git
   cd ai-blog-post-generator


2. **Export your Together AI API key as an environment variable:**
   ```sh
   export TOGETHER_API_KEY='api_key'

3. **Build the Docker Image**

   ```sh
   docker build -t ai-blog-post-generator .

4. **Run the container**
    ```s
    docker run -p 5000:5000 -e TOGETHER_API_KEY=$TOGETHER_API_KEY ai-blog-post-generator


## Usage
After starting the application, go to http://localhost:5000 on your web browser. Choose or type a topic, hit Generate and the application will create a blog post on it.