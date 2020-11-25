# Valorant ids
Recieve a List of all of Valorant's ID for the game. Includes:
  - Skins, Chromas, Levels
  - Maps
  - Attachments
  - Sprays
  - GameModes
  - Charms
  - Player Cards

## Example
 - cURL: `https://shared.na.a.pvp.net/content-service/v2/content`
 - Method: `GET`
 - Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`
    - X-Riot-ClientVersion: `CURRENT CLIENT VERSION` [Located Here](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/ClientVersions.md)

```http
  GET https://shared.na.a.pvp.net/content-service/v2/content
  Content-Type: application/json
  Authorization: Bearer riot_auth_token
  X-Riot-Entitlements-JWT: riot_entitlement_token
  X-Riot-ClientVersion: "release-01.12-3-492454"

  {
    "Characters": [
        {
            "Name": "Breach",
            "ID": "5F8D3A7F-467B-97F3-062C-13ACF203C006",
            "AssetName": "Default__Breach_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Raze",
            "ID": "F94C3B30-42BE-E959-889C-5AA313DBA261",
            "AssetName": "Default__Clay_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Skye",
            "ID": "6F2A04CA-43E0-BE17-7F36-B3908627744D",
            "AssetName": "Default__Guide_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cypher",
            "ID": "117ED9E3-49F3-6512-3CCF-0CADA7E3823B",
            "AssetName": "Default__Gumshoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sova",
            "ID": "320B2A48-4D9B-A075-30F1-1F93A9B638FA",
            "AssetName": "Default__Hunter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Killjoy",
            "ID": "1E58DE9C-4950-5125-93E9-A0AEE9F98746",
            "AssetName": "Default__Killjoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Viper",
            "ID": "707EAB51-4836-F488-046A-CDA6BF494859",
            "AssetName": "Default__Pandemic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phoenix",
            "ID": "EB93336A-449B-9C1B-0A54-A891F7921D69",
            "AssetName": "Default__Phoenix_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Brimstone",
            "ID": "9F0D8BA9-4140-B941-57D3-A7AD57C6B417",
            "AssetName": "Default__Sarge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Sage",
            "ID": "569FDD95-4D10-43AB-CA70-79BECC718B46",
            "AssetName": "Default__Thorne_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Reyna",
            "ID": "A3BFB853-43B2-7238-A4F1-AD90E9E46BCC",
            "AssetName": "Default__Vampire_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Omen",
            "ID": "8E253930-4C05-31DD-1B6C-968525494517",
            "AssetName": "Default__Wraith_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jett",
            "ID": "ADD6443A-41BD-E414-F6AD-E58D267F4E95",
            "AssetName": "Default__Wushu_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        }
    ],
    "Maps": [
        {
            "Name": "Ascent",
            "ID": "7EAECC1B-4337-BBF6-6AB9-04B8F06B3319",
            "AssetName": "Ascent",
            "AssetPath": "/Game/Maps/Ascent/Ascent",
            "IsEnabled": true
        },
        {
            "Name": "Split",
            "ID": "D960549E-485C-E861-8D71-AA9D1AED12A2",
            "AssetName": "Bonsai",
            "AssetPath": "/Game/Maps/Bonsai/Bonsai",
            "IsEnabled": true
        },
        {
            "Name": "Bind",
            "ID": "2C9D57EC-4431-9C5E-2939-8F9EF6DD5CBA",
            "AssetName": "Duality",
            "AssetPath": "/Game/Maps/Duality/Duality",
            "IsEnabled": true
        },
        {
            "Name": "Icebox",
            "ID": "E2AD5C54-4114-A870-9641-8EA21279579A",
            "AssetName": "Port",
            "AssetPath": "/Game/Maps/Port/Port",
            "IsEnabled": true
        },
        {
            "Name": "The Range",
            "ID": "EE613EE9-28B7-4BEB-9666-08DB13BB2244",
            "AssetName": "Range",
            "AssetPath": "/Game/Maps/Poveglia/Range",
            "IsEnabled": true
        },
        {
            "Name": "Shooting Range",
            "ID": "7CA9995D-4F35-DAE1-ACFB-25B8A2FB1FA0",
            "AssetName": "Range_NewPlayerExperience_Master",
            "AssetPath": "/Game/Maps/Poveglia/Range_NewPlayerExperience_Master",
            "IsEnabled": true
        },
        {
            "Name": "Haven",
            "ID": "2BEE0DC9-4FFE-519B-1CBD-7FBE763A6047",
            "AssetName": "Triad",
            "AssetPath": "/Game/Maps/Triad/Triad",
            "IsEnabled": true
        }
    ],
    "Chromas": [
        {
            "Name": "Glitchpop Odin Level 5\r\n(Variant 1 Blue)",
            "ID": "0B30B3E8-4696-7B7C-FED2-50B34234965A",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin Level 7\r\n(Variant 3 Gold)",
            "ID": "BBA7F46F-41EE-9E6C-C37A-DCA8EE4BF50E",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin Level 6\r\n(Variant 2 Red)",
            "ID": "54CAEB7F-4FC4-6ADB-45A6-CFB6202D9C24",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin",
            "ID": "9667983E-4C8C-E5B2-68D7-BE84F9B3D46C",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Odin",
            "ID": "C1ED5BF3-4827-3E3A-EBBB-1BA42A226E59",
            "AssetName": "Default__HeavyMachineGun_Grid_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Odin",
            "ID": "5DA04039-4875-92EC-759F-5B9928D12B30",
            "AssetName": "Default__HMG_Lightning_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Odin",
            "ID": "53CE97ED-47E0-4856-0446-F7BC86E869E0",
            "AssetName": "Default__HMG_Rainbow_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Odin",
            "ID": "2F93861D-4B2F-2175-AF0C-3BA0C736E257",
            "AssetName": "Default__HeavyMachineGun_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Ares",
            "ID": "45B00D43-4B76-8953-A87D-50B43C309D98",
            "AssetName": "Default__LightMachineGun_ArtDeco_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Ares",
            "ID": "0856FA2A-472A-2CC6-FB33-1C984D6CECBA",
            "AssetName": "Default__LMG_Cosmos_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 5\n(Variant 1 Blue)",
            "ID": "E0C5286E-48FF-41AF-A524-9B8DAF11F9D8",
            "AssetName": "Default__LightMachineGun_Edge_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 7\n(Variant 3 Purple)",
            "ID": "4F6C7938-4B3D-E30D-E9B7-9E97F801FE62",
            "AssetName": "Default__LightMachineGun_Edge_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 6\n(Variant 2 Red)",
            "ID": "712019A2-415B-C0B2-9228-08892EB0B1F2",
            "AssetName": "Default__LightMachineGun_Edge_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares",
            "ID": "E56C230F-447D-034F-FE57-CE935B3F8C55",
            "AssetName": "Default__LightMachineGun_Edge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Ares",
            "ID": "D2C1A05E-44CA-5BF9-21AD-48B989E164D2",
            "AssetName": "Default__LightMachineGun_Electroflux_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Ares",
            "ID": "0B299873-40D8-D0AA-0A06-04A1B7EB5BC7",
            "AssetName": "Default__LMG_Exo_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ares",
            "ID": "8C464EAD-4B0D-1590-9880-57A5B6407D4E",
            "AssetName": "Default__LightMachineGun_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Ares",
            "ID": "E6444FF5-4466-5468-BE0A-AA997A688422",
            "AssetName": "Default__LightMachineGun_Sakura_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ares",
            "ID": "B33DE820-4061-8B85-31CE-808F1A2C58F5",
            "AssetName": "Default__LightMachineGun_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Vandal",
            "ID": "D2CB89C5-4BE5-EFDE-765E-43896E6E0A48",
            "AssetName": "Default__AK_ArtDeco_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 6\r\n(Variant 2 Blue)",
            "ID": "6FB459FA-4368-7D20-106A-629DB9825A2B",
            "AssetName": "Default__AK_Dragon_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 7\r\n(Variant 3 Dark)",
            "ID": "403F7D3E-4E96-6566-42F3-01B7A803D660",
            "AssetName": "Default__AK_Dragon_Dark_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 5\r\n(Variant 1 Red)",
            "ID": "A9873BD5-41F9-170D-27F0-ABB68FEA0CE9",
            "AssetName": "Default__AK_Dragon_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal",
            "ID": "835AD8E3-4B0E-071B-CE38-00A05032AC43",
            "AssetName": "Default__AK_Dragon_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Vandal",
            "ID": "10B9C4D7-448D-508D-25F6-A39EDF95A79F",
            "AssetName": "Default__AK_Exo_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Vandal",
            "ID": "9FF28C95-4E69-56B2-6980-E09B503572BB",
            "AssetName": "Default__AK_Gothic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Vandal",
            "ID": "2BE20A2A-4582-B689-F00E-A98DAFAD65EB",
            "AssetName": "Default__AK_Grid_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 6 \r\n(Variant 2 Blue)",
            "ID": "CD3EBDC1-4858-EFDA-6CEE-C683726F8CA9",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 5 \r\n(Variant 1 Orange)",
            "ID": "AD2B0B8B-4DA8-9C88-331A-028F2026AB66",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Orange_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal",
            "ID": "A26E0D1D-4886-7D62-6B4F-1996E706463D",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 7\r\n(Variant 3 Yellow)",
            "ID": "D43B8D21-4FB2-1224-1392-53AB6D829ED1",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Yellow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Vandal",
            "ID": "3B47B889-493B-B28F-131B-ADAF01E18970",
            "AssetName": "Default__AK_Ice_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Vandal",
            "ID": "86F3352F-49B1-603F-6752-60BDFCDDF318",
            "AssetName": "Default__AK_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Vandal",
            "ID": "E5CA1AD8-4548-43F8-13B3-A89CC50AA319",
            "AssetName": "Default__AK_Rainbow_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Vandal",
            "ID": "40813A80-401B-5260-188A-0F9ADF807AE4",
            "AssetName": "Default__AK_Sakura_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 6\n(Variant 2 Black)",
            "ID": "DB4461E5-40DD-1173-3B64-E5836F92F4DD",
            "AssetName": "Default__AK_Soulstealer_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 5\n(Variant 1 Red)",
            "ID": "B2A065C0-4632-CCAA-F496-7681DC2A6185",
            "AssetName": "Default__AK_Soulstealer_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal",
            "ID": "2BD28382-48C6-8579-83E8-E9B64B783DE3",
            "AssetName": "Default__AK_Soulstealer_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 7\n(Variant 3 White)",
            "ID": "B2619C1C-4974-4F06-F37B-C68B1D6D7BD1",
            "AssetName": "Default__AK_Soulstealer_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vandal",
            "ID": "19629AE1-4996-AE98-7742-24A240D41F99",
            "AssetName": "Default__AssaultRifle_AK_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Vandal",
            "ID": "57EE65CC-4B0B-0460-7C05-43890E3B5792",
            "AssetName": "Default__AK_Unstoppable_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Vandal Level 2\r\n(Variant 1 Red)",
            "ID": "81513FC3-431E-7A4F-0EF4-13B3D696433A",
            "AssetName": "Default__AK_Unstoppable_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Vandal Level 3\r\n(Variant 2 Tan)",
            "ID": "416373EC-427A-A8EC-DFD0-FC9BD2772A18",
            "AssetName": "Default__AK_Unstoppable_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Vandal Level 4\r\n(Variant 3 Pink)",
            "ID": "DE316506-4CA5-8228-0550-19B47327B705",
            "AssetName": "Default__AK_Unstoppable_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Vandal",
            "ID": "849B5754-47C2-38F2-F912-A796B0644307",
            "AssetName": "Default__AK_Wasteland_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "D2710367-42B2-CF4E-8B87-2F9D09A41261",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 5\r\n(Variant 1 Blue)",
            "ID": "E4AFD93D-43F4-948C-7E6A-F88B1549409B",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 7\r\n(Variant 3 Gold)",
            "ID": "293D9DDB-41EF-387F-3D71-908384B6AD87",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 6\r\n(Variant 2 Red)",
            "ID": "0D00F717-409F-ABB7-B5E1-9CBD3DCD2752",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog",
            "ID": "F7DD47C7-467B-36F1-0D13-BEB53372B666",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Bulldog",
            "ID": "F9EC80F9-498B-FAB1-CC27-9C867AA1DE49",
            "AssetName": "Default__AssaultRifle_Burst_Electroflux_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Bulldog",
            "ID": "561FA49E-465E-51EB-4517-93AB0105FF44",
            "AssetName": "Default__AssaultRifle_Burst_LIW_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Bulldog",
            "ID": "28CF13A9-4457-027E-2C1F-6388CCC870F0",
            "AssetName": "Default__Burst_Polyanimals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bulldog",
            "ID": "BF35F404-4A14-6953-CED2-5BAFD21639A0",
            "AssetName": "Default__AssaultRifle_Burst_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Bulldog",
            "ID": "1789BE1E-42FB-A43A-2F40-EB9B793481B0",
            "AssetName": "Default__Burst_Triangles_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Phantom",
            "ID": "388DADA2-4BBD-0CD9-F9A9-4C9B66C64240",
            "AssetName": "Default__Carbine_Cosmos_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 5\n(Variant 1 Blue)",
            "ID": "A5529EC0-4BC2-D6C1-7699-A1A3D3809313",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 7\n(Variant 3 Purple)",
            "ID": "A99AC58B-41B0-E1CD-89FD-F3AD171410DF",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 6\n(Variant 2 Red)",
            "ID": "6A3A49BB-4DAF-7C92-3497-299A59836322",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom",
            "ID": "36D14EC2-4376-A355-AD98-BDBC9B4B9E9A",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Phantom",
            "ID": "2E3B98B6-46E9-E233-1E1B-269EBD84598A",
            "AssetName": "Default__AssaultRifle_ACR_Electroflux_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Phantom",
            "ID": "F9BDE748-403A-ACD2-E760-33B8EA9C1B80",
            "AssetName": "Default__AssaultRifle_ACR_Ice_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Phantom",
            "ID": "940B7589-4F19-A242-B038-838E3BDA51AC",
            "AssetName": "Default__AssaultRifle_ACR_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Phantom",
            "ID": "DC9BD4ED-4CC5-5596-940A-F5ACFB1B9907",
            "AssetName": "Default__Carbine_Jade_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Phantom",
            "ID": "83697AAA-415D-3EC3-0205-FCAB8DE464D2",
            "AssetName": "Default__AssaultRifle_ACR_Kingdom_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Phantom",
            "ID": "3AF79E9D-4E55-425E-22DA-DCAB4985706A",
            "AssetName": "Default__AssaultRifle_ACR_Lightning_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom Level 4\r\n(Variant 3 Blue)",
            "ID": "899C3879-4EE6-F67C-C406-82A763629414",
            "AssetName": "Default__Carbine_MagicSpline_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom Level 2\r\n(Variant 1 Green)",
            "ID": "FAC4D97F-4784-BE17-2670-698634C68837",
            "AssetName": "Default__Carbine_MagicSpline_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom Level 3\r\n(Variant 2 Red)",
            "ID": "DDC98143-4D65-B683-4476-01B8ABA85CE6",
            "AssetName": "Default__Carbine_MagicSpline_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom",
            "ID": "C755DCD9-4CE8-86B5-4F1F-AB96A32DE2F1",
            "AssetName": "Default__AssaultRifle_ACR_MagicSpline_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Phantom",
            "ID": "7A53DD42-48C0-DDF9-424D-D7BB478A24AD",
            "AssetName": "Default__AssaultRifle_ACR_Murals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom",
            "ID": "B9C9EB56-4CBD-04B7-06A8-329DC6F1E73A",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 5\r\n(Variant 1 Black)",
            "ID": "B639A920-424B-B855-1E30-7F9B026889F1",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 6\r\n(Variant 2 Green)",
            "ID": "6F9C7109-485A-F2A3-CB1D-9F9A31A995D7",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom",
            "ID": "6096A66F-43D2-D4AD-6421-84AEE3386921",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 7\r\n(Variant 3 White)",
            "ID": "32DFE871-4906-D2CE-4835-2D99AAA52F84",
            "AssetName": "Default__AssaultRifle_ACR_Oni_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phantom",
            "ID": "52221BA2-4E4C-EC76-8C81-3483506D5242",
            "AssetName": "Default__AssaultRifle_ACR_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Glitchpop Judge Level 5\r\n(Variant 1 Blue)",
            "ID": "2ABE2D6A-4D38-434A-FF64-608B936C2661",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge Level 7\r\n(Variant 3 Gold)",
            "ID": "BB88381F-423F-CD76-9AC1-7E9FE541CF25",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge Level 6\r\n(Variant 2 Red)",
            "ID": "1E959CBE-4649-A049-F789-B2B9C9D7EC26",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge",
            "ID": "5966C88B-4662-BE62-5AE6-50BC036700B5",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 6\r\n(Variant 2 Blue)",
            "ID": "EDE643C7-4B83-0FD4-13D1-1C9DDB4D34CD",
            "AssetName": "Default__AutomaticShotgun_Dragon_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 7\r\n(Variant 3 Dark)",
            "ID": "EC9CAA7A-43FF-8F04-52A7-27A46DE24F6E",
            "AssetName": "Default__AutomaticShotgun_Dragon_Dark_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 5\r\n(Variant 1 Red)",
            "ID": "87E27487-4705-8060-5D07-C6A6DC927F09",
            "AssetName": "Default__AutomaticShotgun_Dragon_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge",
            "ID": "72B9E3F7-427F-3D24-F618-11B0F28FEB89",
            "AssetName": "Default__AutomaticShotgun_Dragon_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Judge",
            "ID": "D770DF24-4AAB-3377-A790-A2AFD30010E7",
            "AssetName": "Default__AutomaticShotgun_Electroflux_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Judge",
            "ID": "066F07A2-42C5-4197-497A-F0A3FDBB4A6B",
            "AssetName": "Default__AutomaticShotgun_Grid_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Judge",
            "ID": "7242D958-42F4-CA19-BB8B-7DB67DE3D8C5",
            "AssetName": "Default__AutoShotgun_Jade_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Judge",
            "ID": "B56DC59C-4B76-BEE2-9896-A5B778041865",
            "AssetName": "Default__AutomaticShotgun_Lightning_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Judge",
            "ID": "5FC0A963-47D1-9336-DDF1-0C99D7169AD8",
            "AssetName": "Default__AutomaticShotgun_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Judge",
            "ID": "A0D5B67E-42EE-E831-F1B7-A39CB4F375F5",
            "AssetName": "Default__AutoShotgun_Polyanimals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Judge",
            "ID": "DB80E068-4982-828E-6670-C59C91B692B8",
            "AssetName": "Default__AutoShotgun_Rainbow_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Judge",
            "ID": "B71AE8D6-44BB-AA4C-0D2A-DC9ED9E66410",
            "AssetName": "Default__AutomaticShotgun_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Judge",
            "ID": "5F0E190D-4693-F36A-3F63-B9BD22B1B379",
            "AssetName": "Default__AutomaticShotgun_Triangles_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Bucky",
            "ID": "17F8E996-4440-2011-DA74-1DAC76F5671A",
            "AssetName": "Default__PumpShotgun_CrimsonOps_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky",
            "ID": "2C782AFA-45AE-CB96-370E-95852272B2BB",
            "AssetName": "Default__PumpShotgun_Electroflux3_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky Level 2\r\n(Variant 1 Black)",
            "ID": "FD6330D1-4EEA-006D-24AC-57A31D5C004D",
            "AssetName": "Default__PumpShotgun_Electroflux3_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky Level 3\r\n(Variant 2 Yellow)",
            "ID": "8C6CBE68-4CA1-2EE3-177E-C6BBFFDBA724",
            "AssetName": "Default__PumpShotgun_Electroflux3_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky Level 4\r\n(Variant 3 Blue)",
            "ID": "9B63BE2E-49F4-B05C-9DFB-E0929A36365C",
            "AssetName": "Default__PumpShotgun_Electroflux3_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Bucky",
            "ID": "8BB9C93C-4F27-89F8-3BF7-06B9101DAA85",
            "AssetName": "Default__PumpShotgun_Kingdom_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Bucky",
            "ID": "2B9AAF1D-492A-FCB7-B22B-4C8BA8D67EFA",
            "AssetName": "Default__PumpShotgun_Murals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky",
            "ID": "21693F40-42E4-01A7-B4B2-529FD774BFCE",
            "AssetName": "Default__PumpShotgun_Oblivion_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 5\r\n(Variant 1 Black)",
            "ID": "11737623-4661-BFEA-CA37-08803BDD6D95",
            "AssetName": "Default__PumpShotgun_Oni_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 6\r\n(Variant 2 Green)",
            "ID": "243F999F-4987-7826-4C9E-1CA5BDE88212",
            "AssetName": "Default__PumpShotgun_Oni_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky",
            "ID": "88D497C4-4D21-22D6-02D0-6CAEF087D263",
            "AssetName": "Default__PumpShotgun_Oni_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 7\r\n(Variant 3 White)",
            "ID": "79D385FB-4013-E9A3-A191-D4979C13EC58",
            "AssetName": "Default__PumpShotgun_Oni_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky Level 4\r\n(Variant 2 Black)",
            "ID": "5F9CCDE4-456A-67EB-0A7B-D1B8FD0B0258",
            "AssetName": "Default__PumpShotgun_Raygun_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky Level 3\r\n(Variant 1 Chrome)",
            "ID": "822401FE-4388-C203-3784-A0958885BE07",
            "AssetName": "Default__PumpShotgun_Raygun_Chrome_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky Level 5\r\n(Variant 3 RWB)",
            "ID": "AF2C044E-4C83-04A4-BC7A-42A16BE55796",
            "AssetName": "Default__PumpShotgun_Raygun_RWB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky",
            "ID": "BA632E0D-4F74-2B45-5094-C2BAA0764CD6",
            "AssetName": "Default__PumpShotgun_Raygun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bucky",
            "ID": "3D8FFCFE-4786-0180-42D7-E1BE18DD1CAB",
            "AssetName": "Default__PumpShotgun_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "RagnaRocker Frenzy",
            "ID": "F4143C4C-4FA2-4922-C228-60A276BC9D7F",
            "AssetName": "Default__AutomaticPistol_Breach_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 5\r\n(Variant 1 Blue)",
            "ID": "3B04C752-4564-E7C4-CDF6-7F9C741E3587",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 7\r\n(Variant 3 Gold)",
            "ID": "B923BCC8-4CB8-2A19-070E-588686AAE090",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 6\r\n(Variant 2 Red)",
            "ID": "AB6E58B2-49A3-E0E8-1240-DF94230393D5",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy",
            "ID": "DE8EA7BB-4006-906D-D1C7-25AE5CCB8B48",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 6\r\n(Variant 2 Blue)",
            "ID": "A0E8D567-4673-2F0C-7BB0-DEBB86D3F4EF",
            "AssetName": "Default__AutomaticPistol_Dragon_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 7\r\n(Variant 3 Dark)",
            "ID": "3F8B9999-4A92-DE0A-8A0A-4EBF04258950",
            "AssetName": "Default__AutomaticPistol_Dragon_Dark_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 5\r\n(Variant 1 Red)",
            "ID": "F40759FA-4A3A-3BB1-484E-4FABF878A774",
            "AssetName": "Default__AutomaticPistol_Dragon_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy",
            "ID": "EEE0C458-474A-B80F-871C-C188F3929A79",
            "AssetName": "Default__AutomaticPistol_Dragon_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Frenzy",
            "ID": "1EE55FE2-49B9-67D3-13C3-6CBF7B8A23EF",
            "AssetName": "Default__AutomaticPistol_Electroflux_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Swooping Frenzy",
            "ID": "8A7F5A9A-4865-8908-93BD-1F96F04EC8C3",
            "AssetName": "Default__AutoPistol_Guide_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Frenzy",
            "ID": "67DB243D-4393-F827-50AB-69BADCA7B162",
            "AssetName": "Default__AutomaticPistol_LIW_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spitfire Frenzy",
            "ID": "5A649A38-4C12-FB73-FC12-9F975495716F",
            "AssetName": "Default__AutomaticPistol_Phoenix_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Frenzy",
            "ID": "B5C7C3D6-4242-C174-470C-7B9BC1D188C4",
            "AssetName": "Default__AutoPistol_Rainbow_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Frenzy",
            "ID": "DC99ED5A-4D75-87A0-C921-75963EA3C1E1",
            "AssetName": "Default__AutomaticPistol_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Pistolinha Classic",
            "ID": "2FF2A004-4A1B-BF7D-4184-F5B68DE24C99",
            "AssetName": "Default__BasePistol_Clay_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Classic",
            "ID": "900BECAB-4E59-38D1-C668-449A236142CC",
            "AssetName": "Default__BasePistol_CrimsonOps_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic",
            "ID": "6B9217F8-412D-F482-B2FC-589575A743E2",
            "AssetName": "Default__BasePistol_Electroflux3_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic Level 2\r\n(Variant 1 Black)",
            "ID": "DE707E76-42ED-7D5F-9E78-109AC570EBBE",
            "AssetName": "Default__BasePistol_Electroflux3_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic Level 3\r\n(Variant 2 Yellow)",
            "ID": "C8AA859B-437E-ECC9-4181-759741401890",
            "AssetName": "Default__BasePistol_Electroflux3_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic Level 4\r\n(Variant 3 Blue)",
            "ID": "E768683A-4926-8C5B-B47D-86A8157DBE61",
            "AssetName": "Default__BasePistol_Electroflux3_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 6 \r\n(Variant 2 Blue)",
            "ID": "02390051-4309-22D4-B733-C09FBFCF2E7F",
            "AssetName": "Default__BasePistol_HypeBeast_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 5\r\n(Variant 1 Orange)",
            "ID": "42280760-422F-B5D1-4255-1E8993A817A4",
            "AssetName": "Default__BasePistol_HypeBeast_Orange_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic",
            "ID": "D9DCE0EC-464C-DF67-63A3-1F9A05D322AD",
            "AssetName": "Default__BasePistol_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 7 \r\n(Variant 3 Yellow)",
            "ID": "9FCC46A1-42F8-6407-787D-CB9D3E0BB718",
            "AssetName": "Default__BasePistol_HypeBeast_Yellow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Classic",
            "ID": "4BD1574A-436B-EAFB-3611-588A44EF066A",
            "AssetName": "Default__BasePistol_Ice_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Classic",
            "ID": "E7644F3C-42D3-8336-5135-17A4883032FD",
            "AssetName": "Default__BasePistol_Kingdom_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Classic",
            "ID": "6853E4E7-4241-A574-F4CD-0D9949008CFE",
            "AssetName": "Default__BasePistol_Lightning_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic Level 4\r\n(Variant 3 Blue)",
            "ID": "47650AC0-462F-8672-777F-31AE009D5B40",
            "AssetName": "Default__BasePistol_MagicSpline_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic Level 2\r\n(Variant 1 Green)",
            "ID": "1879F636-45FA-DCA9-6C8A-13878F0CE6FF",
            "AssetName": "Default__BasePistol_MagicSpline_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic Level 3\r\n(Variant 2 Red)",
            "ID": "0DFC6D38-47A6-AB00-A8ED-FA831CE40224",
            "AssetName": "Default__BasePistol_MagicSpline_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic",
            "ID": "8F71E44B-4EAE-3963-C71B-11A2167D34DC",
            "AssetName": "Default__BasePistol_MagicSpline_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Classic",
            "ID": "AB72692D-4447-3CB0-E8A8-30AC11D82213",
            "AssetName": "Default__BasePistol_Murals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic Level 4\r\n(Variant 2 Black)",
            "ID": "39D5DA8E-4E4E-E2A2-30A9-E8B7785225E4",
            "AssetName": "Default__BasePistol_Raygun_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic Level 3\r\n(Variant 1 Chrome)",
            "ID": "E410EFF8-4AAE-3ED3-D2EC-71BCB45954D1",
            "AssetName": "Default__BasePistol_Raygun_Chrome_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic Level 5\r\n(Variant 3 RWB)",
            "ID": "BF7A6BA8-4E33-9499-F829-DC9230D458DE",
            "AssetName": "Default__BasePistol_Raygun_RWB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic",
            "ID": "16B745AC-4E5F-10AB-32B0-FA8384ECB69F",
            "AssetName": "Default__BasePistol_Raygun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Classic",
            "ID": "1BCFD66F-4EFF-E119-387E-94868AD48A29",
            "AssetName": "Default__BasePistol_Sakura_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Classic",
            "ID": "4B2D5B4F-4955-4208-286C-ABADEC250CDD",
            "AssetName": "Default__BasePistol_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Final Chamber Classic",
            "ID": "528232A1-4D11-E724-5C1B-B3BB0C392C84",
            "AssetName": "Default__BasePistol_Thorne_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Ghost",
            "ID": "12966603-4CB3-03DD-BF2E-338FB15D144F",
            "AssetName": "Default__LugerPistol_Grid_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hush Ghost",
            "ID": "B412E61C-4001-8FAB-C5E9-6EB7CAA41E88",
            "AssetName": "Default__LugerPistol_Gumshoe_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ghost",
            "ID": "BEA3E75C-4156-E05D-DD06-70ACF06CCF96",
            "AssetName": "Default__LugerPistol_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Ghost",
            "ID": "27E0B39A-4F38-D19E-FA71-40B63567A909",
            "AssetName": "Default__Luger_Jade_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Ghost",
            "ID": "F0D9BAD3-4C59-743E-C5DA-54BAB6D7C328",
            "AssetName": "Default__Luger_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 5\r\n(Variant 1 Gold)",
            "ID": "9ACF9E55-46B9-5061-F1E7-4FA996FB96C1",
            "AssetName": "Default__LugerPistol_Sovereign_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 7\r\n(Variant 3 Purple)",
            "ID": "C208E6A1-4BB8-E1D9-6943-848DB2AAF3BB",
            "AssetName": "Default__LugerPistol_Sovereign_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 6\r\n(Variant 2 Silver)",
            "ID": "357A60E7-431E-F7AD-847E-1DA16897B1F7",
            "AssetName": "Default__LugerPistol_Sovereign_Silver_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost",
            "ID": "A84764D9-4F1E-A652-3530-1497E2505285",
            "AssetName": "Default__LugerPistol_Sovereign_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ghost",
            "ID": "947A28B6-4E0F-61FB-E795-BC9A5E7B7129",
            "AssetName": "Default__LugerPistol_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Ghost",
            "ID": "C8E92EFE-4CDE-8C70-4D8B-32BF22F72091",
            "AssetName": "Default__Luger_Unstoppable_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Ghost Level 2\r\n(Variant 1 Red)",
            "ID": "ADF994F1-4B88-4E97-905E-4AAA63E55924",
            "AssetName": "Default__Luger_Unstoppable_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Ghost Level 3\r\n(Variant 2 Tan)",
            "ID": "8F4895D8-43F6-1B3B-B193-8F94D8E13F8F",
            "AssetName": "Default__Luger_Unstoppable_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Ghost Level 4\r\n(Variant 3 Pink)",
            "ID": "947C8920-401C-44E2-A11C-5E97B8CE5AFF",
            "AssetName": "Default__Luger_Unstoppable_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vendetta Ghost",
            "ID": "5832A762-4343-83A7-1595-7FB35B7CD50D",
            "AssetName": "Default__LugerPistol_Vampire_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Soul Silencer Ghost",
            "ID": "2A46E69B-4458-15EA-9D8D-A984F1265098",
            "AssetName": "Default__LugerPistol_Wraith_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Sheriff",
            "ID": "D7216A04-4148-E210-8CC7-E1AAF06255F2",
            "AssetName": "Default__RevolverPistol_ArtDeco_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Sheriff",
            "ID": "27881222-49EA-88B1-C2F6-C5B440ED91C1",
            "AssetName": "Default__Revolver_Cosmos_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 5\n(Variant 1 Blue)",
            "ID": "78C77AE1-4987-223D-720E-C596CD1F3A6C",
            "AssetName": "Default__RevolverPistol_Edge_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 7\n(Variant 3 Purple)",
            "ID": "79DA7132-4804-47FC-3249-AB9DEC5752A9",
            "AssetName": "Default__RevolverPistol_Edge_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 6\n(Variant 2 Red)",
            "ID": "47CD743F-4FAB-88B9-5341-668BC62C0983",
            "AssetName": "Default__RevolverPistol_Edge_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff",
            "ID": "00831706-4E60-D5F9-B600-E38BE89828D0",
            "AssetName": "Default__RevolverPistol_Edge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff",
            "ID": "3B0C66B7-40C7-44FC-CDA7-38A7EEC2D40E",
            "AssetName": "Default__Revolver_Electroflux3_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff Level 2\r\n(Variant 1 Black)",
            "ID": "FA6617B7-4091-C604-A6D1-21A054B5C9E4",
            "AssetName": "Default__Revolver_Electroflux3_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff Level 3\r\n(Variant 2 Yellow)",
            "ID": "475FE183-476E-F9A6-9134-24A506D65823",
            "AssetName": "Default__Revolver_Electroflux3_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff Level 4\r\n(Variant 3 Blue)",
            "ID": "F0665A84-48CD-DA41-C46D-148F8802FAD2",
            "AssetName": "Default__Revolver_Electroflux3_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Protektor Sheriff",
            "ID": "6671A60E-483F-706A-C59D-0697A1865F60",
            "AssetName": "Default__RevolverPistol_Hunter_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff",
            "ID": "D3F81911-44E7-F0C1-CC6C-34BDA3BFF6D3",
            "AssetName": "Default__RevolverPistol_Oblivion_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Sheriff",
            "ID": "BCD0BD1C-4FB4-461C-2E71-8F82DE5FD734",
            "AssetName": "Default__Revolver_Polyanimals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Sheriff",
            "ID": "D6F9AE74-45F0-B72A-593F-9B9D9A8CC929",
            "AssetName": "Default__RevolverPistol_Sakura_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Peacekeeper Sheriff",
            "ID": "1DD0FFFF-4B70-A7A2-2F22-1E97FBCE6DAE",
            "AssetName": "Default__RevolverPistol_Sarge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 6\n(Variant 2 Black)",
            "ID": "8D7B103A-4C81-3C67-EBB5-51AB29AEF327",
            "AssetName": "Default__RevolverPistol_Soulstealer_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 5\n(Variant 1 Red)",
            "ID": "C17B4920-4379-99EF-1D56-9CB9C2645D1E",
            "AssetName": "Default__RevolverPistol_Soulstealer_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff",
            "ID": "C092687F-4AF4-F843-F68B-B989000E240D",
            "AssetName": "Default__RevolverPistol_Soulstealer_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 7\n(Variant 3 White)",
            "ID": "2BA467BC-4DF2-4841-BEDB-99B17C7BD067",
            "AssetName": "Default__RevolverPistol_Soulstealer_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sheriff",
            "ID": "5A59BD61-48A9-AF61-C00F-4AA21DECA9A8",
            "AssetName": "Default__RevolverPistol_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Sheriff",
            "ID": "A74B5B26-4BF2-3D4C-4176-15806EBED55E",
            "AssetName": "Default__RevolverPistol_Triangles_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Sheriff",
            "ID": "E75D09B4-4C8B-D9BF-F190-F9A844F3C474",
            "AssetName": "Default__RevolverPistol_Wasteland_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "1CBE1B6F-4914-652C-48D8-8FBB028CEFF0",
            "AssetName": "Default__RevolverPistol_Wushu_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Shorty",
            "ID": "ABD361B4-43A6-728C-376A-529B1F599AB9",
            "AssetName": "Default__Slim_Exo_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Shorty",
            "ID": "EF08044D-4934-A38F-0FF9-63886354D59B",
            "AssetName": "Default__SawedOffShotgun_Gothic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wunderkind Shorty",
            "ID": "EB54DECA-4AE4-07C5-F506-8F9F2EC6331B",
            "AssetName": "Default__Slim_Killjoy_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 5\r\n(Variant 1 Black)",
            "ID": "1C6F1255-410D-5927-0C48-24B3E43CB468",
            "AssetName": "Default__SawedOffShotgun_Oni_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 6\r\n(Variant 2 Green)",
            "ID": "114F03D3-44CA-27D6-9DBE-22BD65A8A3B9",
            "AssetName": "Default__SawedOffShotgun_Oni_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty",
            "ID": "212DF9B7-4F66-CE5D-687A-A8A80C7B5976",
            "AssetName": "Default__SawedOffShotgun_Oni_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 7\r\n(Variant 3 White)",
            "ID": "779EFCC7-4756-14FA-6226-E4909008F56A",
            "AssetName": "Default__SawedOffShotgun_Oni_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Snakebite Shorty",
            "ID": "1C197677-4FC6-E4C8-69F3-389888E5B063",
            "AssetName": "Default__SawedOffShotgun_Pandemic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Shorty",
            "ID": "95608504-4C8B-1408-1612-0F8200421C49",
            "AssetName": "Default__SawedOffShotgun_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Shorty",
            "ID": "701655F9-43D8-1C72-F567-ACAC565FD353",
            "AssetName": "Default__Slim_Wasteland_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Operator",
            "ID": "B0B63CB6-449F-6249-9388-B0B993EB1CC2",
            "AssetName": "Default__BoltSniper_CrimsonOps_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 6\r\n(Variant 2 Blue)",
            "ID": "37CCA29B-4468-A01E-E31B-8F8978A81EEF",
            "AssetName": "Default__BoltSniper_Dragon_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 7\r\n(Variant 3 Dark)",
            "ID": "296DCDDB-4FBF-8834-BC01-44ACAC66DC60",
            "AssetName": "Default__BoltSniper_Dragon_Dark_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 5\r\n(Variant 1 Red)",
            "ID": "A8B125E5-4E33-953D-D02C-37AD9E284B6A",
            "AssetName": "Default__BoltSniper_Dragon_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator",
            "ID": "61583C81-4332-FF81-2EDE-2A8248863C80",
            "AssetName": "Default__BoltSniper_Dragon_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Operator",
            "ID": "1522AAC3-4C78-B8F0-6A80-118B00D3B850",
            "AssetName": "Default__BoltSniper_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Operator",
            "ID": "6A0320AC-4CFC-C805-F75C-B9879CD842C1",
            "AssetName": "Default__BoltSniper_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator Level 4\r\n(Variant 3 Blue)",
            "ID": "C7CFD8F6-4982-B03A-044F-A381C93778BF",
            "AssetName": "Default__BoltSniper_MagicSpline_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator Level 2\r\n(Variant 1 Green)",
            "ID": "1CA546BF-4E4D-AD47-0761-74A09E793A1A",
            "AssetName": "Default__BoltSniper_MagicSpline_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator Level 3\r\n(Variant 2 Red)",
            "ID": "CE7B7AF1-47ED-F1DE-E1BC-ABA69FC3861D",
            "AssetName": "Default__BoltSniper_MagicSpline_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator",
            "ID": "BE0446FF-444C-2AB4-DE70-599D8A152AB8",
            "AssetName": "Default__BoltSniper_MagicSpline_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator",
            "ID": "54EA8BA8-4BCB-EB63-70D2-4DA7520FADE2",
            "AssetName": "Default__BoltSniper_Oblivion_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator Level 4\r\n(Variant 2 Black)",
            "ID": "D3E0FA29-4BA2-E2E3-C829-C9AEE0768585",
            "AssetName": "Default__BoltSniper_Raygun_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator Level 3\r\n(Variant 1 Chrome)",
            "ID": "F5C22F67-4E6F-C23D-24BD-3BB19CF3BF62",
            "AssetName": "Default__BoltSniper_Raygun_Chrome_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator Level 5\r\n(Variant 3 RWB)",
            "ID": "B867C4A0-408C-2F04-2E8E-36A22E85C8F2",
            "AssetName": "Default__BoltSniper_Raygun_RWB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator",
            "ID": "FC0A7435-4786-E732-9F08-A6A9E84F42CE",
            "AssetName": "Default__BoltSniper_Raygun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 6\n(Variant 2 Black)",
            "ID": "319D9F49-46A9-BE17-9B08-CFB1A766FA37",
            "AssetName": "Default__BoltSniper_Soulstealer_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 5\n(Variant 1 Red)",
            "ID": "0B29F645-404F-F9D2-2165-C6BF5B16572F",
            "AssetName": "Default__BoltSniper_Soulstealer_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator",
            "ID": "27865910-4DD4-845F-8671-92988CC1C996",
            "AssetName": "Default__BoltSniper_Soulstealer_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 7\n(Variant 3 White)",
            "ID": "4244D37B-4129-175D-A2DC-98A8E1DE89C6",
            "AssetName": "Default__BoltSniper_Soulstealer_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Operator",
            "ID": "4914F50D-49F9-6424-CA80-9486C45A138D",
            "AssetName": "Default__BoltSniper_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Operator",
            "ID": "5D5942C0-4824-11E9-0E91-65B4B76D3BEA",
            "AssetName": "Default__BoltSniper_Triangles_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Guardian",
            "ID": "E6F6E321-4DE6-5D25-69EA-BAA30D693373",
            "AssetName": "Default__DMR_Cosmos_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Guardian",
            "ID": "5E4D839C-4F56-5173-088E-5CAC4A2E5E67",
            "AssetName": "Default__DMR_Gothic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 6\r\n(Variant 2 Blue)",
            "ID": "E866F273-4ACC-806F-BECD-56A6BEF48FBC",
            "AssetName": "Default__DMR_HypeBeast_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 5\r\n(Variant 1 Orange)",
            "ID": "4CA16478-40C7-2CF6-BDD2-099761921E61",
            "AssetName": "Default__DMR_HypeBeast_Orange_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian",
            "ID": "E2F5A979-4E9A-F931-7F52-D99F0EC4A61B",
            "AssetName": "Default__DMR_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 7\r\n(Variant 3 Yellow)",
            "ID": "22F831DB-4E55-6280-9078-D9B63AE93E4D",
            "AssetName": "Default__DMR_HypeBeast_Yellow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Guardian",
            "ID": "FC0C6D41-496E-5AC5-6C8F-9787F4E71C0D",
            "AssetName": "Default__DMR_Murals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 5\r\n(Variant 1 Black)",
            "ID": "AED44A0E-4834-0EC9-AB68-729F22189BAD",
            "AssetName": "Default__DMR_Oni_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 6\r\n(Variant 2 Green)",
            "ID": "A8A73B3A-4608-6BEF-DD1B-0CBB8AB7D2E4",
            "AssetName": "Default__DMR_Oni_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian",
            "ID": "9E97DE52-4080-8311-2505-8FAADE37FE46",
            "AssetName": "Default__DMR_Oni_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 7\r\n(Variant 3 White)",
            "ID": "2C754236-407D-5708-61DA-ADA2F7821FB4",
            "AssetName": "Default__DMR_Oni_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Guardian",
            "ID": "FF80BBBF-4212-5289-32A4-1B8DA95F52CA",
            "AssetName": "Default__DMR_Polyanimals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 6\n(Variant 2 Black)",
            "ID": "C0F23DC2-4AC3-338C-C559-18962151A702",
            "AssetName": "Default__DMR_SoulStealer_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 5\n(Variant 1 Red)",
            "ID": "13276940-43E7-9ECE-8661-DCA6E8707847",
            "AssetName": "Default__DMR_SoulStealer_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian",
            "ID": "BB9F9FB7-46CA-4DDF-1B83-B8B1FC0401D9",
            "AssetName": "Default__DMR_SoulStealer_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 7\n(Variant 3 White)",
            "ID": "C18A9C89-4B1E-79CD-8A30-5EA5368214FC",
            "AssetName": "Default__DMR_SoulStealer_White_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 5\r\n(Variant 1 Gold)",
            "ID": "6C21B2DD-4D36-7BB6-667B-E5874B7BDA13",
            "AssetName": "Default__DMR_Sovereign_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 7\r\n(Variant 3 Purple)",
            "ID": "94D1A053-4A0F-8D48-EC77-73AAA2003A22",
            "AssetName": "Default__DMR_Sovereign_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 6\r\n(Variant 2 Silver)",
            "ID": "B5280469-4069-B125-C76A-D28E20791322",
            "AssetName": "Default__DMR_Sovereign_Silver_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian",
            "ID": "DF1786B2-4F3D-F207-B92C-0780F4DFFB79",
            "AssetName": "Default__DMR_Sovereign_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Guardian",
            "ID": "0F934388-418A-A9E7-42A7-21B27402E46C",
            "AssetName": "Default__DMR_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Guardian",
            "ID": "4648ECFB-4667-77B7-2723-D3A531A942EA",
            "AssetName": "Default__DMR_Unstoppable_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Guardian Level 2\r\n(Variant 1 Red)",
            "ID": "2DE61652-4285-E5CD-9F85-159B43BB4E9E",
            "AssetName": "Default__DMR_Unstoppable_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Guardian Level 3\r\n(Variant 2 Tan)",
            "ID": "B8A7C66D-4DC8-D849-3FE7-5BBC0A6A4C35",
            "AssetName": "Default__DMR_Unstoppable_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Guardian Level 4\r\n(Variant 3 Pink)",
            "ID": "9D725C7C-4FB4-7A89-4798-B7AF46065668",
            "AssetName": "Default__DMR_Unstoppable_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Marshal",
            "ID": "609F948B-4D2E-99EE-631E-B98A74468877",
            "AssetName": "Default__LeverSniper_Gothic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Marshal",
            "ID": "3EE65B06-48E5-5046-DB49-65B0635AC005",
            "AssetName": "Default__LeverSniper_Ice_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Marshal",
            "ID": "727BB66D-40E5-49E4-6368-44B95C56E8E0",
            "AssetName": "Default__LeverSniper_LIW_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard",
            "ID": "F9800505-4923-A557-494B-02BF4C47EC2B",
            "AssetName": "Default__LeverSniper_Murals_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 5\r\n(Variant 1 Gold)",
            "ID": "079E90B2-4492-3F73-95BD-F5B74A7AC295",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 7\r\n(Variant 3 Purple)",
            "ID": "9D77ED46-4375-65FE-5C2B-54B44BD8E832",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 6\r\n(Variant 2 Silver)",
            "ID": "0BB4EAB3-4C4D-8B6E-1AF5-DAA1387D1FF7",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Silver_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal",
            "ID": "18C67B9A-419D-AA6D-224F-869F7E541FFF",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Marshal",
            "ID": "1AFEC971-4170-F29B-1C94-07A0EFF270AB",
            "AssetName": "Default__LeverSniperRifle_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Marshal",
            "ID": "6E4DCEBA-441B-2FC5-5992-80AB4D779922",
            "AssetName": "Default__LeverSniper_Wasteland_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 5\n(Variant 1 Blue)",
            "ID": "9F4B2FA6-4DE6-E59A-927F-EA86203824B0",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 7\n(Variant 3 Purple)",
            "ID": "9C0F0344-4582-176F-8920-3A947E968675",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 6\n(Variant 2 Red)",
            "ID": "6779FD51-4671-D13F-C3C4-7F8E7A32E107",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre",
            "ID": "DA0D77B2-49B4-148D-E32E-D79AEF1B3829",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Spectre",
            "ID": "0BF12530-4ABB-8851-0420-199AF20C2A2A",
            "AssetName": "Default__MP5_Exo_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 6\r\n(Variant 2 Blue)",
            "ID": "F55E732B-4798-2F21-C099-F7BA8FACC0BF",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 5\r\n(Variant 1 Orange)",
            "ID": "E6586300-4434-2DEE-8867-45B47980F7A5",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Orange_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre",
            "ID": "48B6E421-4F93-5A00-62B3-20A1D320B040",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 7\r\n(Variant 3 Yellow)",
            "ID": "4C67E98B-4E1F-9F53-3163-16B393849F9D",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Yellow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Spectre",
            "ID": "4CC2203E-4EE9-1DBF-FD6B-3597CC965540",
            "AssetName": "Default__MP5_Ice_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Spectre",
            "ID": "0B9BB062-41F3-5E60-91B7-EC91E0F22DBE",
            "AssetName": "Default__MP5_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Spectre",
            "ID": "93D4333A-4AAF-5B7F-8F75-BA8A6E261762",
            "AssetName": "Default__MP5_Jade_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Spectre",
            "ID": "10DA9310-479F-DF03-8229-809A69115FF3",
            "AssetName": "Default__MP5_Kingdom_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Spectre",
            "ID": "C1959560-4B63-054A-0AD1-FBA311B6B50A",
            "AssetName": "Default__MP5_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre Level 4\r\n(Variant 3 Blue)",
            "ID": "611CE1A8-421A-FF42-8142-B6A4A8F5667E",
            "AssetName": "Default__MP5_MagicSpline_Blue_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre Level 2\r\n(Variant 1 Green)",
            "ID": "EEA18B44-45A6-E88F-E7E8-2D840CFFD413",
            "AssetName": "Default__MP5_MagicSpline_Green_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre Level 3\r\n(Variant 2 Red)",
            "ID": "025673DD-4BEB-03EB-A39D-BBAE482674F1",
            "AssetName": "Default__MP5_MagicSpline_Red_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre",
            "ID": "0EB31648-47C2-7922-A944-C1904757640C",
            "AssetName": "Default__MP5_MagicSpline_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre Level 4\r\n(Variant 2 Black)",
            "ID": "22F733F9-4FB3-20F9-E032-F194D22C3D9A",
            "AssetName": "Default__MP5_Raygun_Black_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre Level 3\r\n(Variant 1 Chrome)",
            "ID": "74B5A7A2-43B5-4343-2DC8-C2801230E288",
            "AssetName": "Default__MP5_Raygun_Chrome_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre Level 5\r\n(Variant 3 RWB)",
            "ID": "4DE533BF-44D1-D8D2-9969-168E5A22D910",
            "AssetName": "Default__MP5_Raygun_RWB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre",
            "ID": "271728D3-47C2-CC82-F850-DEBAAD2F84C8",
            "AssetName": "Default__MP5_Raygun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spectre",
            "ID": "A9AACCCA-4CDC-02EA-1D7E-89BBACECC0E2",
            "AssetName": "Default__SubMachineGun_MP5_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Spectre",
            "ID": "B6A4A45D-4592-8216-21AC-C7BC26E947BA",
            "AssetName": "Default__MP5_Triangles_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Spectre",
            "ID": "967FC785-4B8E-0E3C-6232-07B20C01DC81",
            "AssetName": "Default__MP5_Wasteland_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "C78E4616-4499-7926-0F1E-93977020063F",
            "AssetName": "Default__Vector_ArtDeco_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Stinger",
            "ID": "C4C8DA8F-468B-F71B-C61E-779C2E256E92",
            "AssetName": "Default__Vector_CrimsonOps_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger",
            "ID": "0211A43E-4BE7-3430-0080-ED93C58AC3D8",
            "AssetName": "Default__Vector_Electroflux3_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger Level 2\r\n(Variant 1 Black)",
            "ID": "DC9D4105-4CF2-AA79-0535-AE961AD95571",
            "AssetName": "Default__Vector_Electroflux3_V1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger Level 3\r\n(Variant 2 Yellow)",
            "ID": "55F6B4BE-464A-E079-6AC7-94927EE403F5",
            "AssetName": "Default__Vector_Electroflux3_V2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger Level 4\r\n(Variant 3 Blue)",
            "ID": "3549AD5E-4903-AD4D-F33E-9DBEBAEAEA44",
            "AssetName": "Default__Vector_Electroflux3_V3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Stinger",
            "ID": "802491B0-4A8B-F3D9-317F-088C5B0DEDD6",
            "AssetName": "Default__Vector_LIW_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Stinger",
            "ID": "97C19875-4B44-BBC5-6578-D79C9D8B10F7",
            "AssetName": "Default__Vector_Rainbow_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Stinger",
            "ID": "62C17D02-4ADC-C1B4-612C-F2867FD4955A",
            "AssetName": "Default__Vector_Sakura_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 5\r\n(Variant 1 Gold)",
            "ID": "E72114C8-4201-1E3C-75A0-5698E6EE66E1",
            "AssetName": "Default__Vector_Sovereign_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 7\r\n(Variant 3 Purple)",
            "ID": "332D9171-4AC7-C5F0-B49D-D29AF6ED5EB7",
            "AssetName": "Default__Vector_Sovereign_Purple_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 6\r\n(Variant 2 Silver)",
            "ID": "0EA6B63D-4E9C-0FD2-46EC-9095D1C04E59",
            "AssetName": "Default__Vector_Sovereign_Silver_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger",
            "ID": "1D42A0AB-4748-674F-C181-798A1AC5C63A",
            "AssetName": "Default__Vector_Sovereign_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stinger",
            "ID": "31BB2115-4C62-D37C-43C4-11B8FEE7F212",
            "AssetName": "Default__Vector_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Stinger",
            "ID": "FF619AAE-4A06-ACAA-39A6-0C8C561952F9",
            "AssetName": "Default__Vector_Unstoppable_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Stinger Level 2\r\n(Variant 1 Red)",
            "ID": "9E275417-423D-5052-E897-C8AAA3BCD2C6",
            "AssetName": "Default__Vector_Unstoppable_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Stinger Level 3\r\n(Variant 2 Tan)",
            "ID": "B4015264-4DC8-3BE7-4B5E-64861BCCF633",
            "AssetName": "Default__Vector_Unstoppable_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Stinger Level 4\r\n(Variant 3 Pink)",
            "ID": "F2C3F510-4542-4C56-BC48-A4A2C44774A9",
            "AssetName": "Default__Vector_Unstoppable_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Knife",
            "ID": "82988B47-4439-3B28-CBBE-899D381B291E",
            "AssetName": "Default__Melee_Cosmos_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Dagger",
            "ID": "9D137AEB-41A1-A84F-3523-5194E24CC580",
            "AssetName": "Default__Melee__Cyberpunk_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Dagger",
            "ID": "D74171BF-4F3A-7DD7-76B9-04AFEAEB72C0",
            "AssetName": "Default__Melee__Dragon_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Knife",
            "ID": "A42D1C90-4FCF-B6F5-4889-41B6805C0214",
            "AssetName": "Default__Melee_Base_Edge_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Sword",
            "ID": "E276DB7C-4CAB-3215-2B83-C483B8B9139D",
            "AssetName": "Default__Melee_Exo_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Dagger",
            "ID": "7C14D797-4A40-2FBC-C314-249F6029396F",
            "AssetName": "Default__Melee_Gothic_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "D2E296D9-448E-C58F-2229-14A481906686",
            "AssetName": "Default__Melee_Base_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Knife",
            "ID": "5B4270DB-4D8B-7293-8B5C-CBB6AEA9BD22",
            "AssetName": "Default__Melee_Iridescence_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Knife",
            "ID": "138AE294-4F2E-528A-6601-A69E931BB93F",
            "AssetName": "Default__Melee__Kingdom_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Knife",
            "ID": "9C0FC8E8-4E36-86B7-8905-EE848916EA03",
            "AssetName": "Default__Melee_Lightning_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard",
            "ID": "6226D393-49D1-4A15-CB52-C8BCE5FC135A",
            "AssetName": "Default__Melee_Base_Luxury_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Dagger",
            "ID": "A31FC599-4DE8-A3CD-11FE-36BA7990832B",
            "AssetName": "Default__Melee_MagicSpline_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Energy Sword",
            "ID": "066F353C-42D9-3020-F11B-78B6EB29FDB8",
            "AssetName": "Default__Melee__Oblivion_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Claw",
            "ID": "94BF2D2A-4F1B-B68E-0DE1-F2AC152D1127",
            "AssetName": "Default__Melee__Oni_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Baton",
            "ID": "D5AA2665-4381-E982-4FD7-6AB0C2CE920B",
            "AssetName": "Default__Melee_Raygun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Knife",
            "ID": "71241F8E-4689-A110-0B22-8EAC0AA512AA",
            "AssetName": "Default__Melee_Soulstealer_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Sword",
            "ID": "3391BE35-4EAB-936C-F26D-EC810F4454C8",
            "AssetName": "Default__Melee_Base_Sovereign_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Melee",
            "ID": "CAC83E5C-47A1-3519-5420-1DB1FDBC4892",
            "AssetName": "Default__Melee_Base_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Knife",
            "ID": "9C8ED548-4AD7-6D82-9D1E-A0A57D7E2267",
            "AssetName": "Default__Melee_Unstoppable_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Knife Level 2\r\n(Variant 1 Red)",
            "ID": "6AF4123B-4266-D051-A27F-D5AB7D97E2FF",
            "AssetName": "Default__Melee_Unstoppable_v1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Knife Level 3\r\n(Variant 2 Tan)",
            "ID": "A392D2BD-46DF-7723-BB14-A58E05F33F12",
            "AssetName": "Default__Melee_Unstoppable_v2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Knife Level 4\r\n(Variant 3 Pink)",
            "ID": "4201457D-4144-BF26-55CC-FE979ED827F0",
            "AssetName": "Default__Melee_Unstoppable_v3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Skins": [
        {
            "Name": "Glitchpop Odin",
            "ID": "97AF88E4-4176-9FA3-4A26-57919443DAB7",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Odin",
            "ID": "CDA41B87-4D3A-C17C-5F6D-8990CC9C5EFB",
            "AssetName": "Default__HeavyMachineGun_Grid_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Odin",
            "ID": "9E648B20-4ED5-1F34-87A9-979CBE9A958A",
            "AssetName": "Default__HMG_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Odin",
            "ID": "65BAA0CD-42EC-F99D-54A0-338D795B5824",
            "AssetName": "Default__HMG_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Odin",
            "ID": "F454EFD1-49CB-372F-7096-D394DF615308",
            "AssetName": "Default__HeavyMachineGun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Ares",
            "ID": "8B9855F2-4CC6-0C44-3E7C-D0B2A32C6950",
            "AssetName": "Default__LightMachineGun_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Ares",
            "ID": "AC65B631-4BD1-B0FA-3313-0DA74D4EBA9D",
            "AssetName": "Default__LMG_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares",
            "ID": "E901BDEB-405F-D06C-0733-6783274D85B0",
            "AssetName": "Default__LightMachineGun_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Ares",
            "ID": "4E04647A-4CFC-64F8-4643-F6B7DBCB2943",
            "AssetName": "Default__LightMachineGun_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Ares",
            "ID": "556646C0-46DD-6986-00DF-A78D1C17F268",
            "AssetName": "Default__LMG_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ares",
            "ID": "841C9AAB-4005-F7FD-3B67-24B335100FB4",
            "AssetName": "Default__LightMachineGun_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Ares",
            "ID": "2666F98D-4F88-8CB9-4927-629D75A6A7AD",
            "AssetName": "Default__LightMachineGun_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Ares",
            "ID": "5305D9C4-4F46-FBF4-9E9A-DEA772C263B5",
            "AssetName": "Default__LightMachineGun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Vandal",
            "ID": "6191BB0B-456F-1A3E-DF13-CDB0C1B8B1E4",
            "AssetName": "Default__AK_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal",
            "ID": "18609205-4EDB-5966-CFF8-0FBA0230BA1E",
            "AssetName": "Default__AK_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Vandal",
            "ID": "F7F63B78-4B12-B21E-A0E7-6BAFBAD81509",
            "AssetName": "Default__AK_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Vandal",
            "ID": "948D31A0-4C2A-9C82-2B89-FE9F2EC65036",
            "AssetName": "Default__AK_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Vandal",
            "ID": "6F3A2A08-4F32-DBDC-8DCA-628A5C840052",
            "AssetName": "Default__AK_Grid_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal",
            "ID": "B9EE2457-481C-6776-3F5B-0CA8E8F90C89",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Vandal",
            "ID": "41B55C92-4AEB-9C86-854A-4ABCD48EA0BA",
            "AssetName": "Default__AK_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Vandal",
            "ID": "30FD16AF-4560-B2E2-7780-EE8148A0946A",
            "AssetName": "Default__AK_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Vandal",
            "ID": "72C1E90B-40CA-4304-02EB-28BB2AEA4ED2",
            "AssetName": "Default__AK_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Vandal",
            "ID": "F946EF5C-46AB-E146-A712-1D99A1651356",
            "AssetName": "Default__AK_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal",
            "ID": "30388628-42F0-606C-82C0-73AD43DE997F",
            "AssetName": "Default__AK_Soulstealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Vandal",
            "ID": "27F21D97-4C4B-BD1C-1F08-31830AB0BE84",
            "AssetName": "Default__AssaultRifle_AK_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Vandal",
            "ID": "8C22A4B2-4DA0-F2F2-9BD1-C89D106CD646",
            "AssetName": "Default__AK_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Vandal",
            "ID": "32B87592-45AD-C5A6-44AE-A9B844137C58",
            "AssetName": "Default__AK_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "C610DBC8-4A90-3C86-7F9E-BFA910F75BB9",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog",
            "ID": "285C6731-4451-B930-7A3D-C5A736D00F5E",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Bulldog",
            "ID": "23399BEB-4828-0D03-AE24-AAA62B08F796",
            "AssetName": "Default__AssaultRifle_Burst_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Bulldog",
            "ID": "199B8536-488A-09E6-8592-FF9CF21B4CEB",
            "AssetName": "Default__AssaultRifle_Burst_LIW_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Bulldog",
            "ID": "DBF7B813-4931-3B45-DB2B-EA8D418B2B1D",
            "AssetName": "Default__Burst_Polyanimals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Bulldog",
            "ID": "724A7F42-4315-ECCF-0E76-77BDD3EC2E09",
            "AssetName": "Default__AssaultRifle_Burst_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Bulldog",
            "ID": "F580899D-49C4-8BF8-9718-C9A6A38DD503",
            "AssetName": "Default__Burst_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Phantom",
            "ID": "57F91D68-4CDA-76C0-C258-7BA507CD6F87",
            "AssetName": "Default__Carbine_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom",
            "ID": "5EEC4CE6-443D-E9B5-4C5B-2B967D426BD3",
            "AssetName": "Default__AssaultRifle_ACR_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Phantom",
            "ID": "8DB507B5-4D57-96E0-000E-2D8C8AF79550",
            "AssetName": "Default__AssaultRifle_ACR_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Phantom",
            "ID": "C38DCED0-454D-D296-522E-6F8643DECD3B",
            "AssetName": "Default__AssaultRifle_ACR_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Phantom",
            "ID": "6586A7DB-4041-6A29-F37C-D6817657CAA5",
            "AssetName": "Default__AssaultRifle_ACR_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Phantom",
            "ID": "A903E567-480F-A3F9-ADB8-1DA714A2D63C",
            "AssetName": "Default__Carbine_Jade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Phantom",
            "ID": "E13AFE1E-4734-2094-FEE8-9DB016E4D54A",
            "AssetName": "Default__AssaultRifle_ACR_Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Phantom",
            "ID": "8D3EAD4A-4421-F1F2-4292-ECAC859FC135",
            "AssetName": "Default__AssaultRifle_ACR_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom",
            "ID": "13F553A1-4124-7C29-05E9-E7932FDEABB6",
            "AssetName": "Default__Carbine_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Phantom",
            "ID": "41892314-4A99-0048-1838-E38CD680EA26",
            "AssetName": "Default__AssaultRifle_ACR_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom",
            "ID": "E86BF7E4-4DD3-FBEE-533B-FA875344BBAF",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom",
            "ID": "36791B03-452D-8DAD-0091-898CC28D2196",
            "AssetName": "Default__AssaultRifle_ACR_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Phantom",
            "ID": "337CB216-4A6E-D85D-88C2-F29AB317784C",
            "AssetName": "Default__AssaultRifle_ACR_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Glitchpop Judge",
            "ID": "28A659A4-439E-FCD0-6236-D39979EE5C51",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge",
            "ID": "0221B120-444B-6D1B-FC50-E4A98E470EB2",
            "AssetName": "Default__AutomaticShotgun_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Judge",
            "ID": "F6DB3976-4C70-C3BF-01F8-DCA6D335319A",
            "AssetName": "Default__AutomaticShotgun_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Judge",
            "ID": "FBD23FDF-4D7B-8A50-AFA5-C3AD6E7266E5",
            "AssetName": "Default__AutomaticShotgun_Grid_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Judge",
            "ID": "3A1C857A-4671-0667-8EFE-EE90B8BA1E5A",
            "AssetName": "Default__AutoShotgun_Jade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Judge",
            "ID": "5324BC65-44AA-1A16-EDE4-0E9B56F35D0E",
            "AssetName": "Default__AutomaticShotgun_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Judge",
            "ID": "5237CFCA-4D83-6190-A7F9-D2BDC117EA67",
            "AssetName": "Default__AutomaticShotgun_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Judge",
            "ID": "5D217DD0-4F2C-CFCA-274E-3F8F9D518B13",
            "AssetName": "Default__AutoShotgun_Polyanimals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Judge",
            "ID": "8E27A0B3-4DC9-E2A7-E33A-29A616EFC244",
            "AssetName": "Default__AutoShotgun_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Judge",
            "ID": "ACD26127-48FF-8B9E-7BA6-B989AF8A4B24",
            "AssetName": "Default__AutomaticShotgun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Judge",
            "ID": "03751FA0-46DB-0DF3-B8CB-99ADF373ECDA",
            "AssetName": "Default__AutomaticShotgun_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Bucky",
            "ID": "1322A9A8-49AD-BC3A-2319-FB866E21334C",
            "AssetName": "Default__PumpShotgun_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky",
            "ID": "AA6162A5-4C73-1C6F-5C69-9B9082E321FD",
            "AssetName": "Default__PumpShotgun_Electroflux3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Bucky",
            "ID": "75E55415-45CE-B48B-B471-84BEF2368E33",
            "AssetName": "Default__PumpShotgun_Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Bucky",
            "ID": "2A0700DC-4181-AE19-2B49-818B24DCEACB",
            "AssetName": "Default__PumpShotgun_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky",
            "ID": "31F6F214-4379-749A-9285-04A5561E2D03",
            "AssetName": "Default__PumpShotgun_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky",
            "ID": "7DA96A2A-43CE-91C2-28F9-0C95529D133E",
            "AssetName": "Default__PumpShotgun_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky",
            "ID": "0DC9A874-41C5-E582-9A36-37946043346C",
            "AssetName": "Default__PumpShotgun_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Bucky",
            "ID": "70C97FB2-4D79-D4BB-5173-A1888CD4BFD9",
            "AssetName": "Default__PumpShotgun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "RagnaRocker Frenzy",
            "ID": "7D05D1CE-4BF2-FA96-D8F4-DCA86052E3D2",
            "AssetName": "Default__AutomaticPistol_Breach_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy",
            "ID": "5596D764-4B62-210B-59DB-7982E9D4C23F",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy",
            "ID": "4FB9EA7D-45A6-9154-7A46-648781B081C4",
            "AssetName": "Default__AutomaticPistol_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Frenzy",
            "ID": "A010C5FC-4343-067D-4DFB-EE836EC0A45F",
            "AssetName": "Default__AutomaticPistol_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Swooping Frenzy",
            "ID": "D6AF3716-4AB5-8204-A2F4-1EB4FFC51088",
            "AssetName": "Default__AutoPistol_Guide_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Frenzy",
            "ID": "08BFB08F-48CC-2699-2F5C-AABEC43DD43A",
            "AssetName": "Default__AutomaticPistol_LIW_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spitfire Frenzy",
            "ID": "5BB5ACB1-44DD-184B-484E-319188EF78EB",
            "AssetName": "Default__AutomaticPistol_Phoenix_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Frenzy",
            "ID": "531135CC-48CB-68BF-8C99-149E46670C80",
            "AssetName": "Default__AutoPistol_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Frenzy",
            "ID": "F06657F3-48B6-6314-7235-A9A2749DF5B9",
            "AssetName": "Default__AutomaticPistol_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Pistolinha Classic",
            "ID": "34919680-4F00-554B-0C2B-95ACCA7D0D36",
            "AssetName": "Default__BasePistol_Clay_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Classic",
            "ID": "41FCE834-4C76-A0F4-2CF8-CCA3AE879EAB",
            "AssetName": "Default__BasePistol_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic",
            "ID": "6CC70EAE-4297-91D5-ADB9-EFA48004DA77",
            "AssetName": "Default__BasePistol_Electroflux3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic",
            "ID": "D653F4A7-4E92-2559-0A97-2C9D46D009B3",
            "AssetName": "Default__BasePistol_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Classic",
            "ID": "6B6A219D-490A-45F1-1E5C-40BBF3DF5F28",
            "AssetName": "Default__BasePistol_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Classic",
            "ID": "E72D72AB-4284-1469-B544-478A811A29A6",
            "AssetName": "Default__BasePistol_Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Classic",
            "ID": "22FDC42D-4AD6-2BEC-8033-8A8BDF178826",
            "AssetName": "Default__BasePistol_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic",
            "ID": "750D4F04-4FEA-391B-FA8B-539815A63164",
            "AssetName": "Default__BasePistol_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Classic",
            "ID": "2F9F4637-4377-B55F-97A1-1E8974E29B27",
            "AssetName": "Default__BasePistol_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic",
            "ID": "81DDBFCD-4081-8341-FF76-AD8CDB26CE4C",
            "AssetName": "Default__BasePistol_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Classic",
            "ID": "6BA7A7A0-4057-4D5C-7C98-579F232DB298",
            "AssetName": "Default__BasePistol_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Classic",
            "ID": "24AEE897-4CDC-B0FD-E596-1BA90FA6D1B2",
            "AssetName": "Default__BasePistol_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Final Chamber Classic",
            "ID": "47D5E54A-48E5-B62A-5CF5-3CB7EFC12E90",
            "AssetName": "Default__BasePistol_Thorne_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Ghost",
            "ID": "67D3E2F7-4B73-7598-0027-63BD9E2E5FCC",
            "AssetName": "Default__LugerPistol_Grid_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hush Ghost",
            "ID": "A1D3A9E2-4F61-B1F7-3A01-CF867264D1CB",
            "AssetName": "Default__LugerPistol_Gumshoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ghost",
            "ID": "8163DB1A-4E3C-8F11-92FD-BC9E26253593",
            "AssetName": "Default__LugerPistol_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Ghost",
            "ID": "D8314B6C-45FC-FBDA-A797-569A24C11BB9",
            "AssetName": "Default__Luger_Jade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Ghost",
            "ID": "CB98B0D6-4E26-973C-C10D-A38637D04B65",
            "AssetName": "Default__Luger_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost",
            "ID": "A9890917-41EA-EB55-47E7-EE990A87FA4E",
            "AssetName": "Default__LugerPistol_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Ghost",
            "ID": "1C63B43B-43C4-04E4-01C9-7AA1BFFA5AC1",
            "AssetName": "Default__LugerPistol_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Ghost",
            "ID": "B84DF096-4096-E9C4-0869-8E83E7FC5476",
            "AssetName": "Default__Luger_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vendetta Ghost",
            "ID": "0A6EDCF0-4A64-0ED5-1B10-0E96C2EB4CB4",
            "AssetName": "Default__LugerPistol_Vampire_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Soul Silencer Ghost",
            "ID": "E24330EF-4315-512C-4588-95A601995888",
            "AssetName": "Default__LugerPistol_Wraith_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Sheriff",
            "ID": "840F12D8-467B-1A5E-F79C-B893B72B2FBC",
            "AssetName": "Default__RevolverPistol_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Sheriff",
            "ID": "55EF0FFA-44FE-03AC-DCF0-1982DF0857AA",
            "AssetName": "Default__Revolver_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff",
            "ID": "BFD9E773-4376-1F6A-98F2-DC93F0C0607C",
            "AssetName": "Default__RevolverPistol_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff",
            "ID": "2674C385-4397-0383-04DF-988D8D6FD2C8",
            "AssetName": "Default__Revolver_Electroflux3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Protektor Sheriff",
            "ID": "4F1FDE01-4130-0AE7-1320-6FB2F2FB6AB9",
            "AssetName": "Default__RevolverPistol_Hunter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff",
            "ID": "83778C03-45A3-67A2-3C89-6B8598327D58",
            "AssetName": "Default__RevolverPistol_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Sheriff",
            "ID": "54337477-4AEC-4A68-4673-7C8731639D30",
            "AssetName": "Default__Revolver_Polyanimals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Sheriff",
            "ID": "19B997BB-461A-FA85-250D-A8B0B8908FEA",
            "AssetName": "Default__RevolverPistol_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Peacekeeper Sheriff",
            "ID": "26FF0E3E-469A-CBDD-F79F-A3B89556CDEF",
            "AssetName": "Default__RevolverPistol_Sarge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff",
            "ID": "A40A6CE2-462C-C864-5D30-7B9408B98D3D",
            "AssetName": "Default__RevolverPistol_Soulstealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Sheriff",
            "ID": "1EF6BA68-4DBE-30C7-6BC8-93A6C6F13F04",
            "AssetName": "Default__RevolverPistol_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Sheriff",
            "ID": "E8FD8FC3-40CE-3ED1-235A-1C8D9654874F",
            "AssetName": "Default__RevolverPistol_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Sheriff",
            "ID": "9913DA36-48B4-F0F5-DB4E-43847A21E476",
            "AssetName": "Default__RevolverPistol_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "121BC438-4748-B2EE-2C58-768C8C26838B",
            "AssetName": "Default__RevolverPistol_Wushu_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Shorty",
            "ID": "3A921C7B-4E8F-8543-BEE8-01BA6DA86874",
            "AssetName": "Default__Slim_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Shorty",
            "ID": "1064FBD1-416C-BF00-0E30-A282A359847F",
            "AssetName": "Default__SawedOffShotgun_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wunderkind Shorty",
            "ID": "310B80D8-4E1B-B4F0-B713-9DAD458CE734",
            "AssetName": "Default__Slim_Killjoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty",
            "ID": "B36DAD11-4105-6C08-0486-17BA96D0F2A4",
            "AssetName": "Default__SawedOffShotgun_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Snakebite Shorty",
            "ID": "9428E52D-4611-C8FF-1B63-7B8E386FE8CB",
            "AssetName": "Default__SawedOffShotgun_Pandemic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Shorty",
            "ID": "48AD078A-4DAE-2B85-A945-F4B6D1EFECBB",
            "AssetName": "Default__SawedOffShotgun_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Shorty",
            "ID": "30635237-4877-4EA4-5AC4-239474D3A662",
            "AssetName": "Default__Slim_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Operator",
            "ID": "33AAA643-4BC4-4C5F-2762-228C7FC03949",
            "AssetName": "Default__BoltSniper_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator",
            "ID": "D722313D-43CB-B38D-7841-75880A3ED2CB",
            "AssetName": "Default__BoltSniper_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Operator",
            "ID": "5CED2C69-442E-D1AD-83FE-8FB8B2AC0C0F",
            "AssetName": "Default__BoltSniper_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Operator",
            "ID": "0BD5DA19-491F-DD4A-27E2-C9959B10A87A",
            "AssetName": "Default__BoltSniper_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator",
            "ID": "B2164926-4B85-852A-4BD7-D9BC27A642DA",
            "AssetName": "Default__BoltSniper_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator",
            "ID": "BBF8FFB9-49C0-75C0-CC7D-8F8F03A4BD36",
            "AssetName": "Default__BoltSniper_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator",
            "ID": "C21E2F34-4B8C-4350-33C8-A8B626ECAADC",
            "AssetName": "Default__BoltSniper_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator",
            "ID": "AECAB890-43B7-D719-06BC-9295E3D116DC",
            "AssetName": "Default__BoltSniper_Soulstealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Operator",
            "ID": "D1F2920F-469A-3431-AD96-96AFBD0017F2",
            "AssetName": "Default__BoltSniper_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Operator",
            "ID": "CCB54094-4DB8-2C9F-656B-F1BFF329F469",
            "AssetName": "Default__BoltSniper_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Guardian",
            "ID": "6141A40D-48CF-8466-6D46-558C0FF145EA",
            "AssetName": "Default__DMR_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Guardian",
            "ID": "453A734B-4F14-9183-2BE8-97B01F603368",
            "AssetName": "Default__DMR_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian",
            "ID": "2A049F35-4BCD-AF25-21FD-EC942E2D5007",
            "AssetName": "Default__DMR_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Guardian",
            "ID": "F097983D-4C5A-C7ED-C325-039C99BB824E",
            "AssetName": "Default__DMR_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian",
            "ID": "850FEA42-419F-F284-84AE-40AE1EABBB5B",
            "AssetName": "Default__DMR_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Guardian",
            "ID": "96679876-4D41-683C-2E5C-2EA25DDD8FDF",
            "AssetName": "Default__DMR_Polyanimals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian",
            "ID": "DB348DA1-49F2-0BAD-B70A-E4ADE9D31655",
            "AssetName": "Default__DMR_SoulStealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian",
            "ID": "7122D78B-4E60-EB4D-5F65-738D7C1CE9AE",
            "AssetName": "Default__DMR_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Guardian",
            "ID": "3BF1E8E0-47E8-F27A-6054-929575F41A54",
            "AssetName": "Default__DMR_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Guardian",
            "ID": "0A81818D-406E-1D8C-CE4D-9BA89DFDF1AB",
            "AssetName": "Default__DMR_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Marshal",
            "ID": "027A5D7F-4BFC-7C41-A012-24B8C6720FDA",
            "AssetName": "Default__LeverSniper_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Marshal",
            "ID": "DD58AB43-4FF3-659E-8F30-B8BD26619D4D",
            "AssetName": "Default__LeverSniper_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Marshal",
            "ID": "6F48F7FF-40A5-CC9E-1320-BDAA388F5CBF",
            "AssetName": "Default__LeverSniper_LIW_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Marshal",
            "ID": "AD6309B5-4788-D401-33D0-4DBAEEADAF87",
            "AssetName": "Default__LeverSniper_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal",
            "ID": "5211EFA8-4EFD-09BB-6CEE-72B86A8A5972",
            "AssetName": "Default__LeverSniperRifle_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Marshal",
            "ID": "FD44B2D5-49EE-77AB-FA56-588F3AC0C268",
            "AssetName": "Default__LeverSniperRifle_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Marshal",
            "ID": "19F06522-40C8-8DC6-A0CD-92808B24751F",
            "AssetName": "Default__LeverSniper_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre",
            "ID": "0EAB3E5C-4DE4-E221-34FB-2AB435C89EB6",
            "AssetName": "Default__SubMachineGun_MP5_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Spectre",
            "ID": "D405272B-4388-578C-E33B-04842496B8C1",
            "AssetName": "Default__MP5_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre",
            "ID": "20807BD8-4259-35E5-E54E-C1B214F58CC8",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Spectre",
            "ID": "A0938D46-4593-19B4-1AA5-F3B32ECB9963",
            "AssetName": "Default__MP5_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Spectre",
            "ID": "B9836020-433A-ACE4-EB35-3FBD67688C53",
            "AssetName": "Default__MP5_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Spectre",
            "ID": "4643050B-417C-0D84-3626-27B709C49C67",
            "AssetName": "Default__MP5_Jade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Spectre",
            "ID": "30B19F29-419B-1ADC-3561-40BE2B1F7841",
            "AssetName": "Default__MP5_Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Spectre",
            "ID": "3EB4D837-4AE9-B52A-B41D-2789F9974F15",
            "AssetName": "Default__MP5_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre",
            "ID": "418EF9FE-4675-6620-3755-C19ACA3FF131",
            "AssetName": "Default__MP5_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre",
            "ID": "4A8E8FF6-44F2-0EBF-6FA8-A5AF76B628EE",
            "AssetName": "Default__MP5_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Spectre",
            "ID": "F01D1307-4299-42F5-2C5E-7DAB7E69AB19",
            "AssetName": "Default__SubMachineGun_MP5_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Spectre",
            "ID": "C8A5BA23-4F0D-C7DE-8E2F-C184E2FC27BA",
            "AssetName": "Default__MP5_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Spectre",
            "ID": "F7DA43D8-450B-A03F-CEB7-C4B20F738392",
            "AssetName": "Default__MP5_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "42DA0F19-4017-5CB8-08A4-368315561FDF",
            "AssetName": "Default__Vector_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Stinger",
            "ID": "0CF70376-4150-39AA-5657-8890617BC0D1",
            "AssetName": "Default__Vector_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger",
            "ID": "0A128CB6-4BBB-F618-85CB-82BBD17BCBB1",
            "AssetName": "Default__Vector_Electroflux3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Stinger",
            "ID": "598BB272-4BFD-AE82-0242-6490CC6F721E",
            "AssetName": "Default__Vector_LIW_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Stinger",
            "ID": "9D7ED392-4C4C-B1C4-7232-3CBB07B2E133",
            "AssetName": "Default__Vector_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Stinger",
            "ID": "1CD6F578-483B-37A1-A7EF-9A907FAC416A",
            "AssetName": "Default__Vector_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger",
            "ID": "8FB27BB1-4080-581D-BCD3-53AE01861654",
            "AssetName": "Default__Vector_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Stinger",
            "ID": "940FB417-4A9C-3004-41F5-3E8F1F4178B2",
            "AssetName": "Default__Vector_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Stinger",
            "ID": "8FE5EBBC-4CE7-A248-9766-288441706E0A",
            "AssetName": "Default__Vector_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Knife",
            "ID": "A4C41553-4BA5-EFEE-5685-7A9F0CDF7878",
            "AssetName": "Default__Melee_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Dagger",
            "ID": "DDC025B2-475F-889A-2800-80B4215582BC",
            "AssetName": "Default__Melee__Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Dagger",
            "ID": "94B40026-4EFB-39EA-69D7-FCA60BE39C56",
            "AssetName": "Default__Melee__Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Knife",
            "ID": "151EE26C-4E82-E7CA-DAD1-099E7FB34774",
            "AssetName": "Default__Melee_Base_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Sword",
            "ID": "24CF2882-48C7-F287-155A-A4B6B083BAA4",
            "AssetName": "Default__Melee_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Dagger",
            "ID": "9C350EBE-458B-E6ED-AB77-2FB00CF249C1",
            "AssetName": "Default__Melee_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Axe",
            "ID": "E100DFF1-4CF5-54EC-AA65-6FADBC22973B",
            "AssetName": "Default__Melee_Base_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Knife",
            "ID": "6FA830C2-4924-87B2-1510-2FA4FBDCA1DB",
            "AssetName": "Default__Melee_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Knife",
            "ID": "F82AA022-4A6C-FA40-105D-92AF6510AE1B",
            "AssetName": "Default__Melee__Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Knife",
            "ID": "46163791-47B9-2EF0-D255-AAA5146051BB",
            "AssetName": "Default__Melee_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Knife",
            "ID": "4AF88517-4949-9CAA-9DDA-1980F07202A4",
            "AssetName": "Default__Melee_Base_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Dagger",
            "ID": "F6CFD500-4EAB-3C1D-9EEB-188E90731692",
            "AssetName": "Default__Melee_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Energy Sword",
            "ID": "46664F5B-49CA-3E09-4FE5-56BDEF536335",
            "AssetName": "Default__Melee_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Claw",
            "ID": "206FC3FE-45A0-6C19-C367-229B98B6A2AA",
            "AssetName": "Default__Melee__Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Baton",
            "ID": "0357CAF1-41A9-CB1C-C080-38AAB13D9A7E",
            "AssetName": "Default__Melee_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Knife",
            "ID": "0AECB2B8-49CC-560E-42C7-6CBCE44F05CF",
            "AssetName": "Default__Melee_Soulstealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Sword",
            "ID": "2E77AC95-4681-3D87-BBDC-93A50FF6B1F6",
            "AssetName": "Default__Melee_Base_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Melee",
            "ID": "12CC9ED2-4430-D2FE-3064-F7A19B1BA7C7",
            "AssetName": "Default__Melee_Base_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Knife",
            "ID": "C52FE5D7-4500-FFC0-CBCD-BFA29B7EA040",
            "AssetName": "Default__Melee_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "SkinLevels": [
        {
            "Name": "Glitchpop Odin",
            "ID": "549B06BB-4704-25CE-19D5-C9B70B10DE19",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin Level 2",
            "ID": "3E7D08F9-4067-1ABE-8159-87B8E31FC463",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin Level 3",
            "ID": "CA91D540-4D2D-4946-70BD-97AAE8117306",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Odin Level 4",
            "ID": "8C95559D-44FB-544D-00D7-8192ED38B17A",
            "AssetName": "Default__HeavyMachineGun_Cyberpunk_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Odin",
            "ID": "49292F21-4F5E-0A1A-3671-54B7CA8FE65A",
            "AssetName": "Default__HeavyMachineGun_Grid_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Odin",
            "ID": "C59442A5-4B74-792C-D996-71A5FB340625",
            "AssetName": "Default__HMG_Lightning_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Odin",
            "ID": "1BFEA917-4262-37BA-3A76-04B937F2D0BE",
            "AssetName": "Default__HMG_Rainbow_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Odin",
            "ID": "D91FB318-4E40-B4C9-8C0B-BB9DA28BAC55",
            "AssetName": "Default__HeavyMachineGun_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Ares",
            "ID": "A2045403-40F7-2926-F955-028B6867C79A",
            "AssetName": "Default__LightMachineGun_ArtDeco_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Ares",
            "ID": "7D3C0AC4-42CE-7111-2C86-43BE3D2E86A7",
            "AssetName": "Default__LMG_Cosmos_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares",
            "ID": "642EE168-4F9E-1F5F-BE72-01B3A41AC086",
            "AssetName": "Default__LightMachineGun_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 2",
            "ID": "485DF72F-423E-4E53-51A2-68A3C2A929DB",
            "AssetName": "Default__LightMachineGun_Edge_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 3",
            "ID": "B080BE2C-457A-61A2-D3B2-429B32E62345",
            "AssetName": "Default__LightMachineGun_Edge_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Ares Level 4",
            "ID": "6B12682C-4813-D34F-322D-67B0211E1E6D",
            "AssetName": "Default__LMG_Edge_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Ares",
            "ID": "BAD7AE62-4F6A-8974-AB73-7BA6405CA898",
            "AssetName": "Default__LightMachineGun_Electroflux_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Ares",
            "ID": "65BB772A-41F2-8B25-A1AF-75A79D596203",
            "AssetName": "Default__LMG_Exo_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ares",
            "ID": "29BE6D9E-48B2-1229-4F7D-4DA1C20DEDA9",
            "AssetName": "Default__LightMachineGun_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Ares",
            "ID": "9FBE39C6-42D7-B1DB-9048-F0951CE2FF94",
            "AssetName": "Default__LightMachineGun_Sakura_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ares",
            "ID": "0F5F60F4-4C94-E4B2-CEAB-E2B4E8B41784",
            "AssetName": "Default__LightMachineGun_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Vandal",
            "ID": "9FF1A0E6-4F74-0E6D-9117-DE8683DB4EB5",
            "AssetName": "Default__AK_ArtDeco_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal",
            "ID": "B3D3FF38-4202-20D8-2F41-C783477E5636",
            "AssetName": "Default__AK_Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 2",
            "ID": "D86E4684-47D3-9A2F-9BD4-01AE3FD3E183",
            "AssetName": "Default__AK_Dragon_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 3",
            "ID": "77569F90-4E7F-7D91-BD18-2AA12BDBA709",
            "AssetName": "Default__AK_Dragon_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Vandal Level 4",
            "ID": "4FB025DB-471F-3891-6E30-B98866ABB2F9",
            "AssetName": "Default__AK_Dragon_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Vandal",
            "ID": "7383CA56-490A-F9F5-F126-5EA0DCD4A242",
            "AssetName": "Default__AK_Exo_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Vandal",
            "ID": "3D1BC8E8-4759-148C-7775-5A96E8C975FD",
            "AssetName": "Default__AK_GothicLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Vandal",
            "ID": "C9EE9A00-453D-A358-8501-3EBB7CA3765E",
            "AssetName": "Default__AK_Grid_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal",
            "ID": "C9678D8C-4327-F397-B0EC-DCA3C3D6FB15",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 2",
            "ID": "C6F9C7EF-4A35-FA14-C9ED-BD80E37BE826",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 3",
            "ID": "FC332008-475F-5555-0155-4CB3BCE714FF",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Vandal Level 4",
            "ID": "22821A32-4E04-AD4A-1893-95904C08B264",
            "AssetName": "Default__AssaultRifle_AK_HypeBeast_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Vandal",
            "ID": "FBFC273B-4C12-961A-A4FB-978B43BE81A9",
            "AssetName": "Default__AK_Ice_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Vandal",
            "ID": "1878BBC9-409E-66B4-346B-C3997A54DF57",
            "AssetName": "Default__AK_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Vandal",
            "ID": "F4BFFF96-487A-CF9E-08CC-D590D962C4E6",
            "AssetName": "Default__AK_Rainbow_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Vandal",
            "ID": "3AEEF60B-48FB-02AA-31B1-068AEB351213",
            "AssetName": "Default__AK_Sakura_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal",
            "ID": "BA42FE63-457A-78CE-4499-47950A698129",
            "AssetName": "Default__AK_Soulstealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 2",
            "ID": "6F9BA692-4618-D0E6-3099-42B4DC5FCE89",
            "AssetName": "Default__AK_Soulstealer_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 3",
            "ID": "98597B95-451C-70CF-46FB-31B4C5A54394",
            "AssetName": "Default__AK_Soulstealer_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Vandal Level 4",
            "ID": "8C282914-446A-3E99-095A-CD97DF201C8B",
            "AssetName": "Default__AK_Soulstealer_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vandal",
            "ID": "1AB72E66-4DA3-33A0-164F-908113E075A4",
            "AssetName": "Default__AssaultRifle_AK_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Vandal",
            "ID": "94CF6DD4-42C5-F70E-1652-DCA05FA42AD6",
            "AssetName": "Default__AK_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Vandal",
            "ID": "A6D41F01-4B8B-444D-B9DA-3EAAF3D7E262",
            "AssetName": "Default__AK_Wasteland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "3BF9D39F-46B4-BA23-E079-488D799B9416",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog",
            "ID": "4A5AD8CD-4684-A47C-B393-CE9C6760D21A",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 2",
            "ID": "44C5B5CC-4931-B4AF-1A4A-17AB9EC2B89E",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 3",
            "ID": "49EA5740-4731-01C5-A68E-CBA6B86B1049",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Bulldog Level 4",
            "ID": "D83D2283-4C50-EE72-3A8B-51B6A05AED15",
            "AssetName": "Default__AssaultRifle_Burst_Cyberpunk_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Bulldog",
            "ID": "8E032580-414F-7AB4-7EFB-F6AC7D2BC2F1",
            "AssetName": "Default__AssaultRifle_Burst_Electroflux_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Bulldog",
            "ID": "49FC11B3-40A9-29FF-A701-63A6F59E2A0F",
            "AssetName": "Default__AssaultRifle_Burst_LIWLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Bulldog",
            "ID": "0FCE64BD-42C9-1755-8C67-E3A8CDD49DE7",
            "AssetName": "Default__Burst_Polyanimals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bulldog",
            "ID": "C8E6AC70-48EF-9D96-D964-A88E8890B885",
            "AssetName": "Default__AssaultRifle_Burst_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Bulldog",
            "ID": "84F8D0F4-4442-5892-6A20-8F83E65A5E96",
            "AssetName": "Default__Burst_Triangles_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Phantom",
            "ID": "40308B30-4689-9713-52FB-6F8A3534213F",
            "AssetName": "Default__Carbine_Cosmos_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom",
            "ID": "0FF7FF25-42CF-769A-4E6D-BD833121302D",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 2",
            "ID": "48E976CC-4BE8-87C6-2848-DD87BBC0ACF8",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 3",
            "ID": "5791FE6E-4C59-B6EF-A7D4-05B0D7C9AED4",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Phantom Level 4",
            "ID": "9E2DF910-4927-7313-E6B9-639454EF0E91",
            "AssetName": "Default__AssaultRifle_ACR_Edge_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Phantom",
            "ID": "D39A4263-49D3-F2E0-2C13-C299F8644518",
            "AssetName": "Default__AssaultRifle_ACR_Electroflux_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Phantom",
            "ID": "66F68F67-4F5E-8188-8BA8-B183E25E93E7",
            "AssetName": "Default__AssaultRifle_ACR_IceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Phantom",
            "ID": "4845A7AB-4120-AE1C-AEC1-9E915A7424B1",
            "AssetName": "Default__AssaultRifle_ACR_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Phantom",
            "ID": "645FDAE1-4056-E40C-B8E4-A08AEA0DFE2F",
            "AssetName": "Default__Carbine_Jade_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Phantom",
            "ID": "A7229CBA-4691-62B0-9C40-F59A29817DDC",
            "AssetName": "Default__AssaultRifle_ACR_KingdomLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Phantom",
            "ID": "19B20B51-472B-E837-E5DA-F8A348110DBF",
            "AssetName": "Default__Carbine_Lightning_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Phantom",
            "ID": "04DBF8E5-44FC-73F7-0655-8CA05A47739C",
            "AssetName": "Default__Carbine_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Phantom",
            "ID": "F38B2545-4498-48B3-150E-1589E25E7AA7",
            "AssetName": "Default__AssaultRifle_ACR_Murals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom",
            "ID": "B8BB264C-4578-2410-8DFA-6AACFEB318B0",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom Level 2",
            "ID": "D8168629-4E42-1359-4401-FFBB79F59866",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom Level 3",
            "ID": "1B251E84-47F3-738D-C686-6CB718E66C71",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Phantom Level 4",
            "ID": "F97AA61F-4119-F21A-621D-589FE5E55B01",
            "AssetName": "Default__AssaultRifle_ACR_Oblivion_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom",
            "ID": "C00E786E-4E6F-0EF7-0CE3-32BA9918BA41",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 2",
            "ID": "2C4E829A-4915-E9D8-5C6F-43A39D60AFC0",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 3",
            "ID": "BB07581B-4733-CE33-53D4-3DADC038CA4A",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Phantom Level 4",
            "ID": "1B24255D-4F50-9202-7B6F-F7873DB580D1",
            "AssetName": "Default__AssaultRifle_ACR_Oni_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phantom",
            "ID": "871E73ED-452D-EB5A-3D6B-1D87060F35CE",
            "AssetName": "Default__AssaultRifle_ACR_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Glitchpop Judge",
            "ID": "712C7A37-4524-0B27-DFDD-4E95181DD36E",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge Level 2",
            "ID": "C9480C4D-4005-8CD9-E1A2-18BED7F2E801",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge Level 3",
            "ID": "6F48190C-403C-3A92-1A89-F983FA9281DB",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Judge Level 4",
            "ID": "C60C98E3-41DE-ED9C-FB92-AA9C6E0BC7A0",
            "AssetName": "Default__AutomaticShotgun_Cyberpunk_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge",
            "ID": "D8C9FEE3-4E02-BC92-A235-608A556905AE",
            "AssetName": "Default__AutomaticShotgun_Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 2",
            "ID": "640764D8-495D-3663-27AB-B99F5F2466D6",
            "AssetName": "Default__AutomaticShotgun_Dragon_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 3",
            "ID": "D95E4B3C-4081-4005-CAE7-14B890046B4F",
            "AssetName": "Default__AutomaticShotgun_Dragon_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Judge Level 4",
            "ID": "D41A4383-4C15-4C3F-1F16-4FBB4FB36ED8",
            "AssetName": "Default__AutomaticShotgun_Dragon_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Judge",
            "ID": "33D3C906-4305-19CF-8770-1EB5207482CC",
            "AssetName": "Default__AutomaticShotgun_Electroflux_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Judge",
            "ID": "F8CD4279-4530-DB62-1E4E-AA82C129B045",
            "AssetName": "Default__AutomaticShotgun_Grid_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Judge",
            "ID": "4AFDC818-4665-1582-6319-8081AA64E550",
            "AssetName": "Default__AutoShotgun_Jade_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Judge",
            "ID": "1B94D997-4DB6-014F-4CB8-C1B4DF7D7EBC",
            "AssetName": "Default__AutomaticShotgun_Lightning_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Judge",
            "ID": "CFEB4B7A-4310-796C-DB4E-FB9844823992",
            "AssetName": "Default__AutomaticShotgun_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Judge",
            "ID": "3C23FDC3-4300-EC78-5123-BCB0DC456473",
            "AssetName": "Default__AutoShotgun_Polyanimals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Judge",
            "ID": "65ED014B-4279-8BA5-01D3-F48D4E7F115C",
            "AssetName": "Default__AutoShotgun_Rainbow_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Judge",
            "ID": "6942D8D1-4370-A144-2140-22A6D2BE2697",
            "AssetName": "Default__AutomaticShotgun_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Judge",
            "ID": "73E91435-4A2A-2552-D541-EB961E168F2C",
            "AssetName": "Default__AutomaticShotgun_Triangles_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Bucky",
            "ID": "633521C9-42AE-D2BE-78C1-A09B25AF7D10",
            "AssetName": "Default__Pumpshotgun_CrimsonOps_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Bucky",
            "ID": "1E7BE2E9-418E-7F39-D879-A8912BE1D3AB",
            "AssetName": "Default__PumpShotgun_Electroflux3_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Bucky",
            "ID": "4CAA7FB0-4751-52F3-6EED-6AB6232BE131",
            "AssetName": "Default__PumpShotgun_KingdomLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Bucky",
            "ID": "03E03718-4C65-8A47-FB8B-78BA233CECD1",
            "AssetName": "Default__PumpShotgun_Murals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky",
            "ID": "F00520C8-4B70-7255-D23C-C0A4887656A2",
            "AssetName": "Default__PumpShotgun_OblivionLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky Level 2",
            "ID": "D8F0CAD0-40A3-75A4-389B-5D8E91E9E157",
            "AssetName": "Default__PumpShotgun_OblivionLv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky Level 3",
            "ID": "B1A6A3D0-4C31-266E-0D66-5A960D452220",
            "AssetName": "Default__PumpShotgun_OblivionLv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Bucky Level 4",
            "ID": "18039610-4134-95F2-0791-E18A2E9F30DD",
            "AssetName": "Default__PumpShotgun_OblivionLv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky",
            "ID": "CDC130C2-4B12-3702-C8F6-5A8920746395",
            "AssetName": "Default__PumpShotgun_Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 2",
            "ID": "8F1DBCE8-4012-72A8-1E4F-D4B50CFC5BB8",
            "AssetName": "Default__PumpShotgun_Oni_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 3",
            "ID": "B5E520A1-43A6-C144-E70D-918D90F05233",
            "AssetName": "Default__PumpShotgun_Oni_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Bucky Level 4",
            "ID": "AF478F2A-4DAE-43D3-1545-7D96A65C60B1",
            "AssetName": "Default__PumpShotgun_Oni_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky",
            "ID": "22C0AAA3-4919-5A7B-90C0-2DACAFDC32FE",
            "AssetName": "Default__PumpShotgun_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Bucky Level 2",
            "ID": "C91875E5-48A9-0820-6B65-ABA73BF3479D",
            "AssetName": "Default__PumpShotgun_Raygun_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bucky",
            "ID": "2F5078C7-4381-492D-CC00-9F96966BA1EC",
            "AssetName": "Default__PumpShotgun_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "RagnaRocker Frenzy",
            "ID": "B02520DD-48CD-466C-977D-529DC6A1D6F5",
            "AssetName": "Default__AutomaticPistol_Breach_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy",
            "ID": "4B74B3EE-4A63-7339-A28F-8B8BE010CA5A",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 2",
            "ID": "EDDC294E-45F1-026E-1362-70B4E1F1F03A",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 3",
            "ID": "D89C07D2-4EAB-3776-FA3E-D6ABB0E18188",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Frenzy Level 4",
            "ID": "71AF2FC6-4A39-7C34-158F-ABBD0EEB97E5",
            "AssetName": "Default__AutomaticPistol_Cyberpunk_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy",
            "ID": "EA65BA94-468D-39A8-5DED-98820D72D19F",
            "AssetName": "Default__AutomaticPistol_Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 2",
            "ID": "63307028-4680-BBF3-A69F-7FAAD8113A49",
            "AssetName": "Default__AutomaticPistol_Dragon_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 3",
            "ID": "B86EA344-404D-DE22-92C8-1B89C455C47D",
            "AssetName": "Default__AutomaticPistol_Dragon_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Frenzy Level 4",
            "ID": "F70DC825-4BE6-0074-0526-758B3F183152",
            "AssetName": "Default__AutomaticPistol_Dragon_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush Frenzy",
            "ID": "3E32C58E-4347-E4B1-4502-6DAB0DC516A8",
            "AssetName": "Default__AutomaticPistol_Electroflux_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Swooping Frenzy",
            "ID": "2F911F78-46E4-102A-F677-37A069C3A4DC",
            "AssetName": "Default__AutoPistol_Guide_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Frenzy",
            "ID": "9D333FF1-47E2-04C7-2A26-688C08E9164D",
            "AssetName": "Default__AutomaticPistol_LIWLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spitfire Frenzy",
            "ID": "468505E6-46E2-AF29-3974-5FBBE6BF212F",
            "AssetName": "Default__AutomaticPistol_Phoenix_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Frenzy",
            "ID": "5A773352-456E-EF0B-35AB-C99EAD159264",
            "AssetName": "Default__AutoPistol_Rainbow_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Frenzy",
            "ID": "80FABD74-4438-A2DD-0C39-42AB449F9EC6",
            "AssetName": "Default__AutomaticPistol_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Pistolinha Classic",
            "ID": "C2E41149-4F8B-E191-A0AE-5A94B80044F5",
            "AssetName": "Default__BasePistol_ClayLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Classic",
            "ID": "D2B8B79B-4BE7-4790-A356-4E9B06D3965E",
            "AssetName": "Default__BasePistol_CrimsonOps_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Classic",
            "ID": "29A5ECC2-4F93-068A-130A-B5A8A113FEC9",
            "AssetName": "Default__BasePistol_Electroflux3_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic",
            "ID": "C7695CE7-4FC9-1C79-64B3-8C8F9E21571C",
            "AssetName": "Default__BasePistol_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 2",
            "ID": "7B2C1232-460B-AB9A-1ECA-55B5AEE9AD08",
            "AssetName": "Default__BasePistol_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 3",
            "ID": "4FC58223-43E7-A868-A6DF-5E93BE31369C",
            "AssetName": "Default__BasePistol_HypeBeast_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Classic Level 4",
            "ID": "E8A35DDB-4CE7-3867-154C-94803ED12A24",
            "AssetName": "Default__BasePistol_HypeBeast_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Classic",
            "ID": "3800390C-4192-92D1-1703-33BA231FC226",
            "AssetName": "Default__BasePistol_IceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Classic",
            "ID": "6AB90B28-49F1-9E1B-5083-2DA2DE61E109",
            "AssetName": "Default__BasePistol_Kingdom_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Classic",
            "ID": "EB35E4E1-4138-9ECE-08E2-69BD414CF598",
            "AssetName": "Default__BasePistol_Lightning_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Classic",
            "ID": "1B300B91-41BB-D468-F65F-F68EC0861BD6",
            "AssetName": "Default__BasePistol_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Classic",
            "ID": "B8BC5D1B-44AA-AA83-0246-B1A6BB496177",
            "AssetName": "Default__BasePistol_Murals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic",
            "ID": "F35F6E13-4B7B-DA38-C0DE-5C91FFFD584B",
            "AssetName": "Default__BasePistol_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Classic Level 2",
            "ID": "6958FBF5-4708-F97E-92E1-C7ABDF6724B1",
            "AssetName": "Default__BasePistol_Raygun_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Classic",
            "ID": "DF639108-4E9D-7FC1-51DA-4DBB810BA011",
            "AssetName": "Default__BasePistol_Sakura_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Classic",
            "ID": "51CBCCAD-487C-50ED-2FFD-C88B4240FAB3",
            "AssetName": "Default__BasePistol_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Final Chamber Classic",
            "ID": "BBBE4B32-457C-E4FB-A674-1D9C3885D331",
            "AssetName": "Default__BasePistol_Thorne_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "dot EXE Ghost",
            "ID": "9466088A-4AD8-CB08-EC9A-45AABA3A6ACD",
            "AssetName": "Default__LugerPistol_GridLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hush Ghost",
            "ID": "AFCB2528-4415-0178-98B1-C0A751092762",
            "AssetName": "Default__LugerPistol_Gumshoe_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Ghost",
            "ID": "5546F723-4056-6700-80B8-F1B8D42E4952",
            "AssetName": "Default__LugerPistol_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Ghost",
            "ID": "DE822D80-4E91-943D-3DD5-429513E7D177",
            "AssetName": "Default__Luger_Jade_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Ghost",
            "ID": "68564C51-4F7E-67D1-FD0D-4E9D216356E8",
            "AssetName": "Default__Luger_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost",
            "ID": "ED8A1109-4E48-F077-636B-E98DD332BFCC",
            "AssetName": "Default__LugerPistol_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 2",
            "ID": "94B4E0F7-454D-0E5B-9F32-4D9FD399D8A2",
            "AssetName": "Default__LugerPistol_Sovereign_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 3",
            "ID": "5AA0593C-40FC-B9C4-9232-7F91F75B9FBD",
            "AssetName": "Default__LugerPistol_Sovereign_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Ghost Level 4",
            "ID": "D5E747DA-4D41-28E2-68B2-C5B41584F7CB",
            "AssetName": "Default__LugerPistol_Sovereign_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ghost",
            "ID": "0A7E786C-444E-6A80-8BDA-E2B714D68332",
            "AssetName": "Default__LugerPistol_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Ghost",
            "ID": "F9FAB42C-46BF-1BF0-DBA5-32988BE03FC2",
            "AssetName": "Default__Luger_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vendetta Ghost",
            "ID": "4526A891-4754-DA6C-7ADA-95A8A259952E",
            "AssetName": "Default__LugerPistol_VampireLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Soul Silencer Ghost",
            "ID": "B85B3760-43BB-507D-323E-1682FA76D96B",
            "AssetName": "Default__LugerPistol_Wraith_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Sheriff",
            "ID": "6D4766D0-41F0-8493-93EB-A4902A0C6034",
            "AssetName": "Default__RevolverPistol_ArtDecoLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Sheriff",
            "ID": "353C1E5F-4258-C49A-C0D6-319AD33BFFEA",
            "AssetName": "Default__Revolver_Cosmos_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff",
            "ID": "4276D2B5-4B1C-B636-AFF0-4EA579D875D7",
            "AssetName": "Default__RevolverPistol_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 2",
            "ID": "4A585DF0-4BC4-17AA-1E5A-CCAC42B07D12",
            "AssetName": "Default__RevolverPistol_Edge_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 3",
            "ID": "F73B2921-4F40-918E-08EB-45ABD9CE2B3C",
            "AssetName": "Default__RevolverPistol_Edge_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Sheriff Level 4",
            "ID": "65C2C8D3-4473-4F74-305C-FF90FBF318E8",
            "AssetName": "Default__RevolverPistol_Edge_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Sheriff",
            "ID": "DB36EE86-4AA7-249F-6745-5E9DDFFA50B4",
            "AssetName": "Default__Revolver_Electroflux3_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Protektor Sheriff",
            "ID": "D9FC55C6-4B92-98AC-5052-2A8B5CA4FB71",
            "AssetName": "Default__RevolverPistol_Hunter_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff",
            "ID": "2B555F97-46BB-5949-3531-979F5BC817F0",
            "AssetName": "Default__RevolverPistol_OblivionLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff Level 2",
            "ID": "A60421B9-4B86-CCD3-CA08-808EF4CF112B",
            "AssetName": "Default__RevolverPistol_OblivionLv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff Level 3",
            "ID": "1AD8E7B3-4547-0890-AA8D-D79BE028E48F",
            "AssetName": "Default__RevolverPistol_OblivionLv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Sheriff Level 4",
            "ID": "BECD58D6-4DA0-DB56-A748-35923D2750E1",
            "AssetName": "Default__RevolverPistol_OblivionLv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Sheriff",
            "ID": "02F45C84-427C-D575-945F-BA913A732B72",
            "AssetName": "Default__Revolver_Polyanimals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Sheriff",
            "ID": "C8652EFA-462F-D455-20B0-699DD00A9E2A",
            "AssetName": "Default__RevolverPistol_SakuraLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Peacekeeper Sheriff",
            "ID": "EC570F46-4751-EEB6-7739-069BCBB8D05A",
            "AssetName": "Default__RevolverPistol_Sarge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff",
            "ID": "4E4EBB8D-41D0-C326-595A-1F9B257E91FA",
            "AssetName": "Default__RevolverPistol_Soulstealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 2",
            "ID": "AB5C63FC-46C0-8C7D-1D67-0DA96D4B8CF7",
            "AssetName": "Default__RevolverPistol_Soulstealer_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 3",
            "ID": "EF84244D-4F04-01DD-36BA-C7B97A688754",
            "AssetName": "Default__RevolverPistol_Soulstealer_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Sheriff Level 4",
            "ID": "A47A0D1B-4405-9DE7-6011-68A9A4A1F36D",
            "AssetName": "Default__RevolverPistol_Soulstealer_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sheriff",
            "ID": "FEAF05A1-492F-D154-A9F5-0EB1FE9A603E",
            "AssetName": "Default__RevolverPistol_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Sheriff",
            "ID": "4538BFF7-470C-889C-9875-7BA3EBF87C87",
            "AssetName": "Default__RevolverPistol_Triangles_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Sheriff",
            "ID": "0D73596B-478A-DAE0-49CA-2FA588F78F13",
            "AssetName": "Default__RevolverPistol_Wasteland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "443F5A29-4D5E-D63E-A3C6-ADA7713172FA",
            "AssetName": "Default__RevolverPistol_Wushu_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Shorty",
            "ID": "D0A95805-4ADB-95F7-3955-339D89769BEC",
            "AssetName": "Default__Slim_Exo_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Shorty",
            "ID": "907BAB1F-4FCA-982E-7645-41A941EF6626",
            "AssetName": "Default__Slim_Gothic_Lv1_PrimaryAsset1_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wunderkind Shorty",
            "ID": "F9688E62-42C5-9F10-F160-49ABAEE2E02C",
            "AssetName": "Default__Slim_Killjoy_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty",
            "ID": "A2950772-447A-F2DB-BE24-19B0E0ED736F",
            "AssetName": "Default__SawedOffShotgun_Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 2",
            "ID": "75A66462-49D7-134A-03E1-BC8C3B7FDA7A",
            "AssetName": "Default__SawedOffShotgun_Oni_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 3",
            "ID": "02461D7F-4F0A-F25F-94B2-EE960D0734D7",
            "AssetName": "Default__SawedOffShotgun_Oni_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Shorty Level 4",
            "ID": "25E2A599-4564-708A-B80E-AFBEB6781372",
            "AssetName": "Default__SawedOffShotgun_Oni_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Snakebite Shorty",
            "ID": "6F90D1ED-4ACC-D925-4A8A-60913F14D16B",
            "AssetName": "Default__SawedOffShotgun_Pandemic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Shorty",
            "ID": "A7F92A1C-4465-5EA3-7745-BD876117F4A7",
            "AssetName": "Default__SawedOffShotgun_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Shorty",
            "ID": "A88A4C80-4913-A111-0FBA-878ADDDD381A",
            "AssetName": "Default__Slim_Wasteland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Operator",
            "ID": "FC4C9003-4069-D351-E0B5-03B509638C2C",
            "AssetName": "Default__BoltSniper_CrimsonOps_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator",
            "ID": "5C273D0E-47FA-BB8C-D914-728DE95DA30E",
            "AssetName": "Default__BoltSniper_Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 2",
            "ID": "EA7094B7-4F29-2570-0003-14A9B872FC19",
            "AssetName": "Default__BoltSniper_Dragon_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 3",
            "ID": "02567ECE-47A2-A68B-7853-668F45AB0AB0",
            "AssetName": "Default__BoltSniper_Dragon_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Operator Level 4",
            "ID": "41AD7696-47BF-CD88-115B-9CB17AD77919",
            "AssetName": "Default__BoltSniper_Dragon_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Operator",
            "ID": "37851A69-4719-D8AE-D305-49BCEE8D853C",
            "AssetName": "Default__BoltSniper_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Operator",
            "ID": "E5A2E04A-4805-1244-5376-06B40D7C6CBB",
            "AssetName": "Default__BoltSniper_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Operator",
            "ID": "4C053776-467F-2C6A-B609-0BA3EA371A14",
            "AssetName": "Default__BoltSniper_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator",
            "ID": "24C73C29-443C-2440-D6DB-838086F2451A",
            "AssetName": "Default__BoltSniper_OblivionLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator Level 2",
            "ID": "8A0328E1-4067-DDAA-FB06-E6AB0C0C9A54",
            "AssetName": "Default__BoltSniper_OblivionLv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator Level 3",
            "ID": "65888FCA-4A1D-DA64-8735-8495D86338CA",
            "AssetName": "Default__BoltSniper_OblivionLv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Operator Level 4",
            "ID": "4FFC2AE6-4501-2C43-A105-F4977A0A207E",
            "AssetName": "Default__BoltSniper_OblivionLv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator",
            "ID": "4AA31563-44E1-0D9F-F95A-A1B9965AD762",
            "AssetName": "Default__BoltSniper_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Operator Level 2",
            "ID": "D3B07995-4AB5-7593-F3FF-B6AD7E8599D0",
            "AssetName": "Default__BoltSniper_Raygun_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator",
            "ID": "7BFAB387-4E97-D815-4488-C491E3A5520C",
            "AssetName": "Default__BoltSniper_Soulstealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 2",
            "ID": "BF02E33F-4D16-E361-D1ED-1EB58DE846C3",
            "AssetName": "Default__BoltSniper_Soulstealer_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 3",
            "ID": "59409CB0-4583-20A4-C905-4DB393712AF7",
            "AssetName": "Default__BoltSniper_Soulstealer_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Operator Level 4",
            "ID": "21305A72-4374-67C7-C25B-E0BB8DC2DA52",
            "AssetName": "Default__BoltSniper_Soulstealer_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Operator",
            "ID": "88CBA358-4F4D-4D0E-69FC-B48F4C65CB2D",
            "AssetName": "Default__BoltSniper_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Operator",
            "ID": "ED333B00-4E88-A9C5-D309-ACAE85438E93",
            "AssetName": "Default__BoltSniper_Triangles_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Guardian",
            "ID": "BF6DF430-4E46-5C51-DF6F-C2BC3B1CB4FE",
            "AssetName": "Default__DMR_CosmosLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Guardian",
            "ID": "C41A7B5D-4A04-A411-053D-818FE1D77AC6",
            "AssetName": "Default__DMR_Gothic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian",
            "ID": "9336AB9D-445C-0872-A283-9F9B61A0098A",
            "AssetName": "Default__DMR_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 2",
            "ID": "EDC646B0-4A5A-6A76-A860-6B8DB95BD132",
            "AssetName": "Default__DMR_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 3",
            "ID": "14B04B38-4359-62A3-AB62-BCBE715E3FA0",
            "AssetName": "Default__DMR_HypeBeast_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Guardian Level 4",
            "ID": "99B7B761-41B3-E26C-CEEB-B9A1C3A67736",
            "AssetName": "Default__DMR_HypeBeast_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Guardian",
            "ID": "7A0374AF-42F5-2F99-B535-A997F2179717",
            "AssetName": "Default__DMR_Murals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian",
            "ID": "FEE2C305-40D1-1CCA-08B8-46BCEDA98ECA",
            "AssetName": "Default__DMR_Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 2",
            "ID": "10DB658A-4299-A0CD-8822-FEB09ADCA3AD",
            "AssetName": "Default__DMR_Oni_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 3",
            "ID": "FEA4C5E9-4028-72B1-0DDA-00B9D14026A2",
            "AssetName": "Default__DMR_Oni_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Guardian Level 4",
            "ID": "9318A2C8-4CCC-BFB4-E7D9-6289608A4BA5",
            "AssetName": "Default__DMR_Oni_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Guardian",
            "ID": "DF9044E9-4ED4-4A49-B7CE-BABC4A0E23D6",
            "AssetName": "Default__DMR_Polyanimals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian",
            "ID": "C9F0EA7F-4BED-B10E-62D2-0394444FEED1",
            "AssetName": "Default__DMR_SoulStealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 2",
            "ID": "AD0E9E83-4658-0A02-A912-21B41DF87C38",
            "AssetName": "Default__DMR_SoulStealer_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 3",
            "ID": "09FAF945-4BE6-EE7F-43D5-9FAE75E182EC",
            "AssetName": "Default__DMR_SoulStealer_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Guardian Level 4",
            "ID": "4E1B9E7D-4CFC-9A14-4FE1-EA9185CDB6D9",
            "AssetName": "Default__DMR_SoulStealer_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian",
            "ID": "8F8F82F4-4133-82C9-50B2-3C9C67E0F9FB",
            "AssetName": "Default__DMR_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 2",
            "ID": "32CF9B7A-4EA1-64F4-1405-32A2EE614BC8",
            "AssetName": "Default__DMR_Sovereign_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 3",
            "ID": "62F258E7-4821-4925-29B3-3CA90972991F",
            "AssetName": "Default__DMR_Sovereign_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Guardian Level 4",
            "ID": "04C6A2A4-400A-B0DF-B482-658C59529EE6",
            "AssetName": "Default__DMR_Sovereign_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Guardian",
            "ID": "414D888A-41CE-FCF0-E545-C49018EC9CF4",
            "AssetName": "Default__DMR_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Guardian",
            "ID": "FA3D6A11-46C4-2CAF-F7E4-10A5013C034B",
            "AssetName": "Default__DMR_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Marshal",
            "ID": "60DC909F-4C52-B96E-DD37-DFAA2392E373",
            "AssetName": "Default__LeverSniper_Gothic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Marshal",
            "ID": "4A3B4AAF-4CDD-D5CF-B776-0593C3D2BF9A",
            "AssetName": "Default__LeverSniper_IceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Marshal",
            "ID": "115AD37D-4126-20E5-35A5-D691AA97A03C",
            "AssetName": "Default__LeverSniper_LIW_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria Marshal",
            "ID": "50265AD5-4F14-2B32-924E-02BBED2BEA6F",
            "AssetName": "Default__LeverSniper_Murals_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal",
            "ID": "C5DD6298-4928-5D64-5CD0-7FA41EA89D81",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 2",
            "ID": "5DFC0AF6-4C03-03B0-7066-6EA1770FE6C0",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 3",
            "ID": "003665B4-4FF3-881B-5C67-3EBD454D4FAB",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Marshal Level 4",
            "ID": "DD1FEE10-42CA-1201-5BF8-399A16B25620",
            "AssetName": "Default__LeverSniperRifle_Sovereign_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Marshal",
            "ID": "F0389390-49EB-A43E-27FA-FC9F9F8AA9DE",
            "AssetName": "Default__LeverSniperRifle_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Wasteland Marshal",
            "ID": "4049DC82-495B-CECC-8E34-4DBF35753129",
            "AssetName": "Default__LeverSniper_Wasteland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre",
            "ID": "3B955119-421C-3319-50CC-1AAF06B42338",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 2",
            "ID": "53068012-45A5-232E-0BD7-D5AA786C0347",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 3",
            "ID": "D9C7F033-42E9-57C8-7E94-DD9294018E44",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spectre Level 4",
            "ID": "CCBA3803-510B-4AF4-A2BD-F530D8725FD1",
            "AssetName": "Default__SubMachineGun_MP5_Edge_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Spectre",
            "ID": "4D02D9FA-4CB4-4D87-BDF0-97BD5F960C12",
            "AssetName": "Default__MP5_Exo_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre",
            "ID": "D1D528AE-4DCC-E693-68E2-E8A475DF83A4",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 2",
            "ID": "D5B3F1DE-413C-3B6B-1101-128D408647BF",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 3",
            "ID": "3546DC11-40FE-0CA9-2989-CD80FC53ECCC",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Spectre Level 4",
            "ID": "FEFC628B-4078-C57B-DCC7-3591ECA5C4D0",
            "AssetName": "Default__SubMachineGun_MP5_HypeBeast_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche Spectre",
            "ID": "5A0CD3B5-4249-BF6F-D009-17A81532660E",
            "AssetName": "Default__MP5_IceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Spectre",
            "ID": "481A5ABB-45D7-818D-798F-D18D988B6DC1",
            "AssetName": "Default__MP5_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Serenity Spectre",
            "ID": "54EBEA37-4CFE-A79B-707D-0D94017A69A6",
            "AssetName": "Default__MP5_Jade_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Spectre",
            "ID": "BD80C562-4C2D-F00A-156E-9190D023098E",
            "AssetName": "Default__MP5_Kingdom_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Spectre",
            "ID": "7D43477D-465A-67FC-561E-F2A2EBEA697D",
            "AssetName": "Default__MP5_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spectre",
            "ID": "F2EF87C7-4FF5-54F8-E038-CEA4E54EEFDD",
            "AssetName": "Default__MP5_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre",
            "ID": "8A1B2C5B-4692-78AE-9D5C-CDAC6A61E4F4",
            "AssetName": "Default__MP5_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spectre Level 2",
            "ID": "984FA47B-4C3F-CB2A-3FDB-098E342A52F3",
            "AssetName": "Default__MP5_Raygun_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spectre",
            "ID": "1DC45E18-4A07-C85F-0020-6DA4DB1486CE",
            "AssetName": "Default__SubMachineGun_MP5_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Convex Spectre",
            "ID": "FBE265CF-4E3D-9891-791E-5089F1F7F102",
            "AssetName": "Default__MP5_Triangles_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland Spectre",
            "ID": "A83AC09D-4C19-FDA6-8E4D-C1B77DC2B479",
            "AssetName": "Default__MP5_Wasteland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "DF37B069-48B2-0A7C-78EA-5B8EEDC684F7",
            "AssetName": "Default__Vector_ArtDecoLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Stinger",
            "ID": "CD9BEDA3-4042-D79E-6D46-4DAA61484362",
            "AssetName": "Default__Vector_CrimsonOps_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Surge Stinger",
            "ID": "77D5C1DC-4DDE-539C-3A5A-0A95EECBA1E4",
            "AssetName": "Default__Vector_Electroflux3_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Couture Stinger",
            "ID": "84A414F6-4FE4-98FF-8D4E-B5866894C436",
            "AssetName": "Default__Vector_LIW_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation Stinger",
            "ID": "FED9C3F3-40A5-DA67-4AC9-4683CC5A0EBA",
            "AssetName": "Default__Vector_Rainbow_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura Stinger",
            "ID": "E2C84381-4FA6-29B4-37B9-21BBA8AE24BF",
            "AssetName": "Default__Vector_Sakura_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger",
            "ID": "9BC535DD-4D91-3421-2CD0-7A8FDAD3478B",
            "AssetName": "Default__Vector_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 2",
            "ID": "1A8D4093-4E8F-DFE8-9412-E3955662F09C",
            "AssetName": "Default__Vector_Sovereign_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 3",
            "ID": "5E5FD361-4954-2287-012F-F68F624FC879",
            "AssetName": "Default__Vector_Sovereign_Lv3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Stinger Level 4",
            "ID": "B17C1DF5-412C-A9BC-FD65-E6AFB421B13D",
            "AssetName": "Default__Vector_Sovereign_Lv4_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stinger",
            "ID": "471FC2A5-47A7-5B12-2895-0899117D2F57",
            "AssetName": "Default__Vector_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Stinger",
            "ID": "CA2F7BC0-4270-7F76-4623-8596A5584D06",
            "AssetName": "Default__Vector_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula Knife",
            "ID": "88D7C503-477F-C881-AF2C-53BBAB55807C",
            "AssetName": "Default__Melee_Cosmos_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Dagger",
            "ID": "48CE4A70-4207-623B-4739-BFB937812432",
            "AssetName": "Default__Melee__Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Dagger Level 2",
            "ID": "29BD8B5B-4D19-B6AF-70C3-4797C0482E1C",
            "AssetName": "Default__Melee__Cyberpunk_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Dagger",
            "ID": "F3594BCC-43A9-4A74-8C40-98A4E4A4569A",
            "AssetName": "Default__Melee__Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Dagger Level 2",
            "ID": "EF028AC5-40A2-BC8E-582B-C4ABF4ED0EF3",
            "AssetName": "Default__Melee__Dragon_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Knife",
            "ID": "EA441610-42DA-E46F-8D7B-1B9759C105CD",
            "AssetName": "Default__Melee_Base_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Knife Level 2",
            "ID": "34CDB942-4829-EDBF-63CE-BFB3D993BDD1",
            "AssetName": "Default__Melee_Base_Edge_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Sword",
            "ID": "1DC43C70-4DEC-A8E6-E9FA-CDA0033CC041",
            "AssetName": "Default__Melee_Exo_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Dagger",
            "ID": "726B77C9-41C3-80C6-F33E-068B9F74EF56",
            "AssetName": "Default__Melee_Gothic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Axe",
            "ID": "249B0E46-4A11-F045-51BB-649151CD802A",
            "AssetName": "Default__Melee_Base_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Axe Level 2",
            "ID": "DF1ACE24-4ACB-E615-24EB-6E95B7E44DC5",
            "AssetName": "Default__Melee_Base_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism Knife",
            "ID": "7CF3AF0B-4556-A0DB-2E04-EEA4368B354B",
            "AssetName": "Default__Melee_IridescenceLv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Knife",
            "ID": "8C2E0F93-4277-FBB8-20C6-E2B2638B6ED4",
            "AssetName": "Default__Melee__Kingdom_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite Knife",
            "ID": "B6768F01-4D72-F0F1-65B5-71B751536490",
            "AssetName": "Default__Melee_Lightning_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Knife",
            "ID": "E57317AC-4A93-50A9-30E9-93A098513FA9",
            "AssetName": "Default__Melee_Base_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Dagger",
            "ID": "D6E93360-46A2-0103-AFA0-8B91E78B6FE8",
            "AssetName": "Default__Melee_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Energy Sword",
            "ID": "21CEB4B1-480F-DDDB-1422-8AAD73519181",
            "AssetName": "Default__Melee_Oblivion_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Energy Sword Level 2",
            "ID": "24A079A6-4194-0008-BD1C-A980889BB912",
            "AssetName": "Default__Melee_Oblivion_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Claw",
            "ID": "E34039B6-441D-3E17-2773-BDAF5C3D2FAA",
            "AssetName": "Default__Melee__Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Claw Level 2",
            "ID": "444AF7A1-46D4-6139-A4B4-66B3112BD37B",
            "AssetName": "Default__Melee__Oni_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Baton",
            "ID": "3710F62C-4E0C-65FD-848D-8DA25D2FB833",
            "AssetName": "Default__Melee_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Baton Level 2",
            "ID": "7EF7ED92-463E-2E0C-859F-B88DE57F2FB4",
            "AssetName": "Default__Melee_Raygun_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Knife",
            "ID": "D7A02A43-47A5-556C-A69F-EC9CF6EDE66D",
            "AssetName": "Default__Melee_Soulstealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Knife Level 2",
            "ID": "20F6764C-4561-0152-E8A1-E2A75DEB1872",
            "AssetName": "Default__Melee_Soulstealer_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Sword",
            "ID": "90FE45D6-41EA-1C49-8FB9-46B0E98C0077",
            "AssetName": "Default__Melee_Base_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Sword Level 2",
            "ID": "5E7F5D27-46CA-ABD5-72D8-ECBB413EC217",
            "AssetName": "Default__Melee_Base_Sovereign_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Melee",
            "ID": "854938F3-4532-B300-D9A2-379D987D7469",
            "AssetName": "Default__Melee_Base_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ego Knife",
            "ID": "5BF17117-4EAD-A0A8-2961-288D38985E93",
            "AssetName": "Default__Melee_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Attachments": [
        {
            "Name": "",
            "ID": "C1CA73BB-4DCF-F8C0-E6AA-CF8A51EAFC97",
            "AssetName": "Default__Attachment_HMG_ReflexPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "DB9E14FD-4C57-3FCC-3817-0BACFA8B518C",
            "AssetName": "Default__Attachment_LMG_Reflex_RedDotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "D90FF390-4D4D-EE48-8D4C-BC9F7B123692",
            "AssetName": "Default__Attachment_AK_ReflexPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "8C505C5F-4B9E-7338-A54F-24ABA13B2B6B",
            "AssetName": "Default__Attachment_Burst_Reflex_RedDotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Suppressor",
            "ID": "F1278BA5-45C7-E3BC-B239-3D9EE61B989D",
            "AssetName": "Default__Attachment_ACR_Silencer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "C119DA22-419D-5A7D-2E83-CE9C814719E5",
            "AssetName": "Default__Attachment_ACR_Reflex_RedDotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "106E210F-7F8F-408B-8010-81C15AB50032",
            "AssetName": "Default__Attachment_Luger_Silencer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Two Zoom Scope",
            "ID": "E27E029D-47E6-EF77-A21D-A4BA46737070",
            "AssetName": "Default__Attachment_BoltSniper_2XScope_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "",
            "ID": "2CABD857-439B-33B4-CEF7-03A8137ED1E4",
            "AssetName": "Default__Attachment_DMR_Reflex_ReddotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard Scope",
            "ID": "03E545A4-4E19-98BE-421C-EDBA218FDA66",
            "AssetName": "Default__Scope_Lever_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Suppressor",
            "ID": "A711565A-E57C-43C8-9395-E7D09229FF26",
            "AssetName": "Default__Attachment_MP5_Silencer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "C59421D8-D7DC-4E75-8FB9-90710386599E",
            "AssetName": "Default__Attachment_MP5_Reflex_RedDotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "D1D44263-4192-CEBC-0974-D48EF2F15E1D",
            "AssetName": "Default__Attachment_Vector_Reflex_RedDotPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Equips": [
        {
            "Name": "SPIKE",
            "ID": "0AFB2636-4093-C63B-4EF1-1E97966E2A3E",
            "AssetName": "Default__BombEquippable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Odin",
            "ID": "63E6C2B6-4A8E-869C-3D4C-E38355226584",
            "AssetName": "Default__HMGPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ares",
            "ID": "55D8A0F4-4274-CA67-FE2C-06AB45EFDF58",
            "AssetName": "Default__LMGPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Vandal",
            "ID": "9C82E19D-4575-0200-1A81-3EACF00CF872",
            "AssetName": "Default__AKPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Bulldog",
            "ID": "AE3DE142-4D85-2547-DD26-4E90BED35CF7",
            "AssetName": "Default__BurstPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Phantom",
            "ID": "EE8E8D15-496B-07AC-E5F6-8FAE5D4C7B1A",
            "AssetName": "Default__CarbinePrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Classic",
            "ID": "C5DE005C-4BDC-26A7-A47D-C295EAAAE9D8",
            "AssetName": "Default__BasePistolNPEPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Judge",
            "ID": "EC845BF4-4F79-DDDA-A3DA-0DB3774B2794",
            "AssetName": "Default__AutoShotgunPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Bucky",
            "ID": "910BE174-449B-C412-AB22-D0873436B21B",
            "AssetName": "Default__PumpShotgunPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Frenzy",
            "ID": "44D4E95C-4157-0037-81B2-17841BF2E8E3",
            "AssetName": "Default__AutoPistolPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Classic",
            "ID": "29A0CFAB-485B-F5D5-779A-B59F85E204A8",
            "AssetName": "Default__BasePistolPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ghost",
            "ID": "1BAA85B4-4C70-1284-64BB-6481DFC3BB4E",
            "AssetName": "Default__LugerPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Sheriff",
            "ID": "E336C6B8-418D-9340-D77F-7A9E4CFE0702",
            "AssetName": "Default__RevolverPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Shorty",
            "ID": "42DA8CCC-40D5-AFFC-BEEC-15AA47B42EDA",
            "AssetName": "Default__SlimPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Operator",
            "ID": "A03B24D3-4319-996D-0F8C-94BBFBA1DFC7",
            "AssetName": "Default__BoltSniperPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Guardian",
            "ID": "4ADE7FAA-4CF1-8376-95EF-39884480959B",
            "AssetName": "Default__DMRPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Marshal",
            "ID": "C4883E50-4494-202C-3EC3-6B8A9284F00B",
            "AssetName": "Default__LeverSniperPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Spectre",
            "ID": "462080D1-4035-2937-7C09-27AA2A5C27A7",
            "AssetName": "Default__MP5PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Stinger",
            "ID": "F7E1B454-4AD4-1063-EC0A-159E56B58941",
            "AssetName": "Default__VectorPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Melee",
            "ID": "2F59173C-4BED-B6C3-2191-DEA9B58BE9C7",
            "AssetName": "Default__Melee_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Golden Gun",
            "ID": "3DE32920-4A8F-0499-7740-648A5BF95470",
            "AssetName": "Default__SpikeRush_GoldenGun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Themes": [
        {
            "Name": "Aristocrat",
            "ID": "38F408DC-416E-EDA9-3AC5-21892C5F5AD1",
            "AssetName": "Default__Theme_ArtDeco_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Breach",
            "ID": "3B17210D-408B-E1F0-069B-FD8F6E61E90D",
            "AssetName": "Default__Theme_Breach_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bullet01",
            "ID": "A081D668-4D28-1BF5-C7F8-9592EC8AD7F7",
            "AssetName": "Default__Theme_Bullet01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "CB",
            "ID": "151E1837-47EF-27F5-74C8-D687CEA2F1C5",
            "AssetName": "Default__Theme_CB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Clay",
            "ID": "AEED5CC9-4686-9272-E76A-3A9092B5CE0E",
            "AssetName": "Default__Theme_Clay_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP1 Coin",
            "ID": "C913E306-4823-8ABE-8DCC-ECA89EE1CEC0",
            "AssetName": "Default__Theme_Coin_EP1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula",
            "ID": "7E1B7375-4B1D-9E2F-14F2-ACB278400826",
            "AssetName": "Default__Theme_Cosmos_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Crate1",
            "ID": "1480C950-441E-6548-D4AD-EEA4C82F881E",
            "AssetName": "Default__Theme_Crate1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "CrateKingdom",
            "ID": "1062A169-4DDF-C074-B53C-829CF0DA021F",
            "AssetName": "Default__Theme_CrateKingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "CrimsonOps",
            "ID": "C2A38AF9-4D9F-010E-47A0-F5B06570C976",
            "AssetName": "Default__Theme_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop",
            "ID": "5B014F36-414B-4703-9C65-1876C630FEAA",
            "AssetName": "Default__Theme_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Doughnut",
            "ID": "E2C217AC-46DF-20CC-86C0-25B272AB7D3A",
            "AssetName": "Default__Theme_Doughnut_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame",
            "ID": "6245CBBC-4AA3-B339-0D2E-ABB333F6C8C5",
            "AssetName": "Default__Theme_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity",
            "ID": "738936D8-5551-4748-9660-44909304F74B",
            "AssetName": "Default__Theme_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Electroflux3",
            "ID": "F8CA8370-4CDB-67E6-8862-9684AC410148",
            "AssetName": "Default__Theme_Electroflux3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rush",
            "ID": "00347950-4139-2BC2-B594-BC8293CE9342",
            "AssetName": "Default__Theme_Electroflux_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Exo",
            "ID": "E0652066-4C7F-2229-2921-749B044FFD48",
            "AssetName": "Default__Theme_Exo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "FloatingIsland",
            "ID": "9D8CEFA5-4FD7-7AD0-6639-61AE5728FF0C",
            "AssetName": "Default__Theme_FloatingIsland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gelato",
            "ID": "EA250FE3-4D6F-7271-0905-A387ABC506F4",
            "AssetName": "Default__Theme_Gelato_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin",
            "ID": "F1BE220C-4370-C5E9-FA8E-2F9227BA81DE",
            "AssetName": "Default__Theme_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Grid",
            "ID": "271874EB-491B-EAE3-51F8-6F93F93035F9",
            "AssetName": "Default__Theme_Grid_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Guide",
            "ID": "EE89C075-4806-CA65-6436-DB92563B1F3E",
            "AssetName": "Default__Theme_Guide_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gumshoe",
            "ID": "CA77E082-4C08-BF86-2D62-6A8628398615",
            "AssetName": "Default__Theme_Gumshoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hunter",
            "ID": "818FADB7-4DAC-E808-60DD-95BC704A9395",
            "AssetName": "Default__Theme_Hunter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime",
            "ID": "9436FE00-4156-E115-B11F-F69CAC91A6A5",
            "AssetName": "Default__Theme_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche",
            "ID": "13FE8A00-4B7B-7B67-FB79-75B176A32238",
            "AssetName": "Default__Theme_Ice_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism",
            "ID": "7E94D78A-498E-67CB-DE3D-80A36CEE46CF",
            "AssetName": "Default__Theme_Iridescence_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jade",
            "ID": "EE2AB81E-4F02-0832-121F-1FB1F0F5F016",
            "AssetName": "Default__Theme_Jade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Killjoy",
            "ID": "DFFFC0F0-4D14-B358-AB2C-1FA303B5564D",
            "AssetName": "Default__Theme_Killjoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom",
            "ID": "4B6CE579-4A00-D107-6E45-50A5E77CC526",
            "AssetName": "Default__Theme_Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite",
            "ID": "465336B0-4261-9DCA-F6E8-109AD2C40381",
            "AssetName": "Default__Theme_Lightning_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "LIW",
            "ID": "124B113B-420D-36E5-AD9C-56A36852ACC7",
            "AssetName": "Default__Theme_LIW_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "LuckyCat",
            "ID": "AF536BA4-45B3-C187-C8DB-3088CE2A48A4",
            "AssetName": "Default__Theme_LuckyCat_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe",
            "ID": "F22881CC-4A4A-9BC3-D5E9-AD816B42C2D7",
            "AssetName": "Default__Theme_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline",
            "ID": "55A92145-402F-5453-844B-40AF300FC005",
            "AssetName": "Default__Theme_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Galleria",
            "ID": "0C4EE4BA-484A-8FD2-E680-AABA9315CEA4",
            "AssetName": "Default__Theme_Murals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion",
            "ID": "5186D489-450E-BF5E-F129-2DBAA3034A28",
            "AssetName": "Default__Theme_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Onboarding",
            "ID": "59AA59B4-4ACA-2A44-A9D4-A29DC69FDBFA",
            "AssetName": "Default__Theme_Onboarding_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni",
            "ID": "8A34391F-4D1F-6B22-859F-628BFF79D381",
            "AssetName": "Default__Theme_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pandemic",
            "ID": "AD7C6D69-421D-6929-561D-3FBBE1FB596B",
            "AssetName": "Default__Theme_Pandemic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phoenix",
            "ID": "F1543CA6-4D3B-4663-CD6B-4A940B79F1A1",
            "AssetName": "Default__Theme_Phoenix_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pizza",
            "ID": "12142D3E-4BDA-F937-BFF4-A786DA09FDA2",
            "AssetName": "Default__Theme_Pizza_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Polyanimals",
            "ID": "6CE582D1-4CF9-EFC4-078C-169295311F7E",
            "AssetName": "Default__Theme_Polyanimals_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "RadioniteDiamond",
            "ID": "CAB8EC80-4A16-4F53-297F-D3B43FAF6991",
            "AssetName": "Default__Theme_RadioniteDiamond_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation",
            "ID": "548CC24D-4127-A9C3-060C-B2BADA325474",
            "AssetName": "Default__Theme_Rainbow_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster",
            "ID": "CA390B2F-4F2E-12AC-C225-F28BD0F1FD45",
            "AssetName": "Default__Theme_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sakura",
            "ID": "3807F2F2-40C3-0FCE-49CC-708961B60C75",
            "AssetName": "Default__Theme_Sakura_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sarge",
            "ID": "4C02AB17-4C0E-1B88-10E4-7FAC410ABFDF",
            "AssetName": "Default__Theme_Sarge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver",
            "ID": "4479EEA8-4820-C69B-3912-F5AC678FCEDC",
            "AssetName": "Default__Theme_SoulStealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign",
            "ID": "975F7716-498D-8E0B-B7C7-02B507B8E14A",
            "AssetName": "Default__Theme_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Standard",
            "ID": "5A629DF4-4765-0214-BD40-FBB96542941F",
            "AssetName": "Default__Theme_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "SwissCheese",
            "ID": "1248174A-47EC-70A0-346C-278AB65F6958",
            "AssetName": "Default__Theme_SwissCheese_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Thorne",
            "ID": "EE1E3F3C-4837-2330-5E1F-7BA1A6BB2950",
            "AssetName": "Default__Theme_Thorne_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Toaster",
            "ID": "5EF5C2FE-4DB8-EBD7-5E9D-ADBFAB942DFA",
            "AssetName": "Default__Theme_Toaster_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Convex",
            "ID": "B88F012B-4623-E192-26FB-1AB23051BD17",
            "AssetName": "Default__Theme_Triangles_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego",
            "ID": "54E935E3-446F-5184-BA3A-F096C595B146",
            "AssetName": "Default__Theme_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vampire",
            "ID": "2A5C2836-4F75-0A01-089D-EAAF43CC7D14",
            "AssetName": "Default__Theme_Vampire_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland",
            "ID": "04BB8AA5-4BAB-CD4E-E1F0-D9AA3B7BD79D",
            "AssetName": "Default__Theme_Wasteland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wraith",
            "ID": "DEF525C9-4151-AB71-5A18-C7BFF46D4E46",
            "AssetName": "Default__Theme_Wraith_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wushu",
            "ID": "897F7222-4EB3-B86C-1093-7D883C36C731",
            "AssetName": "Default__Theme_Wushu_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "GameModes": [
        {
            "Name": "Standard",
            "ID": "96BD3920-4F36-D026-2B28-C683EB0BCAC5",
            "AssetName": "BombGameMode",
            "AssetPath": "/Game/GameModes/Bomb/BombGameMode.BombGameMode_C",
            "IsEnabled": true
        },
        {
            "Name": "Deathmatch",
            "ID": "A8790EC5-4237-F2F0-E93B-08A8E89865B2",
            "AssetName": "DeathmatchGameMode",
            "AssetPath": "/Game/GameModes/Deathmatch/DeathmatchGameMode.DeathmatchGameMode_C",
            "IsEnabled": true
        },
        {
            "Name": "Onboarding",
            "ID": "D2B4E425-4CAB-8D95-EB26-BB9B444551DC",
            "AssetName": "NPEGameMode",
            "AssetPath": "/Game/GameModes/NewPlayerExperience/NPEGameMode.NPEGameMode_C",
            "IsEnabled": true
        },
        {
            "Name": "Spike Rush",
            "ID": "E921D1E6-416B-C31F-1291-74930C330B7B",
            "AssetName": "QuickBombGameMode",
            "AssetPath": "/Game/GameModes/QuickBomb/QuickBombGameMode.QuickBombGameMode_C",
            "IsEnabled": true
        },
        {
            "Name": "PRACTICE",
            "ID": "E2DC3878-4FE5-D132-28F8-3D8C259EFCC6",
            "AssetName": "ShootingRangeGameMode",
            "AssetPath": "/Game/GameModes/ShootingRange/ShootingRangeGameMode.ShootingRangeGameMode_C",
            "IsEnabled": true
        }
    ],
    "Sprays": [
        {
            "Name": "Caught on Camera Spray",
            "ID": "3D2BCFC5-442B-812E-3C08-9180D6B36077",
            "AssetName": "Default__CaughtOnCamera_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chicken Out Spray",
            "ID": "81C68821-46D3-9176-294C-ABBA0BC64E0B",
            "AssetName": "Default__ChickenReborn_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Defy the Limits Spray",
            "ID": "06351C4A-4A93-793E-F5C9-2FA675359A93",
            "AssetName": "Default__DefyTheLimits_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "G.O.A.T. Spray",
            "ID": "0EB56D06-474D-FBEC-372F-069286388BC5",
            "AssetName": "Default__GOAT_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sad Crab Spray",
            "ID": "D52D5D56-46A7-957D-418D-E3B2B3BD6938",
            "AssetName": "Default__Grief_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Time Spray",
            "ID": "677DC003-4DBF-66A8-9116-4F8D7A9FB8D5",
            "AssetName": "Default__NoTime_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Toxicity Spray",
            "ID": "2B2AE992-403A-F063-64E6-1DBAEE43C95A",
            "AssetName": "Default__NoToxicity_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dark Side Beyond Spray",
            "ID": "7CF85D79-4912-CCB9-FA59-F28E065AE9D5",
            "AssetName": "Default__RadianitePortal_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dap Team Spray",
            "ID": "D4CEEF7F-4E99-70D8-AC85-14850AC08CD3",
            "AssetName": "Default__Teamwork_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "This is Also Fine Spray",
            "ID": "4C08026B-4F56-9494-0D71-3DBB291C4D7F",
            "AssetName": "Default__ThisIsFine_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Little Onion Lad Spray",
            "ID": "82FFCC4C-4195-5399-5D70-F7B1CDD16E37",
            "AssetName": "Default__TurnipBud_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheaters Never Prosper Spray",
            "ID": "936F33FB-49D9-277C-496D-CD9EF04A34CC",
            "AssetName": "Default__VanguardAnticheat_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wanted: Tactibunny Spray",
            "ID": "83CF10B1-42EF-E339-97C6-169F46504733",
            "AssetName": "Default__WantedTactibunny_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "8-bit VALORANT Spray",
            "ID": "2527155B-4BA6-632B-C745-71900A25AB80",
            "AssetName": "Default__8BitVAL_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GGWP Spray",
            "ID": "89565F02-495E-E6F0-5F67-959626122909",
            "AssetName": "Default__GGWP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Mic Drop Spray",
            "ID": "78CF178D-4165-43B8-1ECF-F78771505AF9",
            "AssetName": "Default__MicDrop_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Step Under Here Spray",
            "ID": "9D7DF4CC-4311-42DA-1220-2C9F3BC8C2CC",
            "AssetName": "Default__Mistletoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Op Spray",
            "ID": "04251D6A-4548-856B-5EA1-19B01783C430",
            "AssetName": "Default__NoOperator_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Piece of Cake Spray",
            "ID": "75B2F43A-4154-A1DC-1C6F-EDB5FE224B2A",
            "AssetName": "Default__PieceOfCake_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Octorave Spray",
            "ID": "5972097D-4904-9C86-03C6-E2878C1F0719",
            "AssetName": "Default__Radianite_Octopus_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pick My Strat Spray",
            "ID": "E279312D-4321-5194-13F5-6897B0A005CF",
            "AssetName": "Default__RNGStrats_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stellar Dendrite Spray",
            "ID": "4CA4B72D-4EB4-3A3E-0079-06A31DC06B9B",
            "AssetName": "Default__Snowflake_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Thumbs Up Spray",
            "ID": "43341E92-451F-C194-B4F6-0B926BDC3643",
            "AssetName": "Default__ThumbsUp_KJ_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stay Safe, Wash Your Hands Spray",
            "ID": "5D6CADDA-42C3-1CAC-94D3-458917F5CB2C",
            "AssetName": "Default__ViperCOVID_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Breach Spray",
            "ID": "A05C50B7-4A1D-C2DE-E1E7-AC8A7730DAA4",
            "AssetName": "Default__Spray_BreachCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "K.O. Spray",
            "ID": "DCC8F0DF-46B9-0A3E-7A0F-74A7558DDAFC",
            "AssetName": "Default__Spray_Breach01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Guns Out Spray",
            "ID": "92641409-4113-B674-F95D-FC85F29BF921",
            "AssetName": "Default__Spray_Breach02_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "FTW Spray",
            "ID": "36EE876C-4918-69C7-9CE4-9DAC0B4B929A",
            "AssetName": "Default__Spray_Bullets_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Camper Spray",
            "ID": "71E8FDCA-4099-AF1C-FABF-09A35684E2D0",
            "AssetName": "Default__Spray_Camper_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Excuse Me? Spray",
            "ID": "500DA6BD-4CF1-3362-BE2B-1487EC286B91",
            "AssetName": "Default__Spray_CatWhat_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheesy Shot Spray",
            "ID": "254E3D77-40B8-CFAE-232A-F7A36EE27D61",
            "AssetName": "Default__Spray_Cheese_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Raze Spray",
            "ID": "186CADC9-4356-BCAE-4CBB-CE83F8B15E4F",
            "AssetName": "Default__Spray_RazeCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "BoomShaka Spray",
            "ID": "32FC4BFD-4897-CE74-55D2-9BB008F0DECB",
            "AssetName": "Default__Spray_Clay01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bombshell Spray",
            "ID": "A64B8EDA-4920-434A-5346-30BFB1B58E39",
            "AssetName": "Default__Spray_Clay02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Explorgi Spray",
            "ID": "25D82D17-4739-E206-E8AA-D1BD4FD4DAE6",
            "AssetName": "Default__Spray_Corgi_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Danger Spray",
            "ID": "32570250-4795-981D-BDA7-34963AA042F9",
            "AssetName": "Default__Spray_Danger_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Spray",
            "ID": "0A6DB78C-48B9-A32D-C47A-82BE597584C1",
            "AssetName": "Default__Spray_Default_VALLogo_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Elderflame Spray",
            "ID": "0221E96D-49BE-A601-52D6-EF8270773276",
            "AssetName": "Default__Spray_Dragon01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Fist Bump Spray",
            "ID": "D8CFCE74-4BB8-42B2-022E-9DBF9D648823",
            "AssetName": "Default__Spray_Fist_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GG Shooter Spray",
            "ID": "B520005E-42CF-169C-AB30-A7A60D7F29F1",
            "AssetName": "Default__Spray_GG_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GLHF Spray",
            "ID": "6983AE7C-4CB5-835C-8F62-B7AFFBAAE20E",
            "AssetName": "Default__Spray_GLHFNPE_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wild Life Spray",
            "ID": "7A50C4ED-46F5-7C80-FF43-3EA22E40AEF2",
            "AssetName": "Default__Guide01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "On Your Trail Spray",
            "ID": "7FB920F1-43AF-6172-18A3-36A38EEBA039",
            "AssetName": "Default__Guide02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Skye Spray",
            "ID": "A6779E98-4998-BF8A-8CA6-A783684A7834",
            "AssetName": "Default__GuideCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cypher Spray",
            "ID": "E8754A6E-4EC5-3D1C-2ED9-E0A5FF9F1271",
            "AssetName": "Default__Spray_CypherCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Seeker Spray",
            "ID": "26DF3792-4540-CE9B-6048-11AB72BC4F94",
            "AssetName": "Default__Spray_Gumshoe01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "I See You Spray",
            "ID": "DB1DCDC0-4473-5598-05E4-D4859FA9D340",
            "AssetName": "Default__Spray_Gumshoe02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Lethal Crosshair Spray",
            "ID": "706200B9-40BD-8D93-0442-FF94F6A0FD6E",
            "AssetName": "Default__Spray_Headshot_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sova Spray",
            "ID": "1D63D0B1-4946-A76F-C280-AA8BA3F94772",
            "AssetName": "Default__Spray_SovaCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Take Flight Spray",
            "ID": "F61F23BA-4F5A-0E31-E7EB-CCBC18700676",
            "AssetName": "Default__Spray_Hunter01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "On Target Spray",
            "ID": "60384125-47DD-134F-CD80-FE861830F63C",
            "AssetName": "Default__Spray_Hunter03_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Brick Spray",
            "ID": "880D5DE5-4268-769D-5407-55921AD2DB12",
            "AssetName": "Default__Spray_HypeBeastBrick_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Killjoy Spray",
            "ID": "17678625-4F24-6BDE-58FB-7198778E4FDB",
            "AssetName": "Default__Spray_KilljoyCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Variable Removed Spray",
            "ID": "B11B4890-4E7F-CF5F-BE7C-9C85ECD50868",
            "AssetName": "Default__Spray_KilljoyTurret_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Don't Cross Me Spray",
            "ID": "0A20236D-47D4-E9E6-ADB1-A69ED3FDB1CD",
            "AssetName": "Default__Spray_Wrench_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Lights Out Spray",
            "ID": "9C65BBE6-41DA-C50C-BE81-839214EEDE7C",
            "AssetName": "Default__Spray_LightsOut_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Octo Attack 2 Spray",
            "ID": "CD3D4242-4282-9210-F34F-9998E8B1F9E0",
            "AssetName": "Default__OctoAttack_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pick Your Poison Spray",
            "ID": "145DC009-4F60-0872-0F81-69957D520317",
            "AssetName": "Default__Contract_Spray_Pandemic01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Deadly Venom Spray",
            "ID": "9EAAEC2B-4A81-5691-9A14-2684AB242949",
            "AssetName": "Default__Contract_Spray_Pandemic02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Viper Spray",
            "ID": "36EA48C6-4802-0D7C-AE97-D0A20DB12A1D",
            "AssetName": "Default__Spray_ViperCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phoenix Spray",
            "ID": "47EC7318-4797-56D6-79AC-86AD59081881",
            "AssetName": "Default__Spray_PhoenixCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Claim the Crown Spray",
            "ID": "13CC701A-4321-E105-3B66-01AFFE7DA31A",
            "AssetName": "Default__Spray_Phoenix01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spotlight Spray",
            "ID": "1024275A-4673-8D84-E796-DBBABF611614",
            "AssetName": "Default__Spray_Phoenix02_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Salt Shaker Spray",
            "ID": "EECE70BE-4F84-FACB-49B0-FE95290EFF67",
            "AssetName": "Default__Spray_Salt_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Brimstone Spray",
            "ID": "BE343D37-465E-1878-E6D0-9ABA467D7CCA",
            "AssetName": "Default__Spray_BrimstoneCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Big One Spray",
            "ID": "B16024B9-4F5E-6DFA-C229-7D9C620C24D0",
            "AssetName": "Default__Spray_Sarge01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Getting Reps  Spray",
            "ID": "50BC437D-46C4-E58F-E479-848BECFB48FD",
            "AssetName": "Default__Spray_Sarge02_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Spray",
            "ID": "2E37F837-425D-45F2-22A2-71A9AF5C118F",
            "AssetName": "Default__Spray_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spray",
            "ID": "369C7CDA-4133-B3AB-2C8B-3E8F371CB181",
            "AssetName": "Default__Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Spray",
            "ID": "021C99DD-4A43-01FB-70DF-FC83CD0F0560",
            "AssetName": "Default__Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spray",
            "ID": "9A657204-4376-ED61-AD3E-0A8B7BBECD18",
            "AssetName": "Default__Spray_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Spray",
            "ID": "444464F1-445F-8F75-3C8D-A7BD8F24E654",
            "AssetName": "Default__Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Spray",
            "ID": "1091D2CC-430B-56CA-A82B-279B70026193",
            "AssetName": "Default__Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spray",
            "ID": "735E6C3C-4899-532D-60CF-1BA0CE1A450D",
            "AssetName": "Default__Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Spray",
            "ID": "1658E811-4084-8775-28DF-5A9FEABC52D8",
            "AssetName": "Default__SoulStealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Spray",
            "ID": "71D260CA-4BAD-81F2-0298-44860341A7A6",
            "AssetName": "Default__Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Spray",
            "ID": "D54E0883-4967-5808-E25C-37B3E6313E5C",
            "AssetName": "Default__Spray_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Clip It Spray",
            "ID": "180A93CB-4BA4-DB87-B357-B9B104373A74",
            "AssetName": "Default__Spray_ClipIt_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Tactibear Spray",
            "ID": "BF2188F1-4B0A-A55F-C631-67A54AC1CCC5",
            "AssetName": "Default__Spray_Tactibear_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sage Spray",
            "ID": "2CF3C29C-49EC-7297-93F8-35988FCE5CA6",
            "AssetName": "Default__Spray_SageCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "All Good Spray",
            "ID": "D16B0B8C-4106-493B-F231-AC9B4D56372F",
            "AssetName": "Default__Spray_Thorne01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pulse Check Spray",
            "ID": "6410980B-493B-63BF-0860-31940C553EAD",
            "AssetName": "Default__Spray_Thorne03_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "V for VALORANT Spray",
            "ID": "5D88FD45-434D-B0D6-2331-E8B3D47B8395",
            "AssetName": "Default__Spray_VALLogoNPE_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reyna Spray",
            "ID": "0C342C8C-492E-E20E-CF06-C694EC4A386F",
            "AssetName": "Default__Spray_ReynaCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Leer Spray",
            "ID": "87B81520-4EAA-0536-4C45-BABD5A35A15B",
            "AssetName": "Default__Spray_Vampire01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Marked for Death Spray",
            "ID": "BB6FD4D0-4BA1-68A1-A1E2-D6B1A33D6B9D",
            "AssetName": "Default__Spray_Vampire02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vandal Life Spray",
            "ID": "27C5FD11-4F69-031A-6EE0-6DA838ED7998",
            "AssetName": "Default__Spray_WeaponStencil_Act1BP_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Omen Spray",
            "ID": "FD1A5A33-4170-95A4-F02A-118FB3F0B5C3",
            "AssetName": "Default__Spray_OmenCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "It Hunts Spray",
            "ID": "DA814168-4AB3-98FB-847A-29967FA91C42",
            "AssetName": "Default__Contract_Spray_Wraith01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dark Focus Spray",
            "ID": "E3078809-4D75-8439-5BF6-2BADA7E1E5A4",
            "AssetName": "Default__Contract_Spray_Wraith02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jett Spray",
            "ID": "5DBE809E-4DCB-2CC1-6AFE-57B3A7F4A303",
            "AssetName": "Default__Spray_JettCallsign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Watch This Spray",
            "ID": "CF824D0A-4BF5-0864-6CA2-EFA4D00A819B",
            "AssetName": "Default__Spray_Wushu01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "You Better Run Spray",
            "ID": "5DC78E1A-4ACD-AC48-69D2-A99591E9563F",
            "AssetName": "Default__Spray_Wushu02_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "SprayLevels": [
        {
            "Name": "Caught on Camera Spray",
            "ID": "20D547A4-4EC8-C9EF-DD9D-1C8B74D0E6F7",
            "AssetName": "Default__CaughtOnCamera_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chicken Out Spray",
            "ID": "47484536-4406-CC35-4792-1485ACCB9862",
            "AssetName": "Default__ChickenReborn_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Defy the Limits Spray",
            "ID": "6720FABE-4CFD-087C-B439-6EA3E96797FF",
            "AssetName": "Default__DefyTheLimits_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "G.O.A.T. Spray",
            "ID": "0628B81F-45BD-182E-45D9-3C855EB0020E",
            "AssetName": "Default__GOAT_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sad Crab Spray",
            "ID": "60ADBF1B-48B7-B4A1-CCEE-50B889C34514",
            "AssetName": "Default__Grief_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Time Spray",
            "ID": "04075A6F-4045-BB00-241D-35B207D015BE",
            "AssetName": "Default__NoTime_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Toxicity Spray",
            "ID": "EC428AD4-491C-72F6-7ED7-94A1D189209B",
            "AssetName": "Default__NoToxicity_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dark Side Beyond Spray",
            "ID": "14352CCD-46FA-42E1-6D53-F0895EA3B22F",
            "AssetName": "Default__RadianitePortal_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dap Team Spray",
            "ID": "0D413C36-4801-50BF-9529-D0AFD0FDA8B7",
            "AssetName": "Default__Teamwork_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "This is Also Fine Spray",
            "ID": "43CDB268-4F4C-3987-5DBD-C68A50EC65FA",
            "AssetName": "Default__ThisIsFine_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Little Onion Lad Spray",
            "ID": "F7479644-4C2C-00B5-160E-8E9C1F4CC29C",
            "AssetName": "Default__TurnipBud_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheaters Never Prosper Spray",
            "ID": "AF057481-4427-81E7-E31B-61BF2F55703D",
            "AssetName": "Default__VanguardAnticheat_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wanted: Tactibunny Spray",
            "ID": "3C977A19-41C4-EF77-CA5C-148FECD1095A",
            "AssetName": "Default__WantedTactibunny_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "8-bit VALORANT Spray",
            "ID": "0A3D7DCF-4267-564D-5575-F28B682A3834",
            "AssetName": "Default__8BitVAL_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GGWP Spray",
            "ID": "F586CDAA-4D3B-8551-4155-748E3BBFA765",
            "AssetName": "Default__GGWP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Mic Drop Spray",
            "ID": "116717BA-4820-1D20-2AA8-86AE72727A9D",
            "AssetName": "Default__MicDrop_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Step Under Here Spray",
            "ID": "402B54FF-408A-EF1C-3AA2-8F9F9B477475",
            "AssetName": "Default__Mistletoe_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No Op Spray",
            "ID": "21306B28-43D1-E528-9F73-C3A7DD0C21EE",
            "AssetName": "Default__NoOperator_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Piece of Cake Spray",
            "ID": "6BEB4B1B-4625-AC17-5ED7-AF93313656A6",
            "AssetName": "Default__PieceOfCake_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Octorave Spray",
            "ID": "1661EF43-47E0-0BF2-1E5B-D7A5CA3FEE82",
            "AssetName": "Default__Radianite_Octopus_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pick My Strat Spray",
            "ID": "B9F67327-4B1E-325D-EC07-9B8123C882FF",
            "AssetName": "Default__RNGStrats_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stellar Dendrite Spray",
            "ID": "CEDD19EB-4FA7-7931-923B-65A1CEAEE56B",
            "AssetName": "Default__Snowflake_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Thumbs Up Spray",
            "ID": "1A163BC4-4E74-1917-38BC-EC853E9B949F",
            "AssetName": "Default__ThumbsUp_KJ_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Stay Safe, Wash Your Hands Spray",
            "ID": "72D18701-41B7-9FAA-9DBF-2C990D445B47",
            "AssetName": "Default__ViperCOVID_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Breach Spray",
            "ID": "36BA4655-46F2-DC45-6172-559D66F7FFB5",
            "AssetName": "Default__Spray_BreachCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "K.O. Spray",
            "ID": "BCBF6B1D-4EA7-985B-8962-CBA5BD859828",
            "AssetName": "Default__Spray_Breach01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Guns Out Spray",
            "ID": "FC9AAFE3-4546-83AC-94E4-1F9A39473DD4",
            "AssetName": "Default__Spray_Breach02_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "FTW Spray",
            "ID": "78EC70FB-4C00-3E98-9B58-0888020A7890",
            "AssetName": "Default__Spray_Bullets_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Camper Spray",
            "ID": "7C5FD8CC-4B81-1D14-45BE-A99B00DE2EB8",
            "AssetName": "Default__Spray_Camper_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Excuse Me? Spray",
            "ID": "25741009-4CE6-F6B4-9B76-B38006925758",
            "AssetName": "Default__Spray_CatWhat_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheesy Shot Spray",
            "ID": "FA7763E1-4F67-7EE5-7890-79936EE6AE3F",
            "AssetName": "Default__Spray_Cheese_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Raze Spray",
            "ID": "06B0D1F1-473E-3EFB-2196-64BECB4D761A",
            "AssetName": "Default__Spray_RazeCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "BoomShaka Spray",
            "ID": "8BF8552E-44E7-8DD7-E5FF-A290BF593B07",
            "AssetName": "Default__Spray_Clay01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bombshell Spray",
            "ID": "6BACE1F7-41C6-9AFE-CD5F-A8BED70F9F17",
            "AssetName": "Default__Spray_Clay02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Explorgi Spray",
            "ID": "1DC18B98-4993-5FAB-304F-6EABA1B85C44",
            "AssetName": "Default__Spray_Corgi_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Danger Spray",
            "ID": "4DD06FFC-45EB-85E1-0C70-B78CA9F52AC7",
            "AssetName": "Default__Spray_Danger_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Spray",
            "ID": "AF3A4261-4C81-266D-7963-82AD714B190F",
            "AssetName": "Default__Spray_Default_VALLogo_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Elderflame Spray",
            "ID": "001CA7BC-45B8-F89C-DD75-87874AD158F6",
            "AssetName": "Default__Spray_Dragon01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Fist Bump Spray",
            "ID": "65A0E616-4169-1187-8DAA-D696777CBA48",
            "AssetName": "Default__Spray_Fist_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GG Shooter Spray",
            "ID": "4471CE86-4FCC-E6EE-32AB-4EAD1B475BDA",
            "AssetName": "Default__Spray_GG_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GLHF Spray",
            "ID": "D774FC07-45E2-0F19-F475-C0B1B9661323",
            "AssetName": "Default__Spray_GLHFNPE_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wild Life Spray",
            "ID": "9BFAF6E9-4A54-5539-BF05-AFABEF676B15",
            "AssetName": "Default__Guide01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "On Your Trail Spray",
            "ID": "7548C6DF-476D-4807-D535-1E9CEAC3C666",
            "AssetName": "Default__Guide02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Skye Spray",
            "ID": "811FD7AB-4A85-D68A-8C08-FFA228E5BD98",
            "AssetName": "Default__GuideCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cypher Spray",
            "ID": "067E3A7D-4BAC-788E-6569-09AC8A7457FE",
            "AssetName": "Default__Spray_CypherCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Seeker Spray",
            "ID": "1EDA98D2-46D4-5D6A-EB88-E19DB8E7815C",
            "AssetName": "Default__Spray_Gumshoe01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "I See You Spray",
            "ID": "266D3C0A-47D8-3B9F-597F-6DAFC7A02F97",
            "AssetName": "Default__Spray_Gumshoe02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Lethal Crosshair Spray",
            "ID": "16CAF7B5-4385-5E6B-35C6-D9B4E1275204",
            "AssetName": "Default__Spray_Headshot_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sova Spray",
            "ID": "B16F37F3-4046-304E-2A53-50B404E60243",
            "AssetName": "Default__Spray_SovaCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Take Flight Spray",
            "ID": "535DDA82-46A2-6056-5235-D7871E4BBFF5",
            "AssetName": "Default__Spray_Hunter01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "On Target Spray",
            "ID": "E094A970-4FA2-11FE-82A6-F5A1631C8EA2",
            "AssetName": "Default__Spray_Hunter03_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Brick Spray",
            "ID": "E6095080-447E-C3D8-DA24-69B3F521B7E9",
            "AssetName": "Default__Spray_HypeBeastBrick_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Killjoy Spray",
            "ID": "7ACFE83B-4C1F-3027-9B2F-4987DBF2AB53",
            "AssetName": "Default__Spray_KilljoyCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Variable Removed Spray",
            "ID": "3BFD89C1-44D8-394A-261C-CA9CBE5D6263",
            "AssetName": "Default__Spray_KilljoyTurret_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Don't Cross Me Spray",
            "ID": "6E045CCF-42E9-1ACF-9522-5B8C34193FAC",
            "AssetName": "Default__Spray_Wrench_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Lights Out Spray",
            "ID": "5C618D37-4959-19B0-4493-F698D330E5EA",
            "AssetName": "Default__Spray_LightsOut_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Octo Attack 2 Spray",
            "ID": "7CE49058-493E-C18C-D906-0583D1E876F9",
            "AssetName": "Default__OctoAttack_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pick Your Poison Spray",
            "ID": "DECE39A1-C8B6-4007-AD0B-046C0FA96F55",
            "AssetName": "Default__Contract_Spray_Pandemic01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Deadly Venom Spray",
            "ID": "40F3B48B-5486-40B9-926C-09A1F04F303D",
            "AssetName": "Default__Contract_Spray_Pandemic02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Viper Spray",
            "ID": "A7211B33-4388-5FD1-6B63-7FB3BC814C5C",
            "AssetName": "Default__Spray_ViperCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Phoenix Spray",
            "ID": "8AC8F9D1-4951-631C-E49D-5FB8DB88AF73",
            "AssetName": "Default__Spray_PhoenixCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Claim the Crown Spray",
            "ID": "A98DE724-495D-1873-4FD1-47A8588D2712",
            "AssetName": "Default__Spray_Phoenix01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spotlight Spray",
            "ID": "BA2FFEF8-4CA5-5217-C13F-AB8E6248866A",
            "AssetName": "Default__Spray_Phoenix02_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Salt Shaker Spray",
            "ID": "1A4E85A1-4CA6-C95A-93BA-0185D321380A",
            "AssetName": "Default__Spray_Salt_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Brimstone Spray",
            "ID": "D11A4A44-4EDB-CB49-46E9-93A7FB8BD02C",
            "AssetName": "Default__Spray_BrimstoneCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Big One Spray",
            "ID": "8DBD1739-4706-CA30-E907-CDB400F76CBA",
            "AssetName": "Default__Spray_Sarge01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Getting Reps  Spray",
            "ID": "27D9D9DF-4778-58BB-0514-1E922861C30E",
            "AssetName": "Default__Spray_Sarge02_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Spray",
            "ID": "667D3DF4-4786-4A65-B9A4-BCBCD8ED5EED",
            "AssetName": "Default__Spray_Cyberpunk_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Spray",
            "ID": "088D2BEE-462C-6FD1-0F0F-7CB24F8733AE",
            "AssetName": "Default__Edge_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Spray",
            "ID": "FBFDC963-487E-D666-4F36-0D9CE8D62719",
            "AssetName": "Default__Gothic_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Spray",
            "ID": "7AD4A4C5-48A0-B195-234F-A4A4C213915F",
            "AssetName": "Default__Spray_MagicSpline_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Spray",
            "ID": "23C475E1-4DA7-D32E-BC69-41A4899F4326",
            "AssetName": "Default__Oblivion_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Spray",
            "ID": "135164B6-4295-27B2-34D8-59A95C93E025",
            "AssetName": "Default__Oni_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Spray",
            "ID": "92D7A963-44AE-41C9-3D1B-B58C36EECD96",
            "AssetName": "Default__Raygun_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Spray",
            "ID": "8CE1DB32-4047-8BCD-1E38-9F9991AA0B6B",
            "AssetName": "Default__SoulStealer_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Spray",
            "ID": "CFB0B5E4-4B0A-C150-09A9-12ABEA8A407E",
            "AssetName": "Default__Unstoppable_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Spray",
            "ID": "8A017CE8-430C-4B97-FCC6-178B79BB2800",
            "AssetName": "Default__Spray_Sovereign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Clip It Spray",
            "ID": "457B5D43-4199-AE99-6866-A8A7342393BE",
            "AssetName": "Default__Spray_ClipIt_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Tactibear Spray",
            "ID": "406CB253-4823-872A-EA7D-BCBA8378499A",
            "AssetName": "Default__Spray_Tactibear_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sage Spray",
            "ID": "BD53185F-4EE6-6D29-CA98-7ABE45401482",
            "AssetName": "Default__Spray_SageCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "All Good Spray",
            "ID": "DEE0CE8B-4E71-CC06-6908-228411DE4C65",
            "AssetName": "Default__Spray_Thorne01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pulse Check Spray",
            "ID": "28B0DA71-4D01-825C-A7D5-D480F5D37CA7",
            "AssetName": "Default__Spray_Thorne03_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "V for VALORANT Spray",
            "ID": "280B9B3F-4BFA-9CF5-C72B-78AB277C30E7",
            "AssetName": "Default__Spray_VALLogoNPE_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reyna Spray",
            "ID": "D04D33F8-48CF-112F-F6AA-62AEA1F7FB27",
            "AssetName": "Default__Spray_ReynaCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Leer Spray",
            "ID": "3B7CB17D-4112-7BA3-16AC-72A9FE512BA0",
            "AssetName": "Default__Spray_Vampire01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Marked for Death Spray",
            "ID": "BFBDDA43-429C-047A-EA8C-F2BFCBA1E5C1",
            "AssetName": "Default__Spray_Vampire02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vandal Life Spray",
            "ID": "2DB70E75-4601-7480-9481-479C090B9FCA",
            "AssetName": "Default__Spray_WeaponStencil_Act1BP_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Omen Spray",
            "ID": "2060FA45-4769-B918-84F9-7FBBB1856546",
            "AssetName": "Default__Spray_OmenCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "It Hunts Spray",
            "ID": "3598B7CB-5971-4BC8-BB6B-1A0531BD7387",
            "AssetName": "Default__Contract_Spray_Wraith01_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dark Focus Spray",
            "ID": "9039DD65-27AF-4871-B884-B8F338CF53F5",
            "AssetName": "Default__Contract_Spray_Wraith02_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jett Spray",
            "ID": "0A70FA83-4DB6-354E-63B0-94A2464E4F9E",
            "AssetName": "Default__Spray_JettCallsign_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Watch This Spray",
            "ID": "E4F297C4-4F25-4C76-B39F-08B5CCB0D5E9",
            "AssetName": "Default__Spray_Wushu01_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "You Better Run Spray",
            "ID": "0A759889-4C6A-7920-49ED-A4A1D2F856CA",
            "AssetName": "Default__Spray_Wushu02_Lv1_Level1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Charms": [
        {
            "Name": "In A Bind Buddy",
            "ID": "D6F5E6A4-4D42-B56D-03C3-92955D294F54",
            "AssetName": "Default__GunBuddy_BindDiorama_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hammer Time Buddy",
            "ID": "8FBF09A5-4AD2-46CA-D44E-26B46587A1BF",
            "AssetName": "Default__GunBuddy_Breach_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bullet Buddy",
            "ID": "FEDCEFF5-4A3E-0506-DBC0-8BA5B9CFD171",
            "AssetName": "Default__GunBuddy_Bullet01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Closed Beta Coin Buddy",
            "ID": "57BC159C-4BF9-1963-884A-A387E69013BE",
            "AssetName": "Default__GunBuddy_CB_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Blast Pin Buddy",
            "ID": "99813567-4B6A-47C2-D36F-0BA5BC89ADAC",
            "AssetName": "Default__GunBuddy_Clay_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 1 Coin Buddy",
            "ID": "2FE275A6-41F2-BF54-7FB9-7593429EA675",
            "AssetName": "Default__GunBuddy_Coin_EP1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 2 Coin Buddy",
            "ID": "2A1514DD-433D-C2E4-23A0-C1A75CCAE00B",
            "AssetName": "Default__GunBuddy_Coin_EP1_A2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 3 Coin Buddy",
            "ID": "64245BFE-4740-FC95-95A4-81B4EC4D3412",
            "AssetName": "Default__GunBuddy_Coin_EP1_A3_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chilly McFreeze Buddy",
            "ID": "7AC1F7DB-42A7-BF5A-5B13-95B70E618F5E",
            "AssetName": "Default__GunBuddy_CoolSnowman_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Crate Buddy",
            "ID": "E0462E6C-4188-06CC-E28D-AC9ABCC16BC2",
            "AssetName": "Default__GunBuddy_Crate1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Crate Buddy",
            "ID": "0F1CE8CE-4615-637D-6772-0FA15B848FE4",
            "AssetName": "Default__GunBuddy_CrateKingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Buddy",
            "ID": "FE997250-41EF-444A-A12B-7CA8CA87CB40",
            "AssetName": "Default__GunBuddy_CrimsonOps_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cup o' Crown Buddy",
            "ID": "271C1309-4185-D000-C8BF-56A170C17E1C",
            "AssetName": "Default__GunBuddy_CrownCoffee_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Buddy",
            "ID": "C5BEE9F1-4548-03C3-F88D-D7BF38D1943E",
            "AssetName": "Default__GunBuddy_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Danger Lizard Buddy",
            "ID": "D5B10115-43EA-42E7-8843-5BB5C1E73C6E",
            "AssetName": "Default__GunBuddy_DangerLizard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Discotech Buddy",
            "ID": "42AFB96B-4D11-E465-55A4-0B87BDFBF244",
            "AssetName": "Default__GunBuddy_DiscoBall_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Epilogue: Discotech Buddy",
            "ID": "910EA2D6-4578-C826-2B06-1594769766FB",
            "AssetName": "Default__GunBuddy_DiscoBallGold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Donut Buddy",
            "ID": "26D1B452-461D-8D6F-526B-658C692E0F9E",
            "AssetName": "Default__GunBuddy_Doughnut_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Buddy",
            "ID": "38A10A3B-495C-EEFF-B8AF-C3B2B5CDC3F9",
            "AssetName": "Default__GunBuddy_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Buddy",
            "ID": "2DE08C48-4AA1-0C32-138D-4B834C21AEE2",
            "AssetName": "Default__GunBuddy_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ascent Rising Buddy",
            "ID": "0262276C-4EDE-A858-CAD0-1CA4E877052B",
            "AssetName": "Default__GunBuddy_FloatingIsland_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Froggie Hat Buddy",
            "ID": "B45B70FB-49D4-9D7F-AFDE-57A1EA79D9B5",
            "AssetName": "Default__GunBuddy_FroggyHat_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gelato Cutie Buddy",
            "ID": "108A36D5-44EF-9B4C-B783-B29A6A9AE340",
            "AssetName": "Default__GunBuddy_Gelato_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Watcher Buddy",
            "ID": "41859A85-4344-AEEE-483A-468BAD39E5FD",
            "AssetName": "Default__GunBuddy_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hawko Buddy",
            "ID": "E4689A4B-4DF6-86E8-8D34-A19BDC01AFE7",
            "AssetName": "Default__GunBuddy_GuideBird_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "White Hat Buddy",
            "ID": "E058E4F5-40C4-A26A-E6C7-33A4BAF2E21F",
            "AssetName": "Default__GunBuddy_Gumshoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Safe Haven Buddy",
            "ID": "AE240163-4893-5D7E-9029-31A3CA2A9C84",
            "AssetName": "Default__GunBuddy_HavenDiorama_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Owl Charm Buddy",
            "ID": "EBBCED2D-4851-6B5D-FF3F-5BAAEA322DBF",
            "AssetName": "Default__GunBuddy_Hunter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Buddy",
            "ID": "8AC9948E-4C40-BCEC-4F7D-E6BD5C8B349C",
            "AssetName": "Default__GunBuddy_Hypebeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jack O' Lantern Buddy",
            "ID": "E1F62DC9-4BD1-868E-3CA3-F7B51FD325FA",
            "AssetName": "Default__GunBuddy_JackOLantern_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bot Buddy",
            "ID": "12372DBB-4F09-4B26-6FE5-779488AAA9F9",
            "AssetName": "Default__GunBuddy_Killjoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Netter Treter Buddy",
            "ID": "1E909EE9-4AF5-5D50-AA27-2BB596187986",
            "AssetName": "Default__GunBuddy_KilljoySneaker_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GL Have Cat Buddy",
            "ID": "D8C85CAE-44FD-8D97-A948-25ACFE80B109",
            "AssetName": "Default__GunBuddy_LuckyCat_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Buddy",
            "ID": "F696F391-4B0E-804C-0069-02A0D67DD170",
            "AssetName": "Default__GunBuddy_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dallah Buddy",
            "ID": "D12A80C0-44A0-0549-CC1F-EEB83F7AD248",
            "AssetName": "Default__GunBuddy_MenaiPot_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Buddy",
            "ID": "2D28FBC9-4518-3432-D90D-DE8BBA571A93",
            "AssetName": "Default__GunBuddy_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Coin Buddy",
            "ID": "AC72BB9A-4368-8502-5DAC-698D72021C81",
            "AssetName": "Default__GunBuddy_Onboarding_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Buddy",
            "ID": "57639CF0-4B2F-73F6-5C37-FE816FA560DF",
            "AssetName": "Default__GunBuddy_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Venom Vial Buddy",
            "ID": "BC76826C-4AC3-5C94-11AF-1FB97BA3A835",
            "AssetName": "Default__GunBuddy_Pandemic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hot Bling Buddy",
            "ID": "B9FEB6B6-493C-B76E-CE8E-6FB371CA2CF5",
            "AssetName": "Default__GunBuddy_Phoenix_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pizza Buddy",
            "ID": "15BC068C-4B1E-DFBC-CFBB-9283A8D0E0EE",
            "AssetName": "Default__GunBuddy_Pizza_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Buddy",
            "ID": "8BB77C22-4F90-EC3E-A2F7-16A2DDB064B2",
            "AssetName": "Default__GunBuddy_Polyfox_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pay Respects Buddy",
            "ID": "839C6E7D-4821-157B-FD38-71B3DEBC874F",
            "AssetName": "Default__GunBuddy_PressF_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Crystal Buddy",
            "ID": "ABFE3887-40F8-D3C1-08BB-AB89DAE2A399",
            "AssetName": "Default__GunBuddy_RadianiteDiamond_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Buddy",
            "ID": "90356707-45E1-5D0B-2B34-2D9AADF78B4E",
            "AssetName": "Default__GunBuddy_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Immortal Rose Buddy",
            "ID": "1A838FD4-43C3-DAD7-AD30-37B9240C1CE1",
            "AssetName": "Default__GunBuddy_Rose_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dog Tags Buddy",
            "ID": "AFFEE4FE-4B57-DDDD-BEB2-DEAF0A641B25",
            "AssetName": "Default__GunBuddy_Sarge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Buddy",
            "ID": "0EAB96DA-ED34-4BDB-978F-B02B2FB4EBCC",
            "AssetName": "Default__GunBuddy_Soulstealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Buddy",
            "ID": "A8E2DAC4-4BE6-75E7-BF76-1F9B5A6D5FB5",
            "AssetName": "Default__GunBuddy_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Spike Buddy",
            "ID": "0EC28D81-498C-AF58-722C-BAA60A84151C",
            "AssetName": "Default__GunBuddy_Spike_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Split Decision Buddy",
            "ID": "4E32934E-4AE1-2223-B9E4-90BE4BD9677E",
            "AssetName": "Default__GunBuddy_SplitDiorama_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheesed Buddy",
            "ID": "5DE7339F-40FC-DF25-1CF4-D3A5255BA1F7",
            "AssetName": "Default__GunBuddy_SwissCheese_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bear Tactics Buddy",
            "ID": "2FBE33AA-4E7A-B601-5FA8-CE8FB6511113",
            "AssetName": "Default__GunBuddy_Tactibear_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Squirrel Tactics Buddy",
            "ID": "1F99D997-4AFB-EF4C-E754-CAA0BF84FCE1",
            "AssetName": "Default__GunBuddy_Tactisquirrel_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Potato Aim Buddy",
            "ID": "55702E59-4E3F-E2DD-2B31-91B1938CF0E1",
            "AssetName": "Default__GunBuddy_Tader_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Orb Buddy",
            "ID": "CD1EF501-476D-E9FB-3944-A6B0E2A79878",
            "AssetName": "Default__GunBuddy_Thorne_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Toaster Buddy",
            "ID": "22481BD6-45D7-55A9-DB2F-F4A7B86C0D05",
            "AssetName": "Default__GunBuddy_Toaster_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Scuttle Trash Buddy",
            "ID": "476E2D56-46A1-3607-AA61-3487CF9AE80F",
            "AssetName": "Default__GunBuddy_Trash_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Fist Bump Buddy",
            "ID": "AD508AEB-44B7-46BF-F923-959267483E78",
            "AssetName": "Default__GunBuddy_TrashGold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Buddy",
            "ID": "43922614-4FE5-52C9-8D35-689DB5EC4681",
            "AssetName": "Default__GunBuddy_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Wheel of Steel Buddy",
            "ID": "86BBCE95-4B76-C933-9939-9AA0F0F2C169",
            "AssetName": "Default__GunBuddy_ValorantVinyl_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Soul Capsule Buddy",
            "ID": "C4F69DE5-4440-19B5-8953-36B12BA42BB0",
            "AssetName": "Default__GunBuddy_Vampire_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Grim Delight Buddy",
            "ID": "7CF1FC2C-4456-FA8F-B9F6-C9BE7092163F",
            "AssetName": "Default__GunBuddy_Wraith_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pocket Knife Buddy",
            "ID": "A2E04067-4EA8-FF47-BE4A-F780BDF5E1F7",
            "AssetName": "Default__GunBuddy_Wushu_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "CharmLevels": [
        {
            "Name": "In A Bind Buddy",
            "ID": "633F5DEB-41D2-B9D2-B099-0DBBFD7B3A69",
            "AssetName": "Default__GunBuddy_BindDiorama_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hammer Time Buddy",
            "ID": "98A2FA9E-4E66-EEC9-8B13-298498862F28",
            "AssetName": "Default__GunBuddy_Breach_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bullet Buddy",
            "ID": "8BD42B70-4F2F-5C7D-33D3-0F83521C8EB5",
            "AssetName": "Default__GunBuddy_Bullet01_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Closed Beta Coin Buddy",
            "ID": "CC4BE40D-47E0-7F1E-2E30-9B90CE2607CD",
            "AssetName": "Default__GunBuddy_CB_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Blast Pin Buddy",
            "ID": "7D1864A2-4796-AC3C-A49F-7588AE17ED18",
            "AssetName": "Default__GunBuddy_Clay_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 1 Coin Buddy",
            "ID": "96502717-41F7-5D24-89A1-66AFF04BBBBB",
            "AssetName": "Default__GunBuddy_Coin_EP1_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 2 Coin Buddy",
            "ID": "DEEF49C1-432D-10F7-A750-90B323B079D2",
            "AssetName": "Default__GunBuddy_Coin_EP1_A2_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "EP 1 // 3 Coin Buddy",
            "ID": "0BD4E4B8-48BD-DF5A-3AF3-F49ACF7913E1",
            "AssetName": "Default__GunBuddy_Coin_EP1_A3_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chilly McFreeze Buddy",
            "ID": "2179E882-430E-BE93-B909-BBA9568E66AF",
            "AssetName": "Default__GunBuddy_CoolSnowman_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Crate Buddy",
            "ID": "0DF7158A-46C6-EEB6-9561-E78165756B99",
            "AssetName": "Default__GunBuddy_Crate1_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Crate Buddy",
            "ID": "31E2CC61-4D9E-2AA1-FF65-76A7A0A7BBA1",
            "AssetName": "Default__GunBuddy_CrateKingdom_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Red Alert Buddy",
            "ID": "EEA4991C-4B01-9DD1-5D3C-1CBBDC8E1B0B",
            "AssetName": "Default__GunBuddy_CrimsonOps_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cup o' Crown Buddy",
            "ID": "967652C0-48C5-1B18-AE3E-2BB066F2623D",
            "AssetName": "Default__GunBuddy_CrownCoffee_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Buddy",
            "ID": "E6EEE5EC-4F6F-E764-1C4D-048CE271BE27",
            "AssetName": "Default__GunBuddy_Cyberpunk_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Danger Lizard Buddy",
            "ID": "28227664-476A-72DB-ADAA-159084FBD149",
            "AssetName": "Default__GunBuddy_DangerLizard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Discotech Buddy",
            "ID": "682A5C4E-4506-8D3A-82F9-6D87BD000DC7",
            "AssetName": "Default__GunBuddy_DiscoBall_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Epilogue: Discotech Buddy",
            "ID": "8FAE3CCD-44E0-42E6-D60C-A39E1471CDC9",
            "AssetName": "Default__GunBuddy_DiscoBallGold_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Donut Buddy",
            "ID": "F3A3C59B-4BF3-461C-F956-D0BC7D95A742",
            "AssetName": "Default__GunBuddy_Doughnut_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Buddy",
            "ID": "B2128A8C-49BD-09B1-7B4C-F2B9D2F92508",
            "AssetName": "Default__GunBuddy_Dragon_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Buddy",
            "ID": "ED95E342-4116-F07C-88B9-368A5FADB224",
            "AssetName": "Default__GunBuddy_Edge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ascent Rising Buddy",
            "ID": "175D5EA6-43A6-1E39-E720-62805544F5D3",
            "AssetName": "Default__GunBuddy_FloatingIsland_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Froggie Hat Buddy",
            "ID": "6B26E5CA-4187-CB98-B7B2-9280343E32E3",
            "AssetName": "Default__GunBuddy_FroggyHat_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gelato Cutie Buddy",
            "ID": "461EE5BC-4325-67F1-9E3F-42952FB8F898",
            "AssetName": "Default__GunBuddy_Gelato_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Watcher Buddy",
            "ID": "A7555579-4DF9-6916-E15F-8381C11689A9",
            "AssetName": "Default__GunBuddy_Gothic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hawko Buddy",
            "ID": "10D781C0-4500-19EB-5000-C6AFAC6F2C58",
            "AssetName": "Default__GunBuddy_GuideBird_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "White Hat Buddy",
            "ID": "ABD3D1C7-42B6-46FC-35D2-AC9CF1F33607",
            "AssetName": "Default__GunBuddy_Gumshoe_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Safe Haven Buddy",
            "ID": "D606DF6A-4F8A-1273-083A-5B925A178E36",
            "AssetName": "Default__GunBuddy_HavenDiorama_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Owl Charm Buddy",
            "ID": "011602D8-4078-C9B3-8A3E-AC9642D0417C",
            "AssetName": "Default__GunBuddy_Hunter_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Buddy",
            "ID": "80BBCDFF-4B2C-2370-0806-498C0F4E1D06",
            "AssetName": "Default__GunBuddy_Hypebeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Jack O' Lantern Buddy",
            "ID": "EAF6E89A-46B6-83E3-2EFB-EDA4B0F3DD86",
            "AssetName": "Default__GunBuddy_JackOLantern_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bot Buddy",
            "ID": "F14D17FD-42A2-946F-21FB-1A815A6837BC",
            "AssetName": "Default__GunBuddy_Killjoy_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Netter Treter Buddy",
            "ID": "5B863CB9-4E41-EC89-69EE-49A223D05FF1",
            "AssetName": "Default__GunBuddy_KilljoySneaker_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "GL Have Cat Buddy",
            "ID": "6F7B0B5B-470D-77B0-BD0D-7781CE5FDF07",
            "AssetName": "Default__GunBuddy_LuckyCat_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Buddy",
            "ID": "EC3745C4-432A-8173-8150-CFBB4841C121",
            "AssetName": "Default__GunBuddy_MagicSpline_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dallah Buddy",
            "ID": "6FC24467-43FD-7C59-A531-94A1DB4FDF75",
            "AssetName": "Default__GunBuddy_MenaiPot_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Buddy",
            "ID": "5DCDC42B-4398-0A62-1351-9B8CFDD2892C",
            "AssetName": "Default__GunBuddy_Oblivion_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Coin Buddy",
            "ID": "4B5417ED-49DE-7076-E0FB-12A5B43957CE",
            "AssetName": "Default__GunBuddy_Onboarding_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Buddy",
            "ID": "D59590FA-4389-125A-6C53-C7BD026ACB01",
            "AssetName": "Default__GunBuddy_Oni_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Venom Vial Buddy",
            "ID": "B0E1C557-4C45-BDC7-3E02-1FACC7B19182",
            "AssetName": "Default__GunBuddy_Pandemic_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hot Bling Buddy",
            "ID": "EC22D3C1-4DF0-F0FE-A424-359627FB83FF",
            "AssetName": "Default__GunBuddy_Phoenix_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pizza Buddy",
            "ID": "AA3661F1-4EEF-E8DD-047B-E5B9ED61403B",
            "AssetName": "Default__GunBuddy_Pizza_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Buddy",
            "ID": "456A7D74-4CF8-5CF7-7801-F2A0265DA233",
            "AssetName": "Default__GunBuddy_Polyfox_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pay Respects Buddy",
            "ID": "56F98991-43F8-DCC8-189E-08B7AE6C42AD",
            "AssetName": "Default__GunBuddy_PressF_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Crystal Buddy",
            "ID": "77DC86DC-4D9C-DF35-3921-D18D32355824",
            "AssetName": "Default__GunBuddy_RadianiteDiamond_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Buddy",
            "ID": "2484E328-45E9-A5C0-960F-AD8B0F620D0E",
            "AssetName": "Default__GunBuddy_Raygun_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Immortal Rose Buddy",
            "ID": "9EA89EC3-4CB5-40F1-27AF-F3983AF8AB4D",
            "AssetName": "Default__GunBuddy_Rose_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Dog Tags Buddy",
            "ID": "A72A5CD8-4010-8E76-7F72-E1BDF663FA1C",
            "AssetName": "Default__GunBuddy_Sarge_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Buddy",
            "ID": "F344BEAD-BB25-4226-A990-B5D9694D475D",
            "AssetName": "Default__GunBuddy_Soulstealer_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Buddy",
            "ID": "547C3AA6-4E86-199C-B190-01B75287F30B",
            "AssetName": "Default__GunBuddy_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Spike Buddy",
            "ID": "F7626CD3-411C-A4E6-754B-EB8EE06C8377",
            "AssetName": "Default__GunBuddy_Spike_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Split Decision Buddy",
            "ID": "45DB2427-4FEC-75E1-DA50-D286048DAD53",
            "AssetName": "Default__GunBuddy_SplitDiorama_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Cheesed Buddy",
            "ID": "E88F43B7-4B9A-1050-C1E7-D883A8F706F2",
            "AssetName": "Default__GunBuddy_SwissCheese_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bear Tactics Buddy",
            "ID": "5224EEAF-4387-0750-EB5C-0DA41A9B243C",
            "AssetName": "Default__GunBuddy_Tactibear_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Squirrel Tactics Buddy",
            "ID": "0B3F4807-4B50-2379-9690-398AF0041DCA",
            "AssetName": "Default__GunBuddy_Tactisquirrel_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Potato Aim Buddy",
            "ID": "DA8B0232-4AC3-FBEC-9355-EF81DB0E7437",
            "AssetName": "Default__GunBuddy_Tader_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Orb Buddy",
            "ID": "45D9B8F8-41A6-0FF5-01EB-7987FB000D31",
            "AssetName": "Default__GunBuddy_Thorne_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Toaster Buddy",
            "ID": "7944B081-4B0F-81C8-E41F-3AA5C634B782",
            "AssetName": "Default__GunBuddy_Toaster_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Scuttle Trash Buddy",
            "ID": "00F129A0-47F3-27A8-5D5B-9FB07CE39A05",
            "AssetName": "Default__GunBuddy_Trash_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Fist Bump Buddy",
            "ID": "A57AA3D0-4AD0-B06A-6C54-338CB3EA6B41",
            "AssetName": "Default__GunBuddy_TrashGold_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Buddy",
            "ID": "D3759A6A-4D5C-A322-092F-7290B52566EF",
            "AssetName": "Default__GunBuddy_Unstoppable_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Wheel of Steel Buddy",
            "ID": "B318AF9C-4DB8-E0CF-8BB1-BEA643B1AA9C",
            "AssetName": "Default__GunBuddy_ValorantVinyl_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Soul Capsule Buddy",
            "ID": "9A53CF84-4303-C623-B733-5787F8661404",
            "AssetName": "Default__GunBuddy_Vampire_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Grim Delight Buddy",
            "ID": "CF194771-4EB6-053E-6C0C-5A80DAB14F39",
            "AssetName": "Default__GunBuddy_Wraith_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pocket Knife Buddy",
            "ID": "CBC43EAC-44F5-9BD6-F0DD-40954A12B709",
            "AssetName": "Default__GunBuddy_Wushu_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "PlayerCards": [
        {
            "Name": "The Way Forward Card",
            "ID": "33C1F011-4ECA-068C-9751-F68C788B2EEE",
            "AssetName": "Default__Playercard_Birb_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hivemind Card",
            "ID": "FC209787-414B-10D0-DCAC-04832FC2C654",
            "AssetName": "Default__Playercard_ExoAltUniverse_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VERSUS // Phoenix + Jett Card",
            "ID": "3432DC3D-47DA-4675-67AE-53ADB1FDAD5E",
            "AssetName": "Default__Playercard_JettPhoenix_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Judge Schema Card",
            "ID": "59939BEA-4B82-9CE0-0586-D4B0C8D5271D",
            "AssetName": "Default__Playercard_JudgeSchema_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Killjoy ID Card",
            "ID": "55F584F9-4684-895D-88E0-A8ADA2002D8A",
            "AssetName": "Default__Playercard_KilljoyID_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chicken Noir Card",
            "ID": "FCA32892-4F2F-228B-0F5C-209AD50199B3",
            "AssetName": "Default__Playercard_MissingChicken_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Odin Schema Card",
            "ID": "ADBD4077-4F0F-57C7-D9CD-7E9BC4244646",
            "AssetName": "Default__Playercard_OdinSchema_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "POLYfox Card",
            "ID": "30B64514-440D-1261-F863-6BBB180263F9",
            "AssetName": "Default__Playercard_PolyfoxAltUniverse_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Experiment X011 Card",
            "ID": "D2B288EA-4DC9-0B3B-FC8C-3BAEC575F0F8",
            "AssetName": "Default__Playercard_RadianiteLab_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Epoch Event Card",
            "ID": "5ED8F14B-4C05-9E34-A0DD-878133823928",
            "AssetName": "Default__Playercard_SpikeExplosion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vandal Schema Card",
            "ID": "F951D97C-4ABB-0775-2312-4DB199CDE6BF",
            "AssetName": "Default__Playercard_VandalSchema_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pigs May Fly Card",
            "ID": "16939544-4F84-C889-545E-659E071FF3F8",
            "AssetName": "Default__Playercard_WhenPigsEscape_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ancient Secrets Card",
            "ID": "475CE7C1-4DDC-63AA-7E22-54BB621D615B",
            "AssetName": "Default__Playercard_AncientSecrets_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Holidaze Card",
            "ID": "22888904-4274-C5FB-AC4F-0E8A39A9417E",
            "AssetName": "Default__Playercard_AustralianWinter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bucky Schema Card",
            "ID": "48ED2529-4295-C37A-EAA1-15A1C4137ABE",
            "AssetName": "Default__Playercard_BuckySchema_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ghost Schema Card",
            "ID": "FE84218F-4338-0F85-62CD-DFA5596576A0",
            "AssetName": "Default__Playercard_GhostSchema_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Skye ID Card",
            "ID": "9397E078-4140-CC2B-4FCD-B0AFEDB9ECE8",
            "AssetName": "Default__Playercard_GuideJoins_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "MEMENTO MORI Card",
            "ID": "C0B560FC-4140-9BF1-DAEE-4DA652B824C5",
            "AssetName": "Default__Playercard_MementoMori_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Radianite Hazard Card",
            "ID": "B79B6DAC-4D30-7A76-5710-C0873224F31B",
            "AssetName": "Default__Playercard_RadianiteFormula_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VERSUS // Raze + Killjoy Card",
            "ID": "7AA1A5FB-4AE3-9A3B-AE04-05BD9FC02413",
            "AssetName": "Default__Playercard_RazeKilljoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALOR-ANT Card",
            "ID": "A80D8898-464D-1B63-4B1B-149930C22B6B",
            "AssetName": "Default__Playercard_VALORAnt_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VERSUS // Vandal + Phantom Card",
            "ID": "D14C070E-4F7A-8AB1-350E-199AF481D32A",
            "AssetName": "Default__Playercard_VandalvsPhantom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Epilogue: VERSUS // Vandal + Phantom Card",
            "ID": "F0196638-47A9-C2DA-7665-F599E3D930AD",
            "AssetName": "Default__Playercard_VandalvsPhantom_Gold_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Secret Lineage Card",
            "ID": "F32EB1E5-4CD3-0520-88A3-0CAFB7423002",
            "AssetName": "Default__Playercard_Woah_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Card",
            "ID": "9FB348BC-41A0-91AD-8A3E-818035C4E561",
            "AssetName": "Default__Playercard_Default_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "MMXX Founder Card",
            "ID": "5AAA58D8-4567-DC02-DC74-FBAA957FA7CD",
            "AssetName": "Default__Playercard_Founder_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Vertraulich Card",
            "ID": "51DCF475-4078-2DCE-883B-48BB77670EA8",
            "AssetName": "Default__Playercard_KJ_Tease_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Looking For Group Card",
            "ID": "CD5E4A23-4A0B-0F31-D87A-A1A2EC3301F4",
            "AssetName": "Default__Playercard_LFG_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reyna ID Card",
            "ID": "1FB0BEE0-49DB-FB51-B090-BC834BABDB2B",
            "AssetName": "Default__Playercard_Reyna_Joins_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Beta Card",
            "ID": "EFAF392A-412D-0D4F-4413-DDBDB70D841D",
            "AssetName": "Default__PlayerCard_CBBase_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Beta Pioneer Card",
            "ID": "D29E6E34-44BD-21C8-F7BB-B0A73F267E50",
            "AssetName": "Default__PlayerCard_CBUpgrade_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Beta Watch Card",
            "ID": "E6529E9C-4A2B-C31C-7252-E185A8CE4A04",
            "AssetName": "Default__Playercard_Watcher_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Breach Card",
            "ID": "E99656DF-BBB0-4DB4-867B-29A31CBE2E51",
            "AssetName": "Default__Playercard_Breach_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Big PayDay Card",
            "ID": "E84C7C83-F430-4D6F-B14B-BFDCCD80670A",
            "AssetName": "Default__Playercard_Breach_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Brimstone Card",
            "ID": "9740DDF5-0F1E-46C3-BE8C-01B319680278",
            "AssetName": "Default__Playercard_Brimstone_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "No One Left Behind Card",
            "ID": "109EA8C8-B372-4FE0-BE3C-A5C3E549B38A",
            "AssetName": "Default__Playercard_Brimstone_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Cypher Card",
            "ID": "58314922-434E-6ED6-0625-CC9E137F7EA0",
            "AssetName": "Default__Playercard_Cypher_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Redeemer's Folly Card",
            "ID": "87A0D13A-40E8-78FA-096E-06B41BCEEF2A",
            "AssetName": "Default__PlayerCard_Cypher_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Skye Card",
            "ID": "1F28AC65-411D-619A-ED18-5CAFDA3ACBA7",
            "AssetName": "Default__Playercard_Guide01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "The Great Reclaimer Card",
            "ID": "3BE2322E-4464-66EC-B6CE-C0875F543EE6",
            "AssetName": "Default__Playercard_Guide02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Jett Card",
            "ID": "AB5A453A-F726-4E04-B277-F30D56A8B152",
            "AssetName": "Default__Playercard_Jett_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Mirrored Edge Card",
            "ID": "24E9C88C-4EE1-82FC-2048-BB8942F2147D",
            "AssetName": "Default__Playercard_Jett_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nächtelang Card",
            "ID": "FDF9018A-4A1D-FDFD-7553-009A31C612C5",
            "AssetName": "Default__Playercard_KilljoyCard2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Killjoy Card",
            "ID": "E9021053-495A-E500-9F57-B59F2F94D01B",
            "AssetName": "Default__Playercard_Killjoy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Omen Card",
            "ID": "504F38E4-4874-845C-CCB6-A3AEC7A3A1EB",
            "AssetName": "Default__Playercard_Omen_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "What's Another Death Card",
            "ID": "0166F094-4274-87C3-69E6-368171133181",
            "AssetName": "Default__Playercard_Omen_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Phoenix Card",
            "ID": "BA3F6DEA-9040-4014-B44E-2A856E030F8F",
            "AssetName": "Default__Playercard_Phoenix_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Firestarter Card",
            "ID": "7C7BECB5-A6B4-4B48-AD20-5A816FBC5750",
            "AssetName": "Default__Playercard_Phoenix_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Raze Card",
            "ID": "FBE4935E-421D-4D5D-9EA8-3FB5218D1D1D",
            "AssetName": "Default__Playercard_Raze_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Rising up Card",
            "ID": "3C253E84-4BA8-8892-4C6E-7BA93CFC3D6E",
            "AssetName": "Default__Playercard_Raze_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Reyna Card",
            "ID": "E9DCC215-4B83-90E4-BA3B-4F8D32568EB6",
            "AssetName": "Default__Playercard_Reyna_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Revenge for Life Card",
            "ID": "7D6DA166-42FC-63B2-2913-91A1CD89571C",
            "AssetName": "Default__Playercard_Reyna_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Sage Card",
            "ID": "910ACE70-4D3B-3C53-2C55-5F9FA179CAA8",
            "AssetName": "Default__Playercard_Sage_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Journey of Trials Card",
            "ID": "5A33D85C-42C9-9B75-44C3-E0A447A8A894",
            "AssetName": "Default__Playercard_Sage_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Sova Card",
            "ID": "B03E3577-4F31-AE08-B9B7-4EB587FD13C3",
            "AssetName": "Default__Playercard_Sova_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Through The Looking Glass Card",
            "ID": "91439DFC-4C11-2983-FF5B-0CB5730B7606",
            "AssetName": "Default__Playercard_Sova_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Viper Card",
            "ID": "2F7FD4ED-4B6B-B3FC-0658-18A58F61581B",
            "AssetName": "Default__Playercard_Viper_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "One Dark Night Card",
            "ID": "69265FA9-4C85-E728-D332-4A84857FD84E",
            "AssetName": "Default__Playercard_Viper_2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ascent Card",
            "ID": "A40F0146-4420-645D-6D53-73A362900AF0",
            "AssetName": "Default__Playercard_Ascent_1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "MMXX EP1 Card",
            "ID": "D1C85A2E-450D-F7E0-6EE3-469295CF1951",
            "AssetName": "Default__Playercard_Commemorative_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Mascot Card",
            "ID": "E6A07A97-4C48-421F-515E-288379F7A5BE",
            "AssetName": "Default__Playercard_Corgi_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "What Ancient Mystery Card",
            "ID": "3D1E445F-41C6-71A2-4D60-0790DBE97F64",
            "AssetName": "Default__Playercard_Octopus_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Card",
            "ID": "D93AD22D-4DB7-B6BC-5E9C-E5959BB9DD76",
            "AssetName": "Default__Playercards_Prime_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "New Recruit Card",
            "ID": "612CD02D-4294-EE2A-644C-A3BA3DDF8805",
            "AssetName": "Default__Playercard_Rookie_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Card",
            "ID": "52D88ADD-4269-97C1-FDE3-36BCAC1A436A",
            "AssetName": "Default__PlayerCards_Sovereign_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Showdown Watch Card",
            "ID": "E17C2E94-44FB-9486-8497-9DAB8B942B3D",
            "AssetName": "Default__Playercard_AfreecaTV_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "V Protocol Card",
            "ID": "0819FBCD-4BD4-C379-5384-52803440F2B2",
            "AssetName": "Default__PlayerCard_NPE01_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Code Red Card",
            "ID": "C89194BD-4710-B54E-8D6C-60BE6274FBB2",
            "AssetName": "Default__PlayerCard_NPE02_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "VALORANT Dawn Card",
            "ID": "C8C31580-4315-967B-998B-DFA377BB8843",
            "AssetName": "Default__PlayerCard_NPE03_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop Card",
            "ID": "DF3ADF8C-4FA3-5F57-544D-EABF8B68713D",
            "AssetName": "Default__Playercard_Cyberpunk_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame Card",
            "ID": "6E3D1CD3-4494-8B21-CBC7-0797E8DE75DB",
            "AssetName": "Default__Playercard_Dragon_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity Card",
            "ID": "0ABECAC7-411F-71C0-9504-2D81DF0ACD71",
            "AssetName": "Default__Playercard_Edge_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ruin Card",
            "ID": "0E28A9B5-4A9A-BF7D-B4A1-9B8395461B77",
            "AssetName": "Default__Playercard_Gothic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline Card",
            "ID": "1D0FE8D7-42DD-6F77-50B0-798D1FF90BEF",
            "AssetName": "Default__Playercard_MagicSpline_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion Card",
            "ID": "5FF3A862-4E89-84DD-6E47-BDA2CD2A5CEC",
            "AssetName": "Default__Playercard_Oblivion_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni Card",
            "ID": "AECA98DB-4737-5E0F-3476-7EB8A16EB696",
            "AssetName": "Default__Playercard_Oni_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster Card",
            "ID": "C2F90C55-49BE-93A5-DAF4-6393D9D3F6FC",
            "AssetName": "Default__Playercard_Raygun_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver Card",
            "ID": "8BBDC250-4FFC-F6BA-61A0-0D84C4756A4E",
            "AssetName": "Default__Playercard_SoulStealer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego Card",
            "ID": "8EDF22C5-4489-AB41-769A-07ADB4C454D6",
            "AssetName": "Default__Playercard_Unstoppable_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Classic Schema Card",
            "ID": "86CA5EF3-4F3F-97E7-0F9C-8AA2E9166A7F",
            "AssetName": "Default__Playercard_Classic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "OP Schema Card",
            "ID": "086ACC73-4C6A-26D4-5DA6-A2ADE411897C",
            "AssetName": "Default__Playercard_Operator_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spectre Schema Card",
            "ID": "A75C951F-4822-F85D-44ED-709E413AA5F8",
            "AssetName": "Default__Playercard_Spectre_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "PlayerTitles": [
        {
            "Name": "All Star",
            "ID": "96BBED0E-426E-2F54-8CE1-FF820CA6B703",
            "AssetName": "Default__PlayerTitle_AllStar_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ascendant",
            "ID": "0210A31E-41A0-6150-EE41-BD9D727B629B",
            "AssetName": "Default__PlayerTitle_Ascendant_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ballistic",
            "ID": "BF25C13B-4F89-1AB5-4455-53B34B9763F0",
            "AssetName": "Default__PlayerTitle_Ballistic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Biohazard",
            "ID": "887D1BC0-43B4-C084-4723-E0963A491722",
            "AssetName": "Default__PlayerTitle_Biohazard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Catastrophic",
            "ID": "0EC01B3E-4822-D882-7E6E-E9A0B47CD8BB",
            "AssetName": "Default__PlayerTitle_Catastrophic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Coach",
            "ID": "13B4C766-4F55-11F2-CDE3-ADABABE50C7D",
            "AssetName": "Default__PlayerTitle_Coach_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Concussive",
            "ID": "E5B82CBF-409E-AF39-A6F8-6DADF336DEDB",
            "AssetName": "Default__PlayerTitle_Concussive_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Deadeye",
            "ID": "E4BDB590-4888-86AA-A259-BEBDB52FCBE7",
            "AssetName": "Default__PlayerTitle_Deadeye_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": " ",
            "ID": "D13E579C-435E-44D4-CEC2-6EAE5A3C5ED4",
            "AssetName": "Default__PlayerTitle_Default_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Empress",
            "ID": "86375046-4F22-9DC8-F8D8-B3B4D029CD4B",
            "AssetName": "Default__PlayerTitle_Empress_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Enlightened",
            "ID": "37121E2F-43F6-0B7D-FDC4-29B85F3121C9",
            "AssetName": "Default__PlayerTitle_Enlightened_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "First",
            "ID": "86BD997D-4E37-18C9-ADA0-BF92E54BAF60",
            "AssetName": "Default__PlayerTitle_First_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Flashy",
            "ID": "633BE923-4E83-204F-8DA1-D5930F939369",
            "AssetName": "Default__PlayerTitle_Flashy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Genius",
            "ID": "C3B8609D-46CF-E290-868A-E4852A85704F",
            "AssetName": "Default__PlayerTitle_Genius_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Harbinger",
            "ID": "574B3440-46BD-FEE9-0735-12B4E8A55ACD",
            "AssetName": "Default__PlayerTitle_Harbinger_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hasty",
            "ID": "24E2431E-45B4-EF91-E3F5-F19012522A70",
            "AssetName": "Default__PlayerTitle_Hasty_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "High Command",
            "ID": "7E3A1C4F-4AAE-0569-CD74-A38F3CCE2F51",
            "AssetName": "Default__PlayerTitle_HighCommand_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hotshot",
            "ID": "566B6A77-4F72-AF35-6D17-43BE14E73CB7",
            "AssetName": "Default__PlayerTitle_Hotshot_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hunter",
            "ID": "E1CBD3AA-4156-5330-20C4-E4B95A236DC2",
            "AssetName": "Default__PlayerTitle_Hunter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Hurricane",
            "ID": "475467AE-4A07-41E7-DF1E-699CC239FBD1",
            "AssetName": "Default__PlayerTitle_Hurricane_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Mind Thief",
            "ID": "32087E8B-4260-37AF-F865-5AA64D79F916",
            "AssetName": "Default__PlayerTitle_MindThief_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nature's Wrath",
            "ID": "42E5678C-4FFD-C1A1-71AB-568DB7AF918A",
            "AssetName": "Default__PlayerTitle_NaturesWrath_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Old Dog",
            "ID": "224F0E96-475D-165D-3CA6-8481A4CB7629",
            "AssetName": "Default__PlayerTitle_OldDog_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Recruit",
            "ID": "D873AEF3-49BE-277D-7966-D0A2D9D9AD22",
            "AssetName": "Default__PlayerTitle_Recruit_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Revenant",
            "ID": "E23EAF20-4FB2-5C01-03B0-4FA7F14FBFBD",
            "AssetName": "Default__PlayerTitle_Revenant_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Savage",
            "ID": "82DE085A-4C2B-DA95-A139-048E4CE83DAE",
            "AssetName": "Default__PlayerTitle_Savage_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sharpshooter",
            "ID": "B957C1F1-4784-F202-9BEE-8598EBAA8BAD",
            "AssetName": "Default__PlayerTitle_Sharpshooter_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Swift",
            "ID": "533B2A28-4638-F8CC-5AAE-28A9A9AF5A69",
            "AssetName": "Default__PlayerTitle_Swift_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Techie",
            "ID": "AF20BDD6-4829-2DEE-1BD3-77A34B6E2E9E",
            "AssetName": "Default__PlayerTitle_Techie_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Toxic",
            "ID": "58DBC4AF-4BAF-BD4B-7084-9F92485B4006",
            "AssetName": "Default__PlayerTitle_Toxic_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Trailblazer",
            "ID": "189F8454-45F8-0A74-4B25-77AAE468AC02",
            "AssetName": "Default__PlayerTitle_Trailblazer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "V1.0",
            "ID": "E3CA05A4-4E44-9AFE-3791-7D96CA8F71FA",
            "AssetName": "Default__PlayerTitle_V1dot0_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Warden",
            "ID": "3AEBCA82-4877-BFA9-B215-8E8E3E5DEDC7",
            "AssetName": "Default__PlayerTitle_Warden_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Warhead",
            "ID": "503810E1-44F2-7CE9-5226-9398E60557DE",
            "AssetName": "Default__PlayerTitle_Warhead_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Watchdog",
            "ID": "BEC998EE-416D-BA4A-8AFB-A4BA38C9E228",
            "AssetName": "Default__PlayerTitle_Watchdog_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Catalyst",
            "ID": "A65074FD-4937-734E-20FE-3CAFA842C631",
            "AssetName": "Default__PlayerTitle_Catalyst_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Chicken",
            "ID": "2D284B12-4536-1D0E-B08C-E58850B2A76E",
            "AssetName": "Default__PlayerTitle_Chicken_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Foxy",
            "ID": "326C3796-43C0-4ACA-CD5E-53B3CCF8C507",
            "AssetName": "Default__PlayerTitle_Foxy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Bait",
            "ID": "DC75C976-4A9A-97F0-A94D-42BD5F5E262F",
            "AssetName": "Default__PlayerTitle_Bait_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Pumped",
            "ID": "349D430A-445F-C87E-CC8D-38BC2A86213A",
            "AssetName": "Default__PlayerTitle_Pumped_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spicy",
            "ID": "5DC79611-42F8-24AD-9F5D-6D8288A7FE9A",
            "AssetName": "Default__PlayerTitle_Spicy_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "CB RECRUIT",
            "ID": "DDC0343A-4D1F-F604-0736-C8BAE2AB47FF",
            "AssetName": "Default__PlayerTitle_CBRecruit_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "V1.0",
            "ID": "827243E3-4163-0EFC-68C5-B592D5E9C110",
            "AssetName": "Default__PlayerTitle_CBVet_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ascending",
            "ID": "BBDDCEFA-4F2C-8444-F3CB-8D984E12A874",
            "AssetName": "Default__PlayerTitle_Episode1-1_Ascending_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Day One",
            "ID": "631F4283-48B1-1855-D646-5E8F80E29821",
            "AssetName": "Default__PlayerTitle_Episode1-1_DayOne_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Lone Wolf",
            "ID": "00D4D326-4EDC-3229-7C28-129D3374E3AD",
            "AssetName": "Default__PlayerTitle_Episode1-1_LoneWolf_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Team Player",
            "ID": "9F0EAD27-4925-DB1E-626F-AB95D9C45845",
            "AssetName": "Default__PlayerTitle_Episode1-1_TeamPlayer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "StorefrontItems": [
        {
            "Name": "80",
            "ID": "F86F9999-452B-3D4C-788A-CDA895DDF923",
            "AssetName": "Default__StorefrontItem_UpgradeTokens_Large_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "40",
            "ID": "9483B151-4F66-298B-FB32-B58224324E67",
            "AssetName": "Default__StorefrontItem_UpgradeTokens_Medium_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "20",
            "ID": "187C8A5E-47DE-F4CA-B02B-7697611CFF5B",
            "AssetName": "Default__StorefrontItem_UpgradeTokens_Small_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Avalanche",
            "ID": "0DEE7EF6-D3EA-400A-B15C-5B9524243439",
            "AssetName": "Default__StorefrontItem_AvalancheThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Nebula",
            "ID": "C520FBB0-492C-960E-8B77-F69FC4CE1838",
            "AssetName": "Default__StorefrontItem_CosmosThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Glitchpop",
            "ID": "05E8ADD9-404D-5D37-8973-9F93F8880E2D",
            "AssetName": "Default__StorefrontItem_CyberpunkThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Elderflame",
            "ID": "1BA50CF0-46DD-848F-13A9-DC92FB0A3E3B",
            "AssetName": "Default__StorefrontItem_DragonThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Singularity",
            "ID": "EF72E3C0-467B-AB15-076A-1E9690D16D6F",
            "AssetName": "Default__StorefrontItem_EdgeThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime",
            "ID": "2116A38E-4B71-F169-0D16-CE9289AF4BFA",
            "AssetName": "Default__StorefrontItem_HypebeastThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prism",
            "ID": "CE6C1FA1-4EAE-6DB9-779F-F6988B866DE4",
            "AssetName": "Default__StorefrontItem_IridescenceThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Smite",
            "ID": "ADEC612C-4C82-A4B2-A5F2-B7909E638A67",
            "AssetName": "Default__StorefrontItem_LightningThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe",
            "ID": "1703B166-4E32-63DA-9D16-A7A144AAB574",
            "AssetName": "Default__StorefrontItem_LuxuryThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Spline",
            "ID": "C1B255E2-411D-B159-6DA3-5AB6C011A8CF",
            "AssetName": "Default__StorefrontItem_MagicSplineThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ion",
            "ID": "693D675E-4ED2-C00A-5E38-6B859B275565",
            "AssetName": "Default__StorefrontItem_OblivionThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Oni",
            "ID": "EBFB909D-45BA-C514-3369-55BF014BA293",
            "AssetName": "Default__StorefrontItem_OniThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sensation",
            "ID": "54CBF45C-4B92-5CD9-07AB-3D98175FAFA6",
            "AssetName": "Default__StorefrontItem_RainbowThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Gravitational Uranium Neuroblaster",
            "ID": "E84D5A16-462F-6FBF-BEE0-5A80191A19E5",
            "AssetName": "Default__StorefrontItem_RaygunThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Reaver",
            "ID": "81D85522-4651-4F66-72DE-5FA057B3514C",
            "AssetName": "Default__StorefrontItem_SoulstealerThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign",
            "ID": "FD9FD08F-446F-018F-C632-0E96428F2978",
            "AssetName": "Default__StorefrontItem_SovereignThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Ego",
            "ID": "2D6EC1D9-4152-8A43-5F7F-FF96B29C857F",
            "AssetName": "Default__StorefrontItem_UnstoppableThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Wasteland",
            "ID": "4E3A244B-4482-0541-3EAB-B8912CDB72D6",
            "AssetName": "Default__StorefrontItem_WastelandThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Seasons": [
        {
            "ID": "0df5adb9-4dcb-6899-1306-3e9860661dd3",
            "Name": "Closed Beta",
            "Type": "competitive",
            "StartTime": "2020-04-07T05:15:00Z",
            "EndTime": "2020-05-29T20:14:00Z",
            "IsEnabled": true,
            "IsActive": false,
            "DevelopmentOnly": false
        },
        {
            "ID": "3f61c772-4560-cd3f-5d3f-a7ab5abda6b3",
            "Name": "ACT 1",
            "Type": "competitive",
            "StartTime": "2020-06-01T20:15:00Z",
            "EndTime": "2020-08-04T13:15:00Z",
            "IsEnabled": true,
            "IsActive": false,
            "DevelopmentOnly": false
        },
        {
            "ID": "0530b9c4-4980-f2ee-df5d-09864cd00542",
            "Name": "ACT 2",
            "Type": "competitive",
            "StartTime": "2020-08-04T13:15:00Z",
            "EndTime": "2020-10-13T13:15:00Z",
            "IsEnabled": true,
            "IsActive": false,
            "DevelopmentOnly": false
        },
        {
            "ID": "46ea6166-4573-1128-9cea-60a15640059b",
            "Name": "ACT 3",
            "Type": "competitive",
            "StartTime": "2020-10-13T13:15:00Z",
            "EndTime": "2021-01-12T13:15:00Z",
            "IsEnabled": true,
            "IsActive": true,
            "DevelopmentOnly": false
        }
    ]
}
```
