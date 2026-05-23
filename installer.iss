[Setup]
AppName=Demo App
AppVersion=1.0.0
DefaultDirName={autopf}\Demo App
DefaultGroupName=Demo App
OutputDir=installer_output
OutputBaseFilename=DemoAppSetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "dist\DemoApp.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Demo App"; Filename: "{app}\DemoApp.exe"
Name: "{commondesktop}\Demo App"; Filename: "{app}\DemoApp.exe"

[Run]
Filename: "{app}\DemoApp.exe"; Description: "Launch Demo App"; Flags: nowait postinstall skipifsilent