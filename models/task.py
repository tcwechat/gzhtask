
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


class AccMsgMould(BaseModel):
    """
    模板消息表
    """

    id = BigAutoField(primary_key=True)
    accid = BigAutoField(verbose_name="公众号ID")
    name = CharField(max_length=60,default="",verbose_name="消息名称")
    mould_id = CharField(max_length=60,verbose_name="模板ID",default="")
    mould_name = CharField(max_length=60,default="",verbose_name="模板名称")
    mould_data = CharField(max_length=1024,default="{}",verbose_name="模板数据")
    mould_skip = CharField(max_length=255,verbose_name="跳转",default="")
    sendtime = BigIntegerField(default=0, verbose_name="发送时间")
    send_count = IntegerField(verbose_name="发送人数", default=0)
    status = CharField(max_length=1,verbose_name="""
                                            发送状态
                                                '0'-已发送,
                                                '1'-未发送,
                                                '2'-发送中,
                                                '3'-发送终止,
                                                '4'-发送失败
                                            """,default='1')

    type = CharField(max_length=1, verbose_name="群发粉丝 '0'-全部,'1'-选择标签,'2'-选择性别")
    select_sex = CharField(max_length=1,verbose_name="条件筛选->性别,值为1时是男性，值为2时是女性，值为0时是未知")
    select_tags = CharField(max_length=1024,verbose_name="条件筛选->标签集合",default="[]")

    createtime = BigIntegerField(default=0)

    class Meta:
        db_table = 'accmsgmould'

class AccMsgMass(BaseModel):
    """
    群发消息
    """

    id = BigAutoField(primary_key=True)
    accid = BigIntegerField(verbose_name="公众号ID")
    sendtime = BigIntegerField(default=0, verbose_name="发送时间")
    send_count = IntegerField(verbose_name="发送人数", default=0)
    status = CharField(max_length=1,verbose_name="""
                                            发送状态
                                                '0'-已发送,
                                                '1'-未发送,
                                                '2'-发送中,
                                                '3'-发送终止,
                                                '4'-发送失败
                                            """,default='1')

    type = CharField(max_length=1,verbose_name="群发粉丝 '0'-按条件筛选,'1'-全部粉丝")
    select_sex = CharField(max_length=1, verbose_name="条件筛选->性别,值为1时是男性，值为2时是女性，值为0时是未知")
    select_followtime = CharField(max_length=60, verbose_name="条件筛选->关注时间", default="")
    select_province = CharField(max_length=60, verbose_name="条件筛选->省份", default="")
    select_city = CharField(max_length=60, verbose_name="条件筛选->城市", default="")
    select_tags = CharField(max_length=1024, verbose_name="条件筛选->标签集合", default="[]")
    power = CharField(max_length=1,verbose_name="微信后台权限 0-出现在微信后台已群发消息,1-不出现在微信后台已群发消息",default='1')
    repeat_send = CharField(max_length=1,verbose_name="转发继续发送 0-是,1-否",default='0')
    mobile = CharField(max_length=20,verbose_name="手机号",default="")
    listids = CharField(max_length=1024,verbose_name="IDs")

    createtime = BigIntegerField(default=0)

    class Meta:
        db_table = 'accmsgmass'