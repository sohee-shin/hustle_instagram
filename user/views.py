import os
from uuid import uuid4

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.settings import MEDIA_ROOT
from user.models import User


class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        print("POST 요청이 들어옴")

        email = request.data.get('email')  # 인풋에서 이메일 가져오기
        name = request.data.get('name')  # 인풋에서 이름 가져오기
        nickname = request.data.get('nickname')  # 인풋에서 닉네임 가져오기
        password = request.data.get('password')  # 인풋에서 비밀번호 가져오기
        profile_image = ''

        User.objects.create(email=email,
                            name=name,
                            nickname=nickname,
                            password=password,
                            profile_image=profile_image)

        return Response(status=200, data=dict(message="회원가입에 성공했습니다."))


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        input_email = request.data.get('email')  # 인풋에서 이메일 가져오기
        input_password = request.data.get('password')  # 인풋에서 비밀번호 가져오기
        # 여기까지가 화면에서 올라온 email과 password 저장

        # 입력받은 email이 DB(user_user)에 있는지 확인
        if User.objects.filter(email=input_email).exists():  # 테이블에 있으면 True 반환됨
            # 회원정보 찾으면
            find_user = User.objects.filter(email=input_email).first()  # 찾은 결과가 여렷인 경우 첫번째 값만 반환
            if find_user.password == input_password:
                # 비밀번호가 맞은 경우 --> 로그인 성공

                request.session['email'] = find_user.email  # find_user.email 대신 input_email로 적어도 됨
                request.session['login_check'] = True

                return Response(status=200, data=dict(message="로그인 성공"))

            else:
                # 비밀번호가 틀린 경우
                return Response(status=400, data=dict(message="비밀번호가 틀렸습니다."))

        else:
            # 회원정보 못찾으면
            return Response(status=404, data=dict(message="회원정보가 없습니다."))


class UploadProfileImage(APIView):
    def post(self, request):
        print("POST 요청이 들어옴")

        file = request.FILES['file']  # 인풋에서 파일 가져오기
        email = request.data.get('email')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # 1. 사용자를 찾는다.
        find_user = User.objects.filter(email=email).first()

        # 2. 사용자 프로필 이미지를 변경한다.
        find_user.profile_image=uuid_name

        # 3. save()를 통해 변경된 데이터를 저장한다.
        find_user.save()

        return Response(status=200, data=dict(message="프로필이미지 업로드"))
