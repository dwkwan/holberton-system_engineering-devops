#!/usr/bin/python3
"""queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
import operator


def count_words(subreddit, word_list=[], word_dict={}, after=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code == 200:
        json = r.json()
        data_dict = json.get('data')
        post_list = data_dict.get('children')
        for post in post_list:
            post_data_dict = post.get('data')
            for word in word_list:
                count = post_data_dict.get('title').count(word.capitalize())
                count += post_data_dict.get('title').count(word.lower())
                if word_dict.get(word):
                    word_dict[word] += count
                else:
                    word_dict[word] = count
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1),
                                 reverse=True)
            flag = 0
            for i in sorted_list:
                if i[1] > 0:
                    flag = 1
                    print("{:}: {:}".format(i[0], i[1]))
            if flag == 0:
                print()
            return
        return count_words(subreddit, word_list, word_dict, after)
    else:
        print()
        return
