cd terraform/
terraform init
terraform import azurerm_resource_group.start /subscriptions/931c04b4-268b-4aa4-958c-5a1b5620758b/resourceGroups/Projet
terraform import azurerm_service_plan.start /subscriptions/931c04b4-268b-4aa4-958c-5a1b5620758b/resourceGroups/Projet/providers/Microsoft.Web/serverfarms/CalendarAppli
terraform import azurerm_linux_web_app.start /subscriptions/931c04b4-268b-4aa4-958c-5a1b5620758b/resourceGroups/Projet/providers/Microsoft.Web/sites/CalendarAppli
terraform import azurerm_linux_web_app.start2 /subscriptions/931c04b4-268b-4aa4-958c-5a1b5620758b/resourceGroups/Projet/providers/Microsoft.Web/sites/calendarfront