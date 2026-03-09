# -*- coding: utf-8 -*-
from adata.common.utils.sunrequests import sun_requests

print("导入成功")

sun_requests.set_default_rate_limit(30)
print("默认限制设置成功")

sun_requests.set_rate_limit("example.com", 10)
print("特定域名限制设置成功")

print("\n所有功能测试成功！")
