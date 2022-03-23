import random

from .models import Post, PostCategory, Category, Comment, Author
from django.contrib.auth.models import User
from .articles import post_title1, post_title2, post_title3, post_text1, post_text2, post_text3


def launch():
    user1 = User.objects.create_user('Mike Smith', email='mikes@gmail.com', password='5432112345')
    user2 = User.objects.create_user('Elizabeth Baldwin', email='lizaa@gmail.com', password='1234554321')

    author1 = Author.objects.create(user=user1)
    author2 = Author.objects.create(user=user2)

    category1 = Category.objects.create(category_name='Business')
    category2 = Category.objects.create(category_name='Economy')
    category3 = Category.objects.create(category_name='Ecology')
    category4 = Category.objects.create(category_name='Sport')

    post1 = Post.objects.create(
        post_title=post_title1,
        post_text=post_text1,
        author=author1
    )
    post2 = Post.objects.create(
        post_title=post_title2,
        post_text=post_text2,
        author=author1
    )
    post3 = Post.objects.create(
        news_type='N',
        post_title=post_title3,
        post_text=post_text3,
        author=author2
    )

    PostCategory.objects.create(post=post1, category=category1)
    PostCategory.objects.create(post=post1, category=category2)
    PostCategory.objects.create(post=post2, category=category4)
    PostCategory.objects.create(post=post3, category=category3)
    PostCategory.objects.create(post=post3, category=category2)

    comment1 = Comment.objects.create(comment_post=post2, comment_user=user2,
                                      comment_text='Sport really is a great part of our lives that provides opportunities to many things except good physical form. Sport and team work make us only better and develop our best characteristics!')
    comment2 = Comment.objects.create(comment_post=post2, comment_user=user1,
                                      comment_text='Thank you for your opinion!')
    comment3 = Comment.objects.create(comment_post=post1, comment_user=user2,
                                      comment_text='It is a very difficult time for me and my bakery business. I hope we will manage. Thank you for such an informative article')
    comment4 = Comment.objects.create(comment_post=post1, comment_user=user1,
                                      comment_text='I have the same situation, planning to cut expenses where it is possible')
    comment5 = Comment.objects.create(comment_post=post1, comment_user=user1,
                                      comment_text='I am glad that you find this article to be usefull, hope everything will be good')
    comment6 = Comment.objects.create(comment_post=post3, comment_user=user1,
                                      comment_text='Nothing will save the environment!')

    list_for_rating = [
        post1, post2, post3,
        comment1, comment2, comment3,
        comment4, comment5, comment6
    ]

    for i in range(100):
        random_obj = random.choice(list_for_rating)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

    Author.objects.get(pk=1).update_rating()
    Author.objects.get(pk=2).update_rating()

    best_author = Author.objects.all().order_by('-user_rating')[0].user.username
    print('The best author is', best_author)

    best_article = Post.objects.filter(news_type='A').order_by('-post_rating')[0]
    best_article_rating = best_article.post_rating
    best_article_time = best_article.creation_date
    best_article_author = best_article.author.user.username
    best_article_preview = best_article.preview()
    best_article_title = best_article.post_title

    print(f'The best article with overall rating {best_article_rating} points is entitled {best_article_title}. \n'
          f'It is written by {best_article_author} at {best_article_time}.\n'
          f'Preview: {best_article_preview}')

    for comment in Comment.objects.filter(comment_post=best_article):
        print(
            f'Comment id: {comment.id}, \n'
            f'Data: {comment.creation_date_comment}, \n'
            f'Username: {comment.comment_user.username}, \n'
            f'Rating: {comment.comment_rating}, \n'
            f'Comment: {comment.comment_text}'
        )

