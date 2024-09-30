$services = Get-Service | Select-Object Name, DisplayName, Status
$services | Export-Csv -Path "C:\T26\services.csv" -NoTypeInformation
