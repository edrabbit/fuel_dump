fuel_dump

Quick and easy way to dump your Fuelband activities via API

This was written with the intent of pulling down my daily Fuelband data so I
could feed it into Splunk (http://www.splunk.com). It's super simple and could
be made more robust with some time. But it serves it's purpose for now.

Will spit out a log file with json formatted entries. Be sure to specify at
least the count in order to pull more than the default of 5 items.

https://developer.nike.com/activities/list_users_activities
