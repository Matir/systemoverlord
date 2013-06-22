import datetime
import json
import urllib2
from email.utils import parsedate_to_datetime as parsedate
from mezzanine.blog.management.base import BaseImporterCommand

class Command(BaseImporterCommand):
  def _comment_from_post(self, post):
      if 'comment_body' not in post:
      return None
      comment = {
          'body': post['comment_body'],
          'author': post['comment_author'],
          'title': post['comment_title'],
          'posted': post['comment_posted'],
      }
      del post['comment_body']
      del post['comment_author']
      del post['comment_title']
      del post['comment_posted']
      return comment

  def handle_import(self, options):
    raw_json = json.load(urllib2.urlopen('https://systemoverlord.com/blog.json'))
    blog_posts = {}
    for post in raw_json['nodes']:
      post = post['node']
      comment = comment_from_post(post)
      blog_posts.setdefault(post['path'], post).setdefault(
          'comments', []).append(comment)
    for post in blog_posts.values():
      date = parsedate(post['post_date'])
      tags = [t.strip() for t in post['tags'].split(',')] if post['tags'] else None
      post = self.add_post(title=post['title'],
                           old_url=post['path'],
                           content=post['body'],
                           pub_date=date,
                           tags=tags,
                           categories=[post['category']])
      for comment in filter(None, post['comments']):
        self.add_comment(post=post, name=comment['author'], body=comment['body'],
                         pub_date=parsedate(comment['posted']))

    
