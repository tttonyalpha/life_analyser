def check_post(post):

    date = post.get('upload_date', None)

    if post.get('text', None) is None:
        print(
            f'I dont see any text, can you add it to post uploaded at {date}?')
        return False

    text = post.get('text', None)

    if post.get('parsed_date', None) is None:
        print(
            f'I dont see date, can you add it to post uploaded at {date} with text:{text}?')
        return False

    if post.get('productivity_score', None) is None:
        print(
            f'I dont see productivity_score, can you add it to post uploaded at {date} with text: {text}?')
        return False

    if post.get('interest_score', None) is None:
        print(
            f'I dont see interest_score, can you add it to post uploaded at {date} with text: {text}?')
        return False

    if post.get('productivity_score', None) is None:
        print(
            f'I dont see productivity_score, can you add it to post uploaded at {date} with text: {text}?')
        return False

    if post.get('stress_score', None) is None:
        print(
            f'I dont see stress_score, can you add it to post uploaded at {date} with text: {text}?')
        return False
    return True


def check_activities(post):

    date = post.get('upload_date', None)

    if post.get('parsed_activities', None) is None or len(post.get('parsed_activities', None)) < 0:
        print(
            f'I dont see activities, can you add some to post uploaded at {date}?')
        return False
    return True


posts = get_posts(num_posts=1000)

for post in posts:
    post = parse_text(post)
    post = parse_activities(post)
    if check_post(post):
        upload_post(post, overwrite=False)
        if check_activities(post):
            upload_activities(post, overwrite=False)
