# Case Study for SevenApps

## Overview

Case Study 7 is a chat with pdf application using Gemini API. This repository implements an API using FastAPI that allows users to interact with uploaded pdfs. 

## Table of Contents


- [Technologies Used]
- [Installation]


## Technologies Used

- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
- Gooogle Gemini API: Build with state-of-the-art generative AI models and tools to make AI helpful for everyone

## Installation

To get a local copy up and running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yagatso/casestudy7.git
   cd CaseStudy7

2. Install dependencies
    ```bash
    pip install -r requirements.txt

3. Set up your environment variables(Gemini API Key)
    ```bash
    API_KEY=your_api_key

4. Finally run the application
    ```bash
    uvicorn main:app --reload