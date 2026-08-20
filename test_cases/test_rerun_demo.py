import random


def test_mabe_fail():

    num = random.randint(1, 3)
    assert num == 1,f"随机数{num} 不等于1，偶发失败"