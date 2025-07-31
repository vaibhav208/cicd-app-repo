# End-to-End CI/CD Pipeline for a Python Application on AWS EKS

This repository contains the source code and configuration files for a complete, end-to-end CI/CD pipeline project. The goal of this project is to automate the entire lifecycle of a Python (FastAPI) web application, from a `git push` to a live deployment on a managed Kubernetes cluster in AWS.

## 🚀 Tech Stack

This project integrates a modern set of DevOps and cloud-native technologies:

* **Application:** Python (FastAPI) & Uvicorn
* **Containerization:** Docker
* **Source Control:** Git & GitHub
* **CI/CD Automation:** AWS CodePipeline & AWS CodeBuild
* **Container Registry:** Amazon ECR (Elastic Container Registry)
* **Cloud Provider:** Amazon Web Services (AWS)
* **Orchestration:** Kubernetes on Amazon EKS (Elastic Kubernetes Service)

## 🏛️ Architecture Overview

The pipeline follows a standard GitOps-style workflow:

1.  **Commit:** A developer pushes a code change to the `main` branch on GitHub.
2.  **CI Trigger:** AWS CodePipeline automatically detects the push and triggers the pipeline.
3.  **Build & Test:** AWS CodeBuild spins up a build environment, installs dependencies, and (in a production scenario) would run unit tests.
4.  **Containerize:** CodeBuild uses the `Dockerfile` to build a new container image of the application.
5.  **Push to Registry:** The newly built image is tagged and pushed to a private repository in Amazon ECR.
6.  **Deploy:** The final stage involves deploying the new container image to the Amazon EKS cluster. In this project, this was a manual `kubectl` step, but it can be fully automated.
7.  **Expose:** An AWS Load Balancer, provisioned by a Kubernetes Service manifest, exposes the running application to the internet.
```
[Developer] -> git push -> [GitHub] -> (Webhook) -> [AWS CodePipeline]
                                                           |
                                                           V
                                                 [AWS CodeBuild] -> (Builds & Pushes Image) -> [Amazon ECR]
                                                           |
                                                           V
                                                 [Manual kubectl Apply] -> [Amazon EKS Cluster]
                                                                                |
                                                                                V
                                                                     [AWS Load Balancer] -> [End User]
```

## ✨ Key Features

* **Full Automation:** The Continuous Integration (CI) part of the pipeline is fully automated. Every push to the `main` branch results in a new, versioned container image being stored in ECR.
* **Infrastructure as Code (IaC) Principles:** The application's runtime environment (`Dockerfile`), build process (`buildspec.yml`), and Kubernetes deployment (`deployment.yaml`, `service.yaml`) are all defined as code.
* **Scalable Deployment:** The application is deployed on Kubernetes, allowing for easy scaling and high availability.
* **Cloud-Native Integration:** Leverages managed AWS services (EKS, ECR, CodePipeline) to reduce operational overhead.

## 🛠️ Project Setup & Deployment

This repository contains all the necessary configuration files to replicate this project. The high-level steps are:

1.  **Prerequisites:** An AWS account, a GitHub account, and local installations of `git`, `docker`, the `aws-cli`, and `kubectl`.
2.  **AWS Setup:**
    * Create a private repository in **Amazon ECR**.
    * Create an **Amazon EKS cluster**.
    * Tag the public subnets in your VPC with `kubernetes.io/role/elb` = `1`.
3.  **CI/CD Pipeline Setup:**
    * Create a **CodeBuild** project linked to this GitHub repository, ensuring the "Privileged" flag is enabled and environment variables are set.
    * Create a **CodePipeline** that uses the GitHub repo as a source and the CodeBuild project as the build stage.
    * Grant the CodeBuild IAM role permissions to access ECR.
4.  **Kubernetes Deployment:**
    * Configure `kubectl` access to your EKS cluster, including setting up the `aws-auth` ConfigMap to grant your IAM user permissions.
    * Apply the Kubernetes manifests:
        ```bash
        # Update the image URI in deployment.yaml first!
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        ```

## Acknowledgements

A special thank you to my mentor, **Vimal Daga sir**, for his invaluable guidance and for fostering a deep understanding of real-world cloud and DevOps practices.
"# cicd-app-repo" 
"# cicd-app-repo" 
