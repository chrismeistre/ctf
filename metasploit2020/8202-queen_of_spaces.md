## Port 8202

This is another web challenge.  It was clear to quickly see this website makes use of a GraphQL backend.

It was easy to determine that the call `{"operationName": null, "variables": {}, "query": "{posts{media}}" }` was needed to show all the links for the posts.

One of them had the link to the flag.
