variable "resource_group_location" {
  type        = string
  default     = "francecentral"
  description = "Location of the resource group."
}

variable "resource_group_name" {
  type        = string
  description = "The resource group name."
}

variable "data_lake_name" {
  type        = string
  description = "The data lake resource name."
}

variable "dl_filesystem_name_log" {
  type        = string
  description = "The data lake filesystem resource name."
}

variable "folders" {
  description = "List of folders to create in the Data Lake"
  type        = list(string)
}


variable "blob_storage_name" {
  type        = string
  description = "The blob storage resource name."
}

variable "blob_storage_container_name" {
  type        = string
  description = "The blob storage container resource name."
}

variable "purview_account_name" {
  type        = string
  description = "The purview account resource name."
}