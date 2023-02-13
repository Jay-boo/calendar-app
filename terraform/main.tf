##### login setup provided by mail ####

###################""
resource "azurerm_resource_group" "start" {
  name     = "Projet"
  location = "West Europe"
}

resource "azurerm_service_plan" "start" {
  name                = "CalendarAppli"
  resource_group_name = azurerm_resource_group.start.name
  location            = azurerm_resource_group.start.location
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "start" {
  name                = "CalendarAppli"
  resource_group_name = azurerm_resource_group.start.name
  location            = azurerm_resource_group.start.location
  service_plan_id     = azurerm_service_plan.start.id
  enabled             = var.AppOn   
  site_config {
  }
  app_settings                      = {
           "DOCKER_REGISTRY_SERVER_PASSWORD" = var.DOCKER_REGISTRY_SERVER_PASSWORD
           "DOCKER_REGISTRY_SERVER_URL"      = "https://projetcalendar.azurecr.io" 
          "DOCKER_REGISTRY_SERVER_USERNAME" = "Projetcalendar" 
        }
}

resource "azurerm_linux_web_app" "start2" {
  name                = "calendarfront"
  resource_group_name = azurerm_resource_group.start.name
  location            = azurerm_resource_group.start.location
  service_plan_id     = azurerm_service_plan.start.id
  enabled             = var.AppOn
  site_config {
  }
    app_settings                      = {
          "DOCKER_REGISTRY_SERVER_PASSWORD" = var.DOCKER_REGISTRY_SERVER_PASSWORD
         "DOCKER_REGISTRY_SERVER_URL"      = "https://projetcalendar.azurecr.io" 
          "DOCKER_REGISTRY_SERVER_USERNAME" = "Projetcalendar" 
        }
}

variable AppOn {
  type        = bool
  default     = true
  description = "Start or Stop App Services"
}

variable secret {
  type        = string
  default     = ""
  description = "Secret"
}

