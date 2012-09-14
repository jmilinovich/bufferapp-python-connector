#!/usr/bin/env python
# encoding: utf-8
"""
buffer1.py

Created by John R Milinovich on 2012-08-20.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
import urllib
import json
import pprint


# profile data
'''
url = 'https://api.bufferapp.com/1/profiles.json?access_token=1/{YOUR TOKEN HERE}'
text = urllib.urlopen(url)
object = json.load(text)
print object[0]['statistics']['followers']
print object[0]['counts']['pending']
print object[0]['counts']['sent']
print object[0]['service_username']
print object[0]['id']
'''

# past post data

def Connecter(pagenum):
  updates_url = 'https://api.bufferapp.com/1/profiles/4f13b938512f7e2427000002/updates/sent.json?count=100&page=%s&access_token=1/{YOUR TOKEN HERE}' % pagenum
  updates_text = urllib.urlopen(updates_url)
  updates_obj = json.load(updates_text)
  updates_on_page = len(updates_obj['updates'])
  total_updates = int(updates_obj['total'])
  return updates_obj,updates_on_page,total_updates

def main():

  updates_obj,updates_on_page,total_updates = Connecter('0')
  
  num_full_pages = total_updates / 100
  last_page_posts = total_updates % 100

  post_dict = {}

  for i in range(0,num_full_pages+2):
    updates_obj,updates_on_page,total_updates = Connecter(str(i))
    # add every entry on page to dictionary
    for i in range(0,updates_on_page):
      post_dict[updates_obj['updates'][i]['service_update_id']] = [
                                                                    updates_obj['updates'][i]['text'],
                                                                    updates_obj['updates'][i]['statistics']['clicks'],
                                                                    updates_obj['updates'][i]['statistics']['favorites'],
                                                                    updates_obj['updates'][i]['statistics']['mentions'],
                                                                    updates_obj['updates'][i]['statistics']['reach'],
                                                                    updates_obj['updates'][i]['statistics']['retweets']
                                                                    ]
  pprint.pprint(post_dict)

if __name__ == '__main__':
  main()

#####                       #####
##### profile data response #####
"""
[{u'_id': u'4f13b938512f7e2427000002',
  u'avatar': u'http://a0.twimg.com/profile_images/1605589229/pic_normal.png',
  u'avatar_https': u'https://si0.twimg.com/profile_images/1605589229/pic_normal.png',
  u'counts': {u'pending': 1, u'sent': 275},
  u'created_at': 1326692664,
  u'default': True,
  u'formatted_username': u'@jmilinovich',
  u'id': u'4f13b938512f7e2427000002',
  u'schedules': [{u'days': [u'mon',
                            u'tue',
                            u'wed',
                            u'thu',
                            u'fri',
                            u'sat',
                            u'sun'],
                  u'times': [u'09:20', u'14:25', u'15:49', u'19:35']}],
  u'service': u'twitter',
  u'service_id': u'139638149',
  u'service_username': u'jmilinovich',
  u'statistics': {u'followers': 259},
  u'timezone': u'America/Los_Angeles',
  u'user_id': u'4f13b901512f7eba2600000c',
  u'verb': u'tweet'}]
"""

#####                    #####
##### post data response #####
'''
{u'total': 275,
 u'updates': [{u'_id': u'5031b4a1dd81259407000010',
               u'client_id': u'4ea9c36d512f7e2a2c000002',
               u'created_at': 1345434785,
               u'day': u'Today',
               u'due_at': 1345516500,
               u'due_time': u'7:35 pm',
               u'id': u'5031b4a1dd81259407000010',
               u'media': [],
               u'profile_id': u'4f13b938512f7e2427000002',
               u'profile_service': u'twitter',
               u'sent_at': 1345516509,
               u'service_update_id': u'237739583385776128',
               u'statistics': {u'clicks': 1,
                               u'favorites': 0,
                               u'mentions': 0,
                               u'reach': 259,
                               u'retweets': 0},
               u'status': u'sent',
               u'text': u'TechCrunch: Consumer Is King: Record $4B Raised In Mobile VC In The First Half Of 2012, 25%+ In Consumer Apps http://tcrn.ch/PxJVef',
               u'text_formatted': u'TechCrunch: Consumer Is King: Record $4B Raised In Mobile VC In The First Half Of 2012, 25%+ In Consumer Apps <a class="url" href="http://tcrn.ch/PxJVef" rel="external nofollow" target="_blank">http://tcrn.ch/PxJVef</a>',
               u'updated_at': 1345526007,
               u'user_id': u'4f13b901512f7eba2600000c',
               u'via': u'api'},
'''