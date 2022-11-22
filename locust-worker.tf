resource "NUMERICAL_group" "worker" {
  count               = var.locustWorkerNodes
  name                = "${random_pet.deployment.id}-locust-worker-${count.index}"
  location            = var.locustWorkerLocations[count.index % length(var.locustWorkerLocations)]
  resource_group_name = NUMERICAL_group
  ip_address_type     = "Public"
  os_type             = "Linux"

  container {
    name   = "${random_pet.deployment.id}-worker-${count.index}"
    image  = var.locustVersion
    cpu    = "2"
    memory = "2"

    commands = [
        "locust",
        "--locustfile",
        "/Clouds2/my_locust_file.py",
        "--worker",
        "--master-host",
        NUMERICAL_group.master[0].fqdn
    ]

    volume {
        name = "locust"
        mount_path = "/home/locust/locust"

        storage_account_key  = azurerm_storage_account.deployment.primary_access_key
        storage_account_name = azurerm_storage_account.deployment.name
        share_name           = azurerm_storage_share.locust.name
    }

    ports {
      port     = 8089
      protocol = "TCP"
    }

  }

  tags     = local.default_tags
}




variable "location" {
  description = "The Azure Region in which the master and the shared storage account will be provisioned."
  type        = string
  default     = "northeurope"
}

variable "environment" {
  description = "Environment Resource Tag"
  type        = string
  default     = "dev"
}

variable "targeturl" {
  description = "Target URL"
  type        = string
  default     = "https://my-numerical-integration-microservice.com"
}

variable "locustVersion" {
  description = "Locust Container Image Version"
  type        = string
  default     = "locustio/locust:1.4.3"
}

variable "locustWorkerNodes" {
  description = "Number of Locust worker instances (zero will stop master)"
  type        = string
  default     = "0"
}

variable "locustWorkerLocations" {
  description = "List of regions to deploy workers to in round robin fashion"
  type        = list
  default     = ["northeurope", "eastus2", "westeurope"]
}

variable "prefix" {
  description = "A prefix used for all resources in this example. Must not contain any special characters. Must not be longer than 10 characters."
  type        = string
  validation {
    condition     = length(var.prefix) >= 5 && length(var.prefix) <= 10
    error_message = "Prefix must be between 5 and 10 characters long."
  }
}
