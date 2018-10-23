# Salesforce Quick Connect

## Using OAUTH

Use this terminal based form to quickly connect to your Sandbox instance.

Requirements:

- `python`
- `pip`
- `requests` (ex: `pip install requests`)

#### Running Connect Tool:

From the root directory:

```
#> python main.py
```

#### Other Notes:

You will need a `consumer key` to make the connection (there are other password based use cases as well, not demonstrated here). 

To enable an API Application in your Salesforce instance, follow the directions here:

https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_defining_remote_access_applications.htm

You must be an Admin of the instance to perform the above settinsg configs. The Admin will be able to modify access rights for users from there, or simply provide the consumer key to users. 

## Using Username / Password 

... (WIP) ...
