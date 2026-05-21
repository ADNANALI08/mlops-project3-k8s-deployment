terraform {
  required_providers {
    minikube = {
      source  = "scott-the-programmer/minikube"
      version = "~> 0.4.2"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.30"
    }
  }
  required_version = ">= 1.3.0"
}

provider "minikube" {
  kubernetes_version = "v1.30.0"
}

provider "kubernetes" {
  host                   = minikube_cluster.mlops.host
  client_certificate     = minikube_cluster.mlops.client_certificate
  client_key             = minikube_cluster.mlops.client_key
  cluster_ca_certificate = minikube_cluster.mlops.cluster_ca_certificate
}
