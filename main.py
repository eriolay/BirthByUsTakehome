# import json 

# with open("users.json") as users_file:
#     users_data = json.load(users_file)

# with open("posts.json") as posts_file:
#     posts_data = json.load(posts_file)

# sorted_posts = sorted(posts_data, key=lambda x: x['date'], reverse=True)

# #for each entry in sorted posts, need to add that (top to bottom) to the page in a white square with the user profile
# #pic in a litte circle and the username next to it and the date in Day of the Week, Month Date, Year

import json
from datetime import datetime

#helper functions
def load_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
def get_user_info(user_id):
    for user_info in users_data:
        if user_info['id'] == user_id:
            return user_info
    return None

def date_words(date_str):
    # convert the string to a datetime object
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    
    # convert the datetime object to the date in words
    # Example: "Monday, March 01, 2022"
    date_in_words = date_object.strftime("%A, %B %d, %Y")  
    
    return date_in_words


users_data = load_json_file('users.json')
posts_data = load_json_file('posts.json')


# Sort posts by date in descending order
sorted_posts = sorted(posts_data, key=lambda x: x['date'], reverse=True)

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Posts</title>
    <link rel="stylesheet" href="styles.css">
    </head>
<body>

<div class="heading-container">
    <h1>Community</h1>
    <p class="sub-heading">Connection is the heartbeat of our lives; we are stronger together!</p>
</div>
<div class="post-container">
    """


for post in sorted_posts:
    user_id = post['id']
    user_info = get_user_info(user_id)
    html_content += f"""
    <div class="post">
        <div class="user-info">
            <img class="profile-pic" src="photos/{user_info['profile_photo']}" alt="{user_info['username']}">
            <div class="user-details">
                <h2>@{user_info['username']}</h2>
                <p style="font-weight:300; font-size:14px; font-style: italic; color: #8F4F40">{date_words(post['date'])}</p>
            </div>
        </div>
        <p>{post['content']}</p>
    </div>
    """



html_content += """
</div>
<div class="footer">
    <div class="copyright">
        <p>2022 Birth By Us, Inc. All rights reserved.</p>
    </div>
    <div class="disclaimer">
        <p>Disclaimer: Birth By Us does not provide medical advice. Our services are not a form of healthcare or medical advice. Any information presented to you through our services are meant for informational purposes only. If you have any questions or concerns related to your physical or mental health, contact your healthcare provider. By using our services, you understand and agree that Birth By Us is not a licensed practitioner of medicine.</p>
    </div>
    <div class="terms-service">
        <p>For the full Birth By Us Terms of Service, <a href="#">click here</a>.</p>
    </div>
    <nav>
        <ul class="nav-bar">
            <li><a href="https://birthbyus.com"><img src="Home nav.png" alt="Home"></a></li> 
            <li><a href="#"><img src="Insights nav.png" alt="Insights"></a></li>
            <li><a href="#"><img src="Resource nav.png" alt="Resources"></a></li>
            <li><a href="#"><img src="Community nav.png" alt="Community"></a></li>
        </ul>
    </nav>
</div>
</body>
</html>
"""

# Write HTML content to a file
with open('index.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
