## ID List
Get all Items, Maps, Attachments, Sprays, GameModes, Charms. Player Cards
URL: `https://shared.na.a.pvp.net/content-service/v2/content`

## Template
Here is how to use `cURL` to get Info on ALL IDS:
- URL: `https://shared.na.a.pvp.net/content-service/v2/content`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`
    - X-Riot-ClientVersion: `CURRENT CLIENT VERSION' [Located Here](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/ClientVersions.md)

## Example
ALL ID's WITHIN 1.01
```
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
            "Name": "Cypher",
            "ID": "117ED9E3-49F3-6512-3CCF-0CADA7E3823B",
            "AssetName": "Default__Gumshoe_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sova",
            "ID": "DED3520F-4264-BFED-162D-B080E2ABCCF9",
            "AssetName": "Default__Hunter_NPE_PrimaryAsset_C",
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
        },
        {
            "Name": "Null UI Data!",
            "ID": "36FB82AF-409D-C0ED-4B49-57B1EB08FBD5",
            "AssetName": "Default__BaseCharacterPrimaryDataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ],
    "Maps": [
        {
            "Name": "Null UI Data!",
            "ID": "7A929CD8-4021-C128-5A21-BC896C1929BA",
            "AssetName": "Default__BaseMapPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
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
            "Name": "dot EXE Odin",
            "ID": "C1ED5BF3-4827-3E3A-EBBB-1BA42A226E59",
            "AssetName": "Default__HeavyMachineGun_Grid_Standard_PrimaryAsset_C",
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
            "Name": "Rush Ares",
            "ID": "D2C1A05E-44CA-5BF9-21AD-48B989E164D2",
            "AssetName": "Default__LightMachineGun_Electroflux_Standard_PrimaryAsset_C",
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
            "Name": "Vandal",
            "ID": "19629AE1-4996-AE98-7742-24A240D41F99",
            "AssetName": "Default__AssaultRifle_AK_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "D2710367-42B2-CF4E-8B87-2F9D09A41261",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_Standard_PrimaryAsset_C",
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
            "Name": "Bulldog",
            "ID": "BF35F404-4A14-6953-CED2-5BAFD21639A0",
            "AssetName": "Default__AssaultRifle_Burst_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Kingdom Phantom",
            "ID": "83697AAA-415D-3EC3-0205-FCAB8DE464D2",
            "AssetName": "Default__AssaultRifle_ACR_Kingdom_Standard_PrimaryAsset_C",
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
            "Name": "Phantom",
            "ID": "52221BA2-4E4C-EC76-8C81-3483506D5242",
            "AssetName": "Default__AssaultRifle_ACR_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Luxe Judge",
            "ID": "5FC0A963-47D1-9336-DDF1-0C99D7169AD8",
            "AssetName": "Default__AutomaticShotgun_Luxury_Standard_PrimaryAsset_C",
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
            "Name": "Rush Frenzy",
            "ID": "1EE55FE2-49B9-67D3-13C3-6CBF7B8A23EF",
            "AssetName": "Default__AutomaticPistol_Electroflux_Standard_PrimaryAsset_C",
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
            "Name": "Galleria Classic",
            "ID": "AB72692D-4447-3CB0-E8A8-30AC11D82213",
            "AssetName": "Default__BasePistol_Murals_Standard_PrimaryAsset_C",
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
            "Name": "Protektor Sheriff",
            "ID": "6671A60E-483F-706A-C59D-0697A1865F60",
            "AssetName": "Default__RevolverPistol_Hunter_Standard_PrimaryAsset_C",
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
            "Name": "Sheriff",
            "ID": "5A59BD61-48A9-AF61-C00F-4AA21DECA9A8",
            "AssetName": "Default__RevolverPistol_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "1CBE1B6F-4914-652C-48D8-8FBB028CEFF0",
            "AssetName": "Default__RevolverPistol_Wushu_Standard_PrimaryAsset_C",
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
            "Name": "Luxe Operator",
            "ID": "6A0320AC-4CFC-C805-F75C-B9879CD842C1",
            "AssetName": "Default__BoltSniper_Luxury_Standard_PrimaryAsset_C",
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
            "Name": "Spectre",
            "ID": "A9AACCCA-4CDC-02EA-1D7E-89BBACECC0E2",
            "AssetName": "Default__SubMachineGun_MP5_Standard_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "C78E4616-4499-7926-0F1E-93977020063F",
            "AssetName": "Default__Vector_ArtDeco_Standard_PrimaryAsset_C",
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
            "Name": "",
            "ID": "D2E296D9-448E-C58F-2229-14A481906686",
            "AssetName": "Default__Melee_Base_HypeBeast_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Melee",
            "ID": "138AE294-4F2E-528A-6601-A69E931BB93F",
            "AssetName": "Default__Melee__Kingdom_Standard_PrimaryAsset_C",
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
            "Name": "Sovereign Melee",
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
        }
    ],
    "Skins": [
        {
            "Name": "dot EXE Odin",
            "ID": "CDA41B87-4D3A-C17C-5F6D-8990CC9C5EFB",
            "AssetName": "Default__HeavyMachineGun_Grid_PrimaryAsset_C",
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
            "Name": "Rush Ares",
            "ID": "4E04647A-4CFC-64F8-4643-F6B7DBCB2943",
            "AssetName": "Default__LightMachineGun_Electroflux_PrimaryAsset_C",
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
            "Name": "Standard Vandal",
            "ID": "27F21D97-4C4B-BD1C-1F08-31830AB0BE84",
            "AssetName": "Default__AssaultRifle_AK_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "C610DBC8-4A90-3C86-7F9E-BFA910F75BB9",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_PrimaryAsset_C",
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
            "Name": "Standard Bulldog",
            "ID": "724A7F42-4315-ECCF-0E76-77BDD3EC2E09",
            "AssetName": "Default__AssaultRifle_Burst_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Kingdom Phantom",
            "ID": "E13AFE1E-4734-2094-FEE8-9DB016E4D54A",
            "AssetName": "Default__AssaultRifle_ACR_Kingdom_PrimaryAsset_C",
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
            "Name": "Standard Phantom",
            "ID": "337CB216-4A6E-D85D-88C2-F29AB317784C",
            "AssetName": "Default__AssaultRifle_ACR_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Luxe Judge",
            "ID": "5237CFCA-4D83-6190-A7F9-D2BDC117EA67",
            "AssetName": "Default__AutomaticShotgun_Luxury_PrimaryAsset_C",
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
            "Name": "Rush Frenzy",
            "ID": "A010C5FC-4343-067D-4DFB-EE836EC0A45F",
            "AssetName": "Default__AutomaticPistol_Electroflux_PrimaryAsset_C",
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
            "Name": "Galleria Classic",
            "ID": "2F9F4637-4377-B55F-97A1-1E8974E29B27",
            "AssetName": "Default__BasePistol_Murals_PrimaryAsset_C",
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
            "Name": "Protektor Sheriff",
            "ID": "4F1FDE01-4130-0AE7-1320-6FB2F2FB6AB9",
            "AssetName": "Default__RevolverPistol_Hunter_PrimaryAsset_C",
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
            "Name": "Standard Sheriff",
            "ID": "1EF6BA68-4DBE-30C7-6BC8-93A6C6F13F04",
            "AssetName": "Default__RevolverPistol_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "121BC438-4748-B2EE-2C58-768C8C26838B",
            "AssetName": "Default__RevolverPistol_Wushu_PrimaryAsset_C",
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
            "Name": "Luxe Operator",
            "ID": "0BD5DA19-491F-DD4A-27E2-C9959B10A87A",
            "AssetName": "Default__BoltSniper_Luxury_PrimaryAsset_C",
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
            "Name": "Standard Spectre",
            "ID": "F01D1307-4299-42F5-2C5E-7DAB7E69AB19",
            "AssetName": "Default__SubMachineGun_MP5_Standard_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "42DA0F19-4017-5CB8-08A4-368315561FDF",
            "AssetName": "Default__Vector_ArtDeco_PrimaryAsset_C",
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
            "Name": "Prime Melee",
            "ID": "E100DFF1-4CF5-54EC-AA65-6FADBC22973B",
            "AssetName": "Default__Melee_Base_HypeBeast_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Melee",
            "ID": "F82AA022-4A6C-FA40-105D-92AF6510AE1B",
            "AssetName": "Default__Melee__Kingdom_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Melee",
            "ID": "4AF88517-4949-9CAA-9DDA-1980F07202A4",
            "AssetName": "Default__Melee_Base_Luxury_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Melee",
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
        }
    ],
    "SkinLevels": [
        {
            "Name": "dot EXE Odin",
            "ID": "49292F21-4F5E-0A1A-3671-54B7CA8FE65A",
            "AssetName": "Default__HeavyMachineGun_Grid_Lv1_PrimaryAsset_C",
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
            "Name": "Rush Ares",
            "ID": "BAD7AE62-4F6A-8974-AB73-7BA6405CA898",
            "AssetName": "Default__LightMachineGun_Electroflux_Lv1_PrimaryAsset_C",
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
            "Name": "Vandal",
            "ID": "1AB72E66-4DA3-33A0-164F-908113E075A4",
            "AssetName": "Default__AssaultRifle_AK_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Bulldog",
            "ID": "3BF9D39F-46B4-BA23-E079-488D799B9416",
            "AssetName": "Default__AssaultRifle_Burst_ArtDeco_Lv1_PrimaryAsset_C",
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
            "Name": "Bulldog",
            "ID": "C8E6AC70-48EF-9D96-D964-A88E8890B885",
            "AssetName": "Default__AssaultRifle_Burst_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Kingdom Phantom",
            "ID": "A7229CBA-4691-62B0-9C40-F59A29817DDC",
            "AssetName": "Default__AssaultRifle_ACR_KingdomLv1_PrimaryAsset_C",
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
            "Name": "Phantom",
            "ID": "871E73ED-452D-EB5A-3D6B-1D87060F35CE",
            "AssetName": "Default__AssaultRifle_ACR_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
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
            "Name": "Luxe Judge",
            "ID": "CFEB4B7A-4310-796C-DB4E-FB9844823992",
            "AssetName": "Default__AutomaticShotgun_Luxury_Lv1_PrimaryAsset_C",
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
            "Name": "Rush Frenzy",
            "ID": "3E32C58E-4347-E4B1-4502-6DAB0DC516A8",
            "AssetName": "Default__AutomaticPistol_Electroflux_Lv1_PrimaryAsset_C",
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
            "Name": "Galleria Classic",
            "ID": "B8BC5D1B-44AA-AA83-0246-B1A6BB496177",
            "AssetName": "Default__BasePistol_Murals_Lv1_PrimaryAsset_C",
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
            "Name": "Protektor Sheriff",
            "ID": "D9FC55C6-4B92-98AC-5052-2A8B5CA4FB71",
            "AssetName": "Default__RevolverPistol_Hunter_Lv1_PrimaryAsset_C",
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
            "Name": "Sheriff",
            "ID": "FEAF05A1-492F-D154-A9F5-0EB1FE9A603E",
            "AssetName": "Default__RevolverPistol_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Game Over Sheriff",
            "ID": "443F5A29-4D5E-D63E-A3C6-ADA7713172FA",
            "AssetName": "Default__RevolverPistol_Wushu_Lv1_PrimaryAsset_C",
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
            "Name": "Luxe Operator",
            "ID": "E5A2E04A-4805-1244-5376-06B40D7C6CBB",
            "AssetName": "Default__BoltSniper_Luxury_Lv1_PrimaryAsset_C",
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
            "Name": "Spectre",
            "ID": "1DC45E18-4A07-C85F-0020-6DA4DB1486CE",
            "AssetName": "Default__SubMachineGun_MP5_Standard_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Aristocrat Stinger",
            "ID": "DF37B069-48B2-0A7C-78EA-5B8EEDC684F7",
            "AssetName": "Default__Vector_ArtDecoLv1_PrimaryAsset_C",
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
            "Name": "Prime Melee",
            "ID": "249B0E46-4A11-F045-51BB-649151CD802A",
            "AssetName": "Default__Melee_Base_HypeBeast_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Prime Melee Level 2",
            "ID": "DF1ACE24-4ACB-E615-24EB-6E95B7E44DC5",
            "AssetName": "Default__Melee_Base_HypeBeast_Lv2_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Kingdom Melee",
            "ID": "8C2E0F93-4277-FBB8-20C6-E2B2638B6ED4",
            "AssetName": "Default__Melee__Kingdom_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Luxe Melee",
            "ID": "E57317AC-4A93-50A9-30E9-93A098513FA9",
            "AssetName": "Default__Melee_Base_Luxury_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Melee",
            "ID": "90FE45D6-41EA-1C49-8FB9-46B0E98C0077",
            "AssetName": "Default__Melee_Base_Sovereign_Lv1_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "Sovereign Melee Level 2",
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
            "ID": "F1278BA5-45C7-E3BC-B239-3D9EE61B989D",
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
            "AssetName": "Default__Attachment_DMR_Reflex_AcogPrimaryAsset_C",
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
            "ID": "F1278BA5-45C7-E3BC-B239-3D9EE61B989D",
            "AssetName": "Default__Attachment_MP5_Silencer_PrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        },
        {
            "Name": "",
            "ID": "F1278BA5-45C7-E3BC-B239-3D9EE61B989D",
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
            "AssetName": "Default__HeavyMachineGunPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Ares",
            "ID": "55D8A0F4-4274-CA67-FE2C-06AB45EFDF58",
            "AssetName": "Default__LightMachineGunPrimaryAsset_C",
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
            "AssetName": "Default__AssaultRifle_BurstPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Phantom",
            "ID": "EE8E8D15-496B-07AC-E5F6-8FAE5D4C7B1A",
            "AssetName": "Default__AssaultRifle_ACRPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Judge",
            "ID": "EC845BF4-4F79-DDDA-A3DA-0DB3774B2794",
            "AssetName": "Default__AutomaticShotgunPrimaryAsset_C",
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
            "AssetName": "Default__AutomaticPistolPrimaryAsset_C",
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
            "AssetName": "Default__LugerPistolPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Sheriff",
            "ID": "E336C6B8-418D-9340-D77F-7A9E4CFE0702",
            "AssetName": "Default__RevolverPistolPrimaryAsset_C",
            "AssetPath": "",
            "IsEnabled": true,
            "BaseContent": true
        },
        {
            "Name": "Shorty",
            "ID": "42DA8CCC-40D5-AFFC-BEEC-15AA47B42EDA",
            "AssetName": "Default__SawedOffShotgunPrimaryAsset_C",
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
            "Name": "Doughnut",
            "ID": "E2C217AC-46DF-20CC-86C0-25B272AB7D3A",
            "AssetName": "Default__Theme_Doughnut_PrimaryAsset_C",
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
            "Name": "FloatingIsland",
            "ID": "9D8CEFA5-4FD7-7AD0-6639-61AE5728FF0C",
            "AssetName": "Default__Theme_FloatingIsland_PrimaryAsset_C",
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
            "Name": "Ice",
            "ID": "13FE8A00-4B7B-7B67-FB79-75B176A32238",
            "AssetName": "Default__Theme_Ice_PrimaryAsset_C",
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
            "Name": "Galleria",
            "ID": "0C4EE4BA-484A-8FD2-E680-AABA9315CEA4",
            "AssetName": "Default__Theme_Murals_PrimaryAsset_C",
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
            "Name": "RadioniteDiamond",
            "ID": "CAB8EC80-4A16-4F53-297F-D3B43FAF6991",
            "AssetName": "Default__Theme_RadioniteDiamond_PrimaryAsset_C",
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
            "Name": "Vampire",
            "ID": "2A5C2836-4F75-0A01-089D-EAAF43CC7D14",
            "AssetName": "Default__Theme_Vampire_PrimaryAsset_C",
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
            "Name": "Lights Out Spray",
            "ID": "9C65BBE6-41DA-C50C-BE81-839214EEDE7C",
            "AssetName": "Default__Spray_LightsOut_Act1BP_PrimaryAsset_C",
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
            "Name": "Sovereign Spray",
            "ID": "D54E0883-4967-5808-E25C-37B3E6313E5C",
            "AssetName": "Default__Spray_Sovereign_PrimaryAsset_C",
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
            "Name": "Null UI Data!",
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
            "Name": "Lights Out Spray",
            "ID": "5C618D37-4959-19B0-4493-F698D330E5EA",
            "AssetName": "Default__Spray_LightsOut_Act1BP_Level1_PrimaryAsset_C",
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
            "Name": "Sovereign Spray",
            "ID": "8A017CE8-430C-4B97-FCC6-178B79BB2800",
            "AssetName": "Default__Spray_Sovereign_Level1_PrimaryAsset_C",
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
            "Name": "EP 1 2020 Coin Buddy",
            "ID": "2FE275A6-41F2-BF54-7FB9-7593429EA675",
            "AssetName": "Default__GunBuddy_Coin_EP1_PrimaryAsset_C",
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
            "Name": "Donut Buddy",
            "ID": "26D1B452-461D-8D6F-526B-658C692E0F9E",
            "AssetName": "Default__GunBuddy_Doughnut_PrimaryAsset_C",
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
            "Name": "White Hat Buddy",
            "ID": "E058E4F5-40C4-A26A-E6C7-33A4BAF2E21F",
            "AssetName": "Default__GunBuddy_Gumshoe_PrimaryAsset_C",
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
            "Name": "GL Have Cat Buddy",
            "ID": "D8C85CAE-44FD-8D97-A948-25ACFE80B109",
            "AssetName": "Default__GunBuddy_LuckyCat_PrimaryAsset_C",
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
            "Name": "Radianite Crystal Buddy",
            "ID": "ABFE3887-40F8-D3C1-08BB-AB89DAE2A399",
            "AssetName": "Default__GunBuddy_RadianiteDiamond_PrimaryAsset_C",
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
            "Name": "Sovereign Buddy",
            "ID": "A8E2DAC4-4BE6-75E7-BF76-1F9B5A6D5FB5",
            "AssetName": "Default__GunBuddy_Sovereign_PrimaryAsset_C",
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
            "Name": "EP 1 2020 Coin Buddy",
            "ID": "96502717-41F7-5D24-89A1-66AFF04BBBBB",
            "AssetName": "Default__GunBuddy_Coin_EP1_Lv1_PrimaryAsset_C",
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
            "Name": "Donut Buddy",
            "ID": "F3A3C59B-4BF3-461C-F956-D0BC7D95A742",
            "AssetName": "Default__GunBuddy_Doughnut_Lv1_PrimaryAsset_C",
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
            "Name": "White Hat Buddy",
            "ID": "ABD3D1C7-42B6-46FC-35D2-AC9CF1F33607",
            "AssetName": "Default__GunBuddy_Gumshoe_Lv1_PrimaryAsset_C",
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
            "Name": "GL Have Cat Buddy",
            "ID": "6F7B0B5B-470D-77B0-BD0D-7781CE5FDF07",
            "AssetName": "Default__GunBuddy_LuckyCat_Lv1_PrimaryAsset_C",
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
            "Name": "Radianite Crystal Buddy",
            "ID": "77DC86DC-4D9C-DF35-3921-D18D32355824",
            "AssetName": "Default__GunBuddy_RadianiteDiamond_Lv1_PrimaryAsset_C",
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
            "Name": "Sovereign Buddy",
            "ID": "547C3AA6-4E86-199C-B190-01B75287F30B",
            "AssetName": "Default__GunBuddy_Sovereign_Lv1_PrimaryAsset_C",
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
            "Name": "Prime",
            "ID": "2116A38E-4B71-F169-0D16-CE9289AF4BFA",
            "AssetName": "Default__StorefrontItem_HypebeastThemeBundle_DataAsset_C",
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
            "Name": "Sovereign",
            "ID": "FD9FD08F-446F-018F-C632-0E96428F2978",
            "AssetName": "Default__StorefrontItem_SovereignThemeBundle_DataAsset_C",
            "AssetPath": "",
            "IsEnabled": true
        }
    ]
}
```