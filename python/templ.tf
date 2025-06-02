anikumar43@WKMZT67B4DC2 ~ % cat render.tpl 
apiVersion: v1
kind: ConfigMap
metadata:
  name: ${name}
data:
  key: ${value}

anikumar43@WKMZT67B4DC2 ~ % cat main.tf 
variable "name" {}
variable "value" {}

resource "null_resource" "write_configmap" {
  provisioner "local-exec" {
    command = <<EOT
      echo '${templatefile("${path.module}/render.tpl", {
        name  = var.name,
        value = var.value
      })}' > configmap.yaml
    EOT
  }
}
