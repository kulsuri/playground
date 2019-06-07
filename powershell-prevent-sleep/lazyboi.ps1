param($minutes = 9999)

$myShell = New-Object -com "Wscript.Shell"

for ($i = 0; $i -lt $minutes; $i++) {

    Start-Sleep -Seconds 10

    $myShell.sendkeys("{F16}")
}