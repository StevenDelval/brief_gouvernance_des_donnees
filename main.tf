resource "azurerm_resource_group" "rg" {
  location = var.resource_group_location
  name     = var.resource_group_name
}

resource "azurerm_storage_account" "data_lake" {
  name                     = var.data_lake_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"
}

resource "azurerm_storage_data_lake_gen2_filesystem" "dl_filesystem_region" {
  for_each           = toset(var.folders)
  name               = each.value
  storage_account_id = azurerm_storage_account.data_lake.id
}

resource "azurerm_storage_data_lake_gen2_filesystem" "dl_filesystem_log" {
  name               = var.dl_filesystem_name_log
  storage_account_id = azurerm_storage_account.data_lake.id
}

resource "azurerm_storage_account" "blob_storage" {
  name                     = var.blob_storage_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
resource "azurerm_storage_container" "blob_storage_container" {
  name                  = var.blob_storage_container_name
  storage_account_name  = azurerm_storage_account.blob_storage.name
  container_access_type = "private"
}

resource "azurerm_purview_account" "purview_account" {
  name                = var.purview_account_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = "northeurope"

  identity {
    type = "SystemAssigned"
  }
}