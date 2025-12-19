Retailio Sales & Product Data Pipeline
Overview

This repository contains an automated Retailio sales and product data pipeline designed using a modern cloud-based ELT architecture.
The pipeline supports reliable data generation, ingestion, transformation, and analytics delivery for business reporting in Power BI.

The project demonstrates industry best practices in automation, data warehousing, cloud storage, security, and business intelligence integration.

Architecture Overview

Architecture Pattern: ELT (Extract → Load → Transform)

The pipeline separates raw data ingestion from transformation logic, ensuring scalability, auditability, and analytics readiness.

High-level flow:

Data Generation → Cloud Storage → Ingestion → Transformation → Analytics

End-to-End Pipeline Flow
flowchart LR
    A[Windows Task Scheduler<br/>Weekly] --> B[Data Generation Script]
    B --> C[Amazon S3<br/>Raw Data Storage]

    C --> D[Airbyte Cloud<br/>Daily Sync]
    D --> E[Snowflake RAW Schema]

    E --> F[Snowflake STAGE Schema<br/>Cleansing & Standardization]
    F --> G[Snowflake ANALYTICS Schema<br/>Business Views]

    G --> H[Power BI<br/>Dashboards & Reports]

Pipeline Workflow
1. Data Generation (Weekly)

A scheduled job runs via Windows Task Scheduler

Sales and product datasets are generated automatically

Output files are uploaded to Amazon S3

2. Amazon S3 – Raw / Landing Zone

Stores raw datasets in their original format

Acts as the source of truth for ingestion

No transformations applied at this stage

3. Airbyte Cloud – Ingestion Layer

Synchronizes new and updated files from S3 to Snowflake

Runs on a daily schedule

Loads data into Snowflake RAW schema with minimal processing

4. Snowflake – Transformation Layer

SQL-based transformations are applied inside Snowflake:

RAW Schema

Immutable, historical record of ingested data

Supports auditing and traceability

STAGE Schema

Data cleansing and standardization

Data type casting and business rule enforcement

ANALYTICS Schema

Final reporting views

Optimized for BI consumption

5. Power BI – Reporting Layer

Connects directly to Snowflake analytics views

Provides interactive dashboards and insights

Supports business decision-making

Technology Stack
Layer	Technology
Scheduling	Windows Task Scheduler
Storage	Amazon S3
Ingestion	Airbyte Cloud
Data Warehouse	Snowflake
Transformation	SQL (Snowflake)
Analytics	Power BI
Scheduling Strategy
Component	Frequency
Data Generation	Weekly
S3 → Snowflake Sync	Daily
Snowflake Transformations	Scheduled / Event-based
Repository Structure
retailio-data-pipeline/
├── scheduler/          # Scheduled data generation scripts
├── sql/                # Snowflake SQL (RAW, STAGE, ANALYTICS)
├── diagrams/           # Architecture and flow diagrams
├── docs/               # Documentation and data dictionary
├── .env.example        # Environment variable template
├── .gitignore          # Security and cleanup rules
└── README.md

Configuration & Security

Secrets and credentials are managed via environment variables

Sensitive assets are excluded using .gitignore

Raw data files and Snowflake SQL execution details are not committed

Repository follows least-privilege and separation-of-concerns principles

Usage Guide

Configure the weekly job in Windows Task Scheduler

Verify data files are uploaded to the designated Amazon S3 bucket

Configure Airbyte Cloud to sync S3 data to Snowflake daily

Deploy Snowflake SQL transformations

Connect Power BI to Snowflake analytics views

Purpose

This project demonstrates:

End-to-end data pipeline design

Cloud-native ELT architecture

Workflow automation and scheduling

Data warehouse modeling best practices

Secure analytics integration with BI tools

