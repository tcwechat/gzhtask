
from apps.base import BaseHandler
from utils.time_st import UtilTime
from utils.decorator.connector import Core_connector

from apps.task.task import follow_run,reply_run

class Follow(BaseHandler):

    @Core_connector(isTransaction=False,isTicket=False)
    async def post(self, *args, **kwargs):

        ut = UtilTime()

        runTime = ut.today.shift(seconds=5)

        for item in self.data['obj']['listids']:
            print(runTime.datetime)
            self.scheduler.add_job(follow_run, 'date',
                run_date=runTime.datetime,
                kwargs={
                    "url": "{}/v1/api/wechat/AccFollow_Send".format(self.application.settings.get("busiServer")),
                    "data": {
                        "data":{
                            "listid":item,
                            "nickname":self.data.get("nickname"),
                            "openid":self.data.get("openid"),
                            "accid":self.data.get("accid")
                        }
                    }
                })
            if self.data['obj']['sendlimit'].split(",")[1] == 'H':
                runTime = runTime.shift(hours=int(self.data['obj']['sendlimit'].split(",")[0]))
            elif self.data['obj']['sendlimit'].split(",")[1] == 'M':
                runTime = runTime.shift(minutes=int(self.data['obj']['sendlimit'].split(",")[0]))
            elif self.data['obj']['sendlimit'].split(",")[1] == 'S':
                runTime = runTime.shift(seconds=int(self.data['obj']['sendlimit'].split(",")[0]))

        return None

class Reply(BaseHandler):

    @Core_connector(isTransaction=False,isTicket=False)
    async def post(self, *args, **kwargs):

        ut = UtilTime()

        start = self.data['obj']['quiet'].split("-")[0]
        end = self.data['obj']['quiet'].split("-")[0]

        if start <= ut.arrow_to_string(format_v="HH:mm") <= end:
            return None
        else:
            pass

        t = self.data['obj']['nosend_limit'].split(',')[0]
        u = self.data['obj']['nosend_limit'].split(',')[1]

        createtime = ut.timestamp_to_arrow(self.data['obj']['createtime'])

        if u == 'H':
            runTime = createtime.shift(hours=int(t))
        elif u == 'M':
            runTime = createtime.shift(minutes=int(t))
        elif u == 'S':
            runTime = createtime.shift(seconds=int(t))
        else:
            return None

        if self.data['obj']['send_type'] == '0':
            self.scheduler.add_job(reply_run, 'date',
                                   run_date=runTime.datetime,
                                   kwargs={
                                       "url": "{}/v1/api/wechat/AccReply_Send".format(
                                           self.application.settings.get("busiServer")),
                                       "data": {
                                           "data": {
                                               "obj": self.data['obj'],
                                               "send_type": '1',
                                               "listids": self.data['obj']['listids'],
                                               "nickname": self.data.get("nickname"),
                                               "openid": self.data.get("openid"),
                                               "accid": self.data.get("accid")
                                           }
                                       }
                                   })
        elif self.data['obj']['send_type'] == '1':

            for item in self.data['obj']['listids']:
                print(runTime.datetime)
                self.scheduler.add_job(reply_run, 'date',
                                       run_date=runTime.datetime,
                                       kwargs={
                                           "url": "{}/v1/api/wechat/AccReply_Send".format(
                                               self.application.settings.get("busiServer")),
                                           "data": {
                                               "data": {
                                                   "obj":self.data['obj'],
                                                   "send_type":'2',
                                                   "listids": [item],
                                                   "nickname": self.data.get("nickname"),
                                                   "openid": self.data.get("openid"),
                                                   "accid": self.data.get("accid")
                                               }
                                           }
                                       })
                if self.data['obj']['sendlimit'].split(",")[1] == 'H':
                    runTime = runTime.shift(hours=int(self.data['obj']['sendlimit'].split(",")[0]))
                elif self.data['obj']['sendlimit'].split(",")[1] == 'M':
                    runTime = runTime.shift(minutes=int(self.data['obj']['sendlimit'].split(",")[0]))
                elif self.data['obj']['sendlimit'].split(",")[1] == 'S':
                    runTime = runTime.shift(seconds=int(self.data['obj']['sendlimit'].split(",")[0]))
        elif self.data['obj']['send_type'] == '2':
            self.scheduler.add_job(reply_run, 'date',
                                   run_date=runTime.datetime,
                                   kwargs={
                                       "url": "{}/v1/api/wechat/AccReply_Send".format(
                                           self.application.settings.get("busiServer")),
                                       "data": {
                                           "data": {
                                               "obj": self.data['obj'],
                                               "send_type": '0',
                                               "listids": self.data['obj']['listids'],
                                               "nickname": self.data.get("nickname"),
                                               "openid": self.data.get("openid"),
                                               "accid": self.data.get("accid")
                                           }
                                       }
                                   })

        return None