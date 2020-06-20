# User Balance
Get User's Valorant Points, Radianite Points, and ___

## Example
```http
GET https://pd.na.a.pvp.net/store/v1/wallet/PLAYERID
Content-Type: application/json
Authorization: Bearer riot_auth_token
X-Riot-Entitlements-JWT: riot_entitlement_token

{
    "Balances": {
        "85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741": 1930,
        "e59aa87c-4cbf-517a-5983-6e81511be9b7": 60,
        "f08d4ae3-939c-4576-ab26-09ce1f23bb37": 0
    }
}
```

| Currency | ID |
| - | - |
| Valorant Points | 85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741 |
| Radianite Points | e59aa87c-4cbf-517a-5983-6e81511be9b7 |
| Unknown (Always has been 0, Probably Future Currency) | f08d4ae3-939c-4576-ab26-09ce1f23bb37 |


## Template
Here is how to use `cURL` to get User's Balences:
- URL: `https://pd.na.a.pvp.net/store/v1/wallet/'PlayerID'`
- Method: `GET`
- Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`