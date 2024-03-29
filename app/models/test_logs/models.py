# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 12:33 上午
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm


from common.libs.BaseModel import *


class TestLogs(BaseModel):
    __tablename__ = 'exilic_test_logs'
    __table_args__ = {'comment': '日志记录表'}

    log_type = db.Column(db.String(255), nullable=False, comment='类型')
    creator = db.Column(db.String(32), comment='创建人')
    creator_id = db.Column(BIGINT(20, unsigned=True), comment='创建人id')
    remark = db.Column(db.String(255), comment='备注')

    def __repr__(self):
        return 'TestLogs 模型对象-> ID:{} log_type:{}'.format(self.id, self.log_type)
