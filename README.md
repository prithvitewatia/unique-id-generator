# Distributed Unique ID Generator Service

This project implements a **distributed unique ID generator** inspired by [Flickr's Ticket Servers](https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/). It uses FastAPI, PostgreSQL, and Docker to create a scalable and fault-tolerant ID generation system.

## Features

- Generates unique IDs using odd and even sequences distributed across two services.
- Fault tolerance: If one service fails, the other continues generating IDs.
- Load-balanced traffic between ID generation services using Nginx.
- Minimal latency and high throughput design.

## Technologies Used

- **FastAPI**: Lightweight framework for building the ID generation API.
- **PostgreSQL**: Reliable relational database for sequence management.
- **Docker**: Containerized deployment for scalability.
- **Nginx**: Load balancer to route requests between services.

## Architecture

1. **Odd ID Generator**:
   - Generates odd numbers using a PostgreSQL sequence.
   - Exposed via `/next_id` endpoint.

2. **Even ID Generator**:
   - Generates even numbers using a PostgreSQL sequence.
   - Exposed via `/next_id` endpoint.

3. **Load Balancer**:
   - Nginx routes requests between the odd and even ID generators.

4. **Database**:
   - Each generator uses its own PostgreSQL instance to manage sequences.
