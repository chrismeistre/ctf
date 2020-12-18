## Port 9001

This was another easy one where you could immediately see this is a SQLi challenge.  

After checking the number of valid columns being returned, I fetched the table names and finally the column names.

The final payload was `search=A%27 UNION ALL SELECT 1,link,3 FROM hidden;--` and that gave me the link for the flag.
