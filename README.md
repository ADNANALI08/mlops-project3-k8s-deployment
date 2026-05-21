# MLOps Project 3 — K8s Cluster Deployment

**Name:** [ADNAN ALI]
**SAP ID:** [70148007]
**Section:** [1st]
**Semester:** 6th

## Stack
Terraform · Minikube · Kubeflow Pipelines · MLflow · Scikit-learn · Docker · kubectl · Nginx · WSL Ubuntu

## Project Phases
1. **Terraform IaC** — Minikube K8s cluster provisioned via terraform apply
2. **Kubeflow Pipelines** — ML workflow deployed on K8s
3. **ML Pipeline** — Iris classification (load → train → evaluate), Accuracy: 1.0
4. **MLflow Registry** — Model registered and aliased as Production
5. **K8s Deployment** — 3-replica ReplicaSet with Nginx Ingress load balancer
