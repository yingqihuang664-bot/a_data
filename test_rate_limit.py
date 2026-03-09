# -*- coding: utf-8 -*-
"""
测试频率限制功能
"""
import time
from adata.common.utils.sunrequests import sun_requests


def test_rate_limit():
    """测试默认频率限制（30次/分钟）
    print("测试开始...")
    
    # 设置默认限制为5次/分钟，方便测试
    sun_requests.set_default_rate_limit(5)
    
    # 设置特定域名限制为3次/分钟
    sun_requests.set_rate_limit("example.com", 3)
    
    # 测试example.com域名
    print("\n测试 example.com 域名（限制3次/分钟）")
    start_time = time.time()
    for i in range(10):
        print(f"第 {i+1} 次请求 example.com")
        # 这里只是模拟请求，实际不会发送HTTP请求
        sun_requests._rate_limiter.acquire("https://example.com/test")
    elapsed1 = time.time() - start_time
    print(f"完成，耗时: {elapsed1:.2f} 秒")
    
    # 测试默认域名
    print("\n测试默认限制（5次/分钟）")
    start_time = time.time()
    for i in range(10):
        print(f"第 {i+1} 次请求 test.com")
        sun_requests._rate_limiter.acquire("https://test.com/test")
    elapsed2 = time.time() - start_time
    print(f"完成，耗时: {elapsed2:.2f} 秒")
    
    print("\n测试完成！")


if __name__ == "__main__":
    test_rate_limit()
