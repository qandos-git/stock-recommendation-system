FROM python:3.11.11-slim

# Set the working directory
WORKDIR /app

# Copy dependencies file first (for caching layers)
COPY requirements.txt .

# Install Python dependencies, including PyTorch
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy the FastAPI app files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
