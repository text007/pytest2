# pytest文档27-运行上次失败用例(--lf 和 --ff）


# --lf 和 --ff
"""
—lf, —last-failed   只重新运行上次运行失败的用例（或如果没有失败的话会全部跑）
—ff, —failed-first  运行所有测试，但首先运行上次运行失败的测试（这可能会重新测试，从而导致重复的fixture setup/teardown）
"""


# --lf
"""
只想运行其中2个failed的和1error用例
pytest --lf
cd:pytest26
"""


# --ff
"""
先运行上次失败的，后运行其它通过的用例
--ff
cd:pytest26
"""
