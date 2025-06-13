# Dockerfile
FROM langflowai/langflow:latest

WORKDIR /app

# This line is crucial for including your custom component in the image
COPY my_custom_components/ /app/my_custom_components/

EXPOSE 7860

CMD ["langflow", "run", "--host", "0.0.0.0"]