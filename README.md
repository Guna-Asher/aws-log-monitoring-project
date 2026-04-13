# AWS Log Monitoring & Archival System

## Overview

This project implements an automated log monitoring pipeline using AWS EC2, IAM Roles, Docker, Python, cron scheduling, and Amazon S3.

The system scans application logs, extracts ERROR entries, and uploads them securely into an S3 bucket.

## Architecture

Application logs
→ Docker container
→ Python monitoring script
→ IAM Role authentication
→ Amazon S3 archival storage

## Technologies Used

Linux
AWS EC2
IAM Roles
Amazon S3
Docker
Python (boto3)
Cron automation

## Features

Automated log scanning
Error detection
Secure IAM role authentication
Containerized execution
Cloud archival storage
