""" fuel_dump.py - Quick and easy way to dump your Fuelband activities via API

This was written with the intent of pulling down my daily Fuelband data so I
could feed it into Splunk (http://www.splunk.com). It's super simple and could
be made more robust with some time. But it serves it's purpose for now.

Will spit out a log file with json formatted entries. Be sure to specify at
least the count in order to pull more than the default of 5 items.

https://developer.nike.com/activities/list_users_activities

"""

__author__ = "Ed Hunsinger"
__copyright__ = "Copyright 2013"
__email__ = "edrabbit@edrabbit.com"

import datetime
import json
import urllib2


def make_request(url):
    req = urllib2.Request(url)
    req.add_header("appid", "fuelband")
    req.add_header("Accept", "application/json")
    handle = urllib2.urlopen(req)
    data = json.load(handle)
    return data

def process_data(data):
    data = data['data']
    data.reverse()
    results = []
    for activity in data:
        results.append(activity)
    return results

if __name__ == "__main__":
    # TODO: Make all of this into arguments
    access_token = "YOUR_ACCESS_TOKEN"  # 
    output_file = 'output.log'
    root_domain = 'https://api.nike.com'

    # Nike's API is confusing.
    #  If I give it a start date of 2013-01-01
    #  and an end date of 2013-01-03 and count set to 3,
    #  it returns results for 2013-01-02, 2013-01-03, and 2013-01-04
    start_date = '2012-12-31'
    end_date = '2013-12-31'
    dt_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    dt_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    count = (dt_end_date - dt_start_date).days + 1

    # Turns out start_date and end_date are optional. If you want to grab all
    # of your activities/days, then set the count to your number of
    # days/activities.
    #endpoint = (
    # '/me/sport/activities?access_token=%s&count=%s&startDate=%s&endDate=%s'
    # % (access_token, count, start_date, end_date))

    endpoint = (
        '/me/sport/activities?access_token=%s&count=%s'
        % (access_token, count))
    url = '%s%s' % (root_domain, endpoint)
    data = make_request(url)
    results = process_data(data)
    results = sorted(results, key=lambda day: day['startTime'])

    of = open(output_file, 'w')
    for day in results:
        of.write('%s\n' % (json.dumps(day)))
    of.close()