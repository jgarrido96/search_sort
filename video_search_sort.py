import shutil

from flask import Flask, jsonify, request # handling the import, giving us access to Flask and its functionality


def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)




videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

# Task 1: Implement the binary search algorithm for searching videos by title.

def sort_videos(lst, key = 'title'):
    swapped = True
    i = 1
    while swapped:
        swapped = False
        for idx in range(len(lst)-1):
            if lst[idx][key] > lst[idx+1][key]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                i += 1
                swapped = True
    return lst

videos_by_title = sort_videos(videos)
print(videos_by_title)

def video_search(vid_lst, video):
    low = 0
    high = 0
    num_checks = 0
    for a_dict in vid_lst:
        high += 1
    while low <= high:
        mid = (low+high) // 2
        num_checks += 1
        if vid_lst[mid]['title'] == video:
            return f"{video} can be found at index {mid}, and it took {num_checks} checks"
        elif video > vid_lst[mid]['title']:
            low = mid + 1
        else:
            high = mid - 1
    print('Not Found, checks:', num_checks)
    return -1

line_break()
print(video_search(videos_by_title, "Nature's Wonders: National Geographic"))


def title_merge(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        title_merge(left_half)
        title_merge(right_half)
        l = 0
        r = 0
        m = 0
        while l < len(left_half) and r < len(right_half):
            if left_half[l]['title'] < right_half[r]['title']:
                lst[m] = left_half[l]
                l +=1
            else:
                lst[m] = right_half[r]
                r += 1
            m += 1
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    return lst

# ********************** can't compare letters as lower or higher*******************
#************************Check Line 77***************************
# Everything else works tho :)

# Task 2: Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search developed in Task 1. This API should accept a search query as input and return the matching videos, if any.

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Welcome to our video selection!</p>"

@app.route("/title", methods = ["GET"])
def get_videos():
    return video_search(videos_by_title, 'The Art of Coding')

@app.route('/titles-list', methods = ['GET'])
def get_titles():
    return title_merge(videos)

# Video Sorting with Merge Sort:

# Task 1: 


if __name__ == '__main__':
    app.run(debug = True)
