resource "kind_cluster" "mlops" {
  name            = "mlops-cluster"
  wait_for_ready  = true
}

output "cluster_name" {
  value = kind_cluster.mlops.name
}

output "kubeconfig" {
  value     = kind_cluster.mlops.kubeconfig
  sensitive = true
}
