# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 4:10 下午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : case_env_api.py
# @Software: PyCharm

from app.all_reference import *
from app.models.test_env.models import TestEnv


class CaseEnvApi(MethodView):
    """
    用例测试环境Api
    GET: 环境详情
    POST: 环境新增
    PUT: 环境编辑
    DELETE: 环境删除
    """

    def get(self, env_id):
        """环境详情"""

        query_env = TestEnv.query.get(env_id)

        if not query_env:
            return api_result(code=400, message='环境id:{}数据不存在'.format(env_id))

        return api_result(code=200, message='删除成功', data=query_env.to_json())

    def post(self):
        """环境新增"""

        data = request.get_json()
        env_url = data.get('env_url')
        env_name = data.get('env_name')
        remark = data.get('remark')

        query_env = TestEnv.query.filter_by(env_url=env_url).first()

        if query_env:
            return api_result(code=400, message='环境:{} 已经存在'.format(env_url))

        new_env = TestEnv(
            env_url=env_url,
            env_name=env_name,
            remark=remark,
            creator='调试',
            creator_id=1
        )
        db.session.add(new_env)
        db.session.commit()
        return api_result(code=201, message='创建成功')

    def put(self):
        """环境编辑"""

        data = request.get_json()
        env_id = data.get('env_id')
        env_url = data.get('env_url')
        env_name = data.get('env_name')
        remark = data.get('remark')

        query_env = TestEnv.query.get(env_id)

        if not query_env:
            return api_result(code=400, message='环境id:{} 不存在'.format(env_id))

        if query_env.env_url != env_url:
            if TestEnv.query.filter_by(env_url=env_url).all():
                return api_result(code=400, message='环境url:{} 已经存在'.format(env_url))

        query_env.env_url = env_url
        query_env.env_name = env_name
        query_env.remark = remark
        query_env.modifier = "调试"
        query_env.modifier_id = 1
        db.session.commit()
        return api_result(code=203, message='编辑成功')

    def delete(self):
        """环境删除"""

        data = request.get_json()
        env_id = data.get('env_id')

        query_env = TestEnv.query.get(env_id)

        if not query_env:
            return api_result(code=400, message='环境id:{}数据不存在'.format(env_id))

        query_env.is_deleted = query_env.id
        query_env.modifier = "调试"
        query_env.modifier_id = 1
        db.session.commit()
        return api_result(code=204, message='删除成功')
