# User Balance
Make a GET Request and receive Valorant Points, Radianite Points and an Unknown Currency.

## Information
When making the request you will receive JSON text back, within the json text you will be seeing 3 different ids with each id containing a value. Please refer to the table below for id correlations.
| Currency | ID |
| - | - |
| Valorant Points | 85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741 |
| Radianite Points | e59aa87c-4cbf-517a-5983-6e81511be9b7 |
| Unknown | f08d4ae3-939c-4576-ab26-09ce1f23bb37 |

## Example
 - cURL: `https://pd.na.a.pvp.net/store/v1/wallet/'PlayerID'`
 - Method: `GET`
 - Headers:
    - Authorization: `Bearer riot_auth_token`
    - X-Riot-Entitlements-JWT: `riot_entitlement_token`


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
