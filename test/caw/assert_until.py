"""
断言工具
"""


def assert_res(actul_dict, expect_dict, keys):
    """
    断言方法
    :param actul_dict: 真实的响应结果，字典格式
    :param expect_dict: 预期的响应结果，字典格式
    :param keys: 要断言的字段，元组类型
    """
    for k in keys:
        assert actul_dict==expect_dict[k]