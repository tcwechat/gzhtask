
from apps.base import BaseHandler
from utils.time_st import UtilTime
from utils.decorator.connector import Core_connector

from apps.task.task import follow_run

class Follow(BaseHandler):

    @Core_connector(isTransaction=False,isTicket=False)
    async def post(self, *args, **kwargs):

        ut = UtilTime()

        runTime = ut.today.shift(seconds=10)

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
            runTime = runTime.shift(hours=self.data['obj']['sendlimit'])

        return None