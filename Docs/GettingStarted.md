# Getting Started
Welcome to the Valorant API Quick-Start Guide. These API's are what are used within the game when you are playing.
These API's are very easy to use, and no one should have issues using them.
I made this Documentation as easy to understand that i possibly could.

## Replicating RSO and Getting an Authentication Token and Entitlement Token
**THIS SCRIPT IS CURRENTLY MADE FOR NA, PLEASE CHANGE ANY `NA` TO YOUR REGION**


A more in depth guide will be added to this page soon, for now please use [RSO_AuthFlow](https://github.com/RumbleMike/ValorantAPI/blob/master/Docs/RSO_AuthFlow.py) Made by Luc1412
- Requirements
	- Python 3
		- import re
		- import aiohttp
		- import asyncio
		- import json

This replication of RSO can be translated into other languages for authentication purposes. If you were to recreate RSO please note that you will need a CookieJar to store cookies for this
RSO method to function properly. This AuthFlow has already been implemented into C# and a Discord Bot To link Your Discord with Your Riot ACC.

## Example Request with [Postman](https://www.postman.com/)
Making a Get Request to get Story Contract Information:

Enter Access Token as An Authentication Bearer Token:
![Authen](https://user-images.githubusercontent.com/49486947/85186800-08f7f700-b269-11ea-92ac-876563c952ac.png)

Enter Entitlements Token as a Header as `X-Riot-Entitlements-JWT`:
![Postman_DbP6CrGIFq](https://user-images.githubusercontent.com/49486947/85186784-e8c83800-b268-11ea-8e02-fcf7bd77528f.png)

Receive Information Back :)_ :
![reap](https://user-images.githubusercontent.com/49486947/85186849-596f5480-b269-11ea-9743-43e1dde6572b.png)


## Questions?
Contact me on Discord @ `RumbleMike#5406`
