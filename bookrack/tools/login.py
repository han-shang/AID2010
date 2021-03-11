from django.http import JsonResponse
import jwt
from django.conf import settings
from books.models import User


def login_check(func):
    def wrap(request, *args, **kwargs):
        # 在请求对象中获取前段提交过来的token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)
        # token的校验
        try:
            # decode方法中，首先会验签，签名是否有效；
            # 验签通过后，从 payload获取有效期，判断token是否在有效期内
            payload = jwt.decode(token,
                                 settings.JWT_TOKEN_KEY,
                                 algorithm='HS256')
        except:
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)
        # 从结果中获取私有申明
        email = payload['email']
        # 根据用户名称获取用户对象
        user = User.objects.get(email=email)
        # 将用户对象作为request的附加属性
        request.myuser = user
        # 调用所修饰的函数
        return func(request, *args, **kwargs)

    return wrap