# Scheduler Microservice

This microservice provides API endpoints for managing and scheduling jobs, using Flask, Celery, and SQLAlchemy.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run Redis server:
   ```bash
   redis-server
   ```

3. Run Celery worker:
   ```bash
   celery -A scheduler worker --beat --loglevel=info
   ```

4. Run Flask app:
   ```bash
   python app.py
   ```

## API Endpoints

- `GET /jobs`: List all jobs
- `GET /jobs/:id`: Retrieve a job by ID
- `POST /jobs`: Create a new job

## Scaling Strategy

To handle the projected load of ~10,000 users, ~1,000 services, and ~6,000 API requests per minute, the microservice needs to be scalable both horizontally and vertically.

### 1. **Horizontal Scaling**:
   - **Load Balancing**: Use a load balancer like NGINX or AWS ELB to distribute incoming requests across multiple instances of the microservice.
   - **Containerization**: Deploy the microservice using Docker containers and orchestrate them with Kubernetes. This allows easy scaling by adding more containers as demand increases.
   - **Distributed Task Queue**: Celery supports distributed task queues, so the tasks can be executed by multiple worker nodes.

### 2. **Vertical Scaling**:
   - **Optimize Resource Usage**: Tune the application to efficiently use CPU, memory, and network resources. Use tools like `gunicorn` with multiple worker processes for better CPU utilization.

### 3. **Database Scaling**:
   - **Read/Write Separation**: Implement master-slave replication for the database where write operations go to the master, and read operations can be handled by replicas.
   - **Sharding**: If the database grows large, sharding can be used to split data across multiple servers.

### 4. **Caching**:
   - Use Redis or Memcached to cache frequent read operations, reducing database load and improving response times.

### 5. **API Rate Limiting**:
   - Implement rate limiting to protect the API from being overwhelmed by excessive requests from any single user or service.

By implementing these strategies, the microservice can be scaled to handle the increased load while maintaining performance and availability.
