# -*- coding: utf-8 -*-
import adata

print("测试主入口频率限制设置函数")

adata.set_default_rate_limit(20)
print("默认限制设置为 20次/分钟 成功")

adata.set_rate_limit("eastmoney.com", 50)
print("东方财富域名限制设置为 50次/分钟 成功")

adata.set_rate_limit("10jqka.com.cn", 60)
print("同花顺域名限制设置为 60次/分钟 成功")

print("\n所有API测试成功！")
