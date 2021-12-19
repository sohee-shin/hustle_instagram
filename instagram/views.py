from rest_framework.views import APIView
from django.shortcuts import render

from content.models import Feed, Reply, Like, Bookmark
from user.models import User


class Main(APIView):
    def get(self, request):
        if request.session.get('login_check'):  # 로그인 성공여부 확인

            # 세션의 email 정보 가져와서 User DB에서 사용자 정보 찾아오기
            email = request.session.get('email')
            find_user = User.objects.filter(email=email).first()

            # data_list 안에 Reply DB정보를 넣기 위해 분해함
            data_list = []
            for feed in Feed.objects.all().order_by('-id'):
                data_list.append(dict(id=feed.id,
                                      image=feed.image,
                                      profile_image=feed.profile_image,
                                      nickname=feed.nickname,
                                      content=feed.content,
                                      reply_list=Reply.objects.filter(feed_id=feed.id),
                                      is_like=Like.objects.filter(email=email, feed_id=feed.id).exists(),
                                      is_bookmark=Bookmark.objects.filter(email=email, feed_id=feed.id).exists()
                                      )
                                 )

            # main.html로 로그인 사용자 정보를 'user_info'로 넘기기
            return render(request, "instagram/main.html",
                          context=dict(
                              data_list=data_list,
                              user_info=find_user
                          ))

        # 로그인 실패시 로그인 페이지로 이동
        else:
            return render(request, "user/login.html")


class Mypage(APIView):
    def get(self, request):
        if request.session.get('login_check'):  # 로그인 성공여부 확인

            # 세션의 email 정보 가져와서 User DB에서 사용자 정보 찾아오기
            email = request.session.get('email')
            find_user = User.objects.filter(email=email).first()

            # data_list 안에 Reply DB정보를 넣기 위해 분해함
            data_list = []
            for feed in Feed.objects.all().order_by('-id'):
                data_list.append(dict(id=feed.id,
                                      image=feed.image,
                                      profile_image=feed.profile_image,
                                      nickname=feed.nickname,
                                      content=feed.content,
                                      reply_list=Reply.objects.filter(feed_id=feed.id),
                                      is_like=Like.objects.filter(email=email, feed_id=feed.id).exists(),
                                      is_bookmark=Bookmark.objects.filter(email=email, feed_id=feed.id).exists()
                                      )
                                 )

            # main.html로 로그인 사용자 정보를 'user_info'로 넘기기
            return render(request, "instagram/mypage.html",
                          context=dict(
                              data_list=data_list,
                              user_info=find_user
                          ))

        # 로그인 실패시 로그인 페이지로 이동
        else:
            return render(request, "user/login.html")


