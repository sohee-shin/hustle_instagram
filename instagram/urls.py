"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from content.views import Test, CreateReply, CreateLike, CancelLike, CreateBookmark, CancelBookmark
from instagram import settings
from instagram.views import Main, Mypage
from user.views import Join, Login, UploadProfileImage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('test', Test.as_view()),
    path('join/', Join.as_view()),
    path('login/', Login.as_view()),
    path('reply/', CreateReply.as_view()),
    path('like/', CreateLike.as_view()),
    path('cancellike/', CancelLike.as_view()),
    path('bookmark/', CreateBookmark.as_view()),
    path('cancelbookmark/', CancelBookmark.as_view()),
    path('mypage/', Mypage.as_view()),
    path('uploadprofileimage/', UploadProfileImage.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

