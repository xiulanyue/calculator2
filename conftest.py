import pytest
import yaml
from pythoncode.calculator import Calculator
import os
file_path = os.path.dirname(__file__) + "/calculator_data.yaml"

with open(file_path) as f:
    datas = yaml.safe_load(f)
    add_datas = datas["add_datas"]
    sub_datas = datas["sub_datas"]
    mul_datas = datas["mul_datas"]
    div_datas = datas["div_datas"]
    myids = datas["myids"]

@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=add_datas,ids=myids)
def get_add_datas(request):
    data = request.param
    return data

@pytest.fixture(params=sub_datas,ids=myids)
def get_sub_datas(request):
    data = request.param
    return data

@pytest.fixture(params=mul_datas,ids=myids)
def get_mul_datas(request):
    data = request.param
    return data

@pytest.fixture(params=div_datas,ids=myids)
def get_div_datas(request):
    data = request.param
    return data