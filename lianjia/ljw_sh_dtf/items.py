# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class LjwShDtfItem(Item):
    # 房屋属性
    link_url = Field()  # 链接
    title = Field()     # 标题
    price = Field()     # 价格
    rooms = Field()     # 户型
    square = Field()    # 面积
    floor = Field()     # 楼层
    face = Field()      # 朝向
    area = Field()      # 区域
    uptime = Field()    # 上架时间
    community = Field() # 小区
    address = Field()   # 地址
    # subway = Field()    # 地铁

    # 联系经纪人属性
    # adviser_name = Field()   # 顾问姓名
    # adviser_phone = Field()  # 联系电话
    # look_times = Field()          # 带看次数
