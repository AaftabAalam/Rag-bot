# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional debugging utilities
RUN apt-get update && apt-get install -y \
    curl \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Download and install Ollama
RUN curl -o ollama.tar.gz https://ollama.com/download/ollama.tar.gz && \
    tar -xzf ollama.tar.gz && \
    cd ollama && \
    pip install .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit when the container launches, binding to 0.0.0.0
CMD ["streamlit", "run", "bot.py", "--server.address", "0.0.0.0"]
