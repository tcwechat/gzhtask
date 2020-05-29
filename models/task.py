
from peewee import *
from models.base import BaseModel

class AccMsgCustomer(BaseModel):

    id = BigAutoField(primary_key=True)
    accids = CharField(max_length=1024,verbose_name="公众号ids",default="[]")
    name = CharField(max_length=60,default="",verbose_name="消息名称")
    listids = CharField(max_length=1024,verbose_name="推送内容id集合",default='[]')
    sendtime = BigIntegerField(default=0,verbose_name="发送时间")
    createtime = BigIntegerField(default=0)

    type = CharField(max_length=1,verbose_name="群发粉丝 '0'-按条件筛选,'1'-全部粉丝")
    status = CharField(max_length=1,verbose_name="""
                                            发送状态
                                                '0'-已发送,
                                                '1'-未发送,
                                                '2'-发送中,
                                                '3'-发送终止,
                                                '4'-发送失败
                                            """,default='1')

    select_sex = CharField(max_length=1,verbose_name="条件筛选->性别,值为1时是男性，值为2时是女性，值为0时是未知")
    select_followtime = CharField(max_length=60,verbose_name="条件筛选->关注时间",default="")
    select_province = CharField(max_length=60,verbose_name="条件筛选->省份",default="")
    select_city = CharField(max_length=60,verbose_name="条件筛选->城市",default="")
    select_tags = CharField(max_length=1024,verbose_name="条件筛选->标签集合",default="[]")

    class Meta:
        db_table = 'accmsgcustomer'