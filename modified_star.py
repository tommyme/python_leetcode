import json

import requests

from plugins.fuckwecqupt.entity.user import User
from saaya.helper.utils import *
import datetime

burp0_headers = {"Referer": "https://servicewechat.com/wx8227f55dc4490f45/148/page-frame.html",
                 "Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.B1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070333) NetType/4G Language/zh_CN Process/appbrand0"}


def get_newest_logid(user: User):
    burp0_url = "https://we.cqupt.edu.cn:443/api/lxsp_new/get_lxsp_student_list.php"

    req_params = {"openid": user.openid, "xh": user.studentNo, "page": 1, "timestamp": get_timestamp()}
    burp0_json = {
        "key": base64encode(json.dumps(req_params))}

    res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    results = json.loads(res.text)
    print(results)
    logger.debug(f'status:{results["status"]}')
    if len(results['data']) > 0:
        logger.debug(f'first data:{results["data"]["result"][0]}')
        return results["data"]["result"][0]['log_id']
    return "-1"


def my_auto_enter(enter_type: int, uniform_no: str):
    # 闸机设置0出校1入校
    if enter_type == 0:
        location = "崇文门出口4"
    else:
        location = "崇文门侧门入口2"

    burp0_url = "https://we.cqupt.edu.cn/api/lxsp_new/postInfo/getstuauth.php"
    time1 = get_timestamp()
    data_time1 = datetime.datetime.fromtimestamp(time1) + datetime.timedelta(hours=8)
    str_time1 = data_time1.strftime('%Y-%m-%d %H:%M:%S')
    signature = get_sign(str_time1, uniform_no, enter_type, time1)
    req_params = {"accesstime": str_time1, "flag": str(enter_type), "timestamp": time1, "tunnel": location,
                  "userid": uniform_no, "signature": signature}

    res = requests.post(burp0_url, headers=burp0_headers, json=req_params)
    print(res.text)
    results = json.loads(res.text)

    logger.debug(f'result:{results}')
    return results['errcode'] == 0


# 0 为out school，1 为in school,
def auto_enter(logid: str, enter_type: int, user: User):
    if enter_type == 0:
        location = "崇文门出口4"
    else:
        location = "崇文门侧门入口2"

    burp0_url = "https://we.cqupt.edu.cn:443/api/tools/post_lxsp_sm_bak1002.php"
    req_params = {"openid": user.openid, "xh": user.studentNo, "type": "入校" if enter_type == 1 else "出校",
                  "version": "",
                  "log_id": str(logid), "location": location, "latitude": 29.531151, "longitude": 106.599906,
                  "timestamp": get_timestamp()}

    burp0_json = {
        "key": base64encode(json.dumps(req_params, ensure_ascii=False))}
    res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    results = json.loads(res.text)

    logger.debug(f'result:{results}')
    return results['status'] == 200


# 可能可以直接绕过审批流程
def my_auto_apply(user: User):
    # 我也不知道为啥会少8个小时，估计是时区的问题，估计是docker时区的锅
    time1 = datetime.datetime.now() + datetime.timedelta(hours=8)
    time2 = time1 + datetime.timedelta(hours=24) if (time1 + datetime.timedelta(
        hours=24)).day == time1.day else datetime.datetime(time1.year, time1.month, time1.day, 23, 59, 59)
    burp0_url = "https://we.cqupt.edu.cn:443/api/lxsp/post_lxsp_spxx_test1228.php"
    req_params = {"xh": user.studentNo, "name": user.name, "xy": user.college, "nj": user.grade,
                  "openid": user.openid, "wcmdd": "重庆市,重庆市,南岸区", "qjsy": "无", "wcxxdd": "无", "sfly": "请选择",
                  "wcrq": time1.strftime('%Y-%m-%d %H:%M:%S'), "qjlx": "市内当日离返校",
                  "yjfxsj": time2.strftime('%Y-%m-%d %H:%M:%S'),
                  "beizhu": "", "timestamp": get_timestamp()}
    burp0_json = {
        "key": base64encode(json.dumps(req_params, ensure_ascii=False))}
    res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    results = json.loads(res.text)

    logger.debug(f'result:{results}')
    print(results)
    return results['status'] == 200


def get_sign(mytime: str, uniform_no: str, enter_type: int, time1: int):
    if enter_type == 0:
        tunnel = "崇文门出口4"
    else:
        tunnel = "崇文门侧门入口2"
    sign_s = "accesstime={}&flag={}&timestamp={}&tunnel={}&userid={}&key=f1f0c03dcacb8630d923b25d8b46da0b28080479".format(
        mytime, enter_type, time1, tunnel, uniform_no)
    print(sign_s)
    return get_md5(sign_s, False)


def my_new_apply(user: User):
    # 我也不知道为啥会少8个小时，估计是时区的问题，估计是docker时区的锅
    time1 = datetime.datetime.now()+ datetime.timedelta(hours=8)
    time2 = time1 + datetime.timedelta(hours=1.5) if (time1 + datetime.timedelta(
        hours=1.5)).day == time1.day else datetime.datetime(time1.year, time1.month, time1.day, 23, 59, 59)
    burp0_url = "https://we.cqupt.edu.cn:443/api/lxsp_new/post_lxsp_spxx.php"
    req_params = {"xh": user.studentNo, "name": user.name, "xy": user.college, "nj": user.grade,
                  "openid": user.openid, "wcmdd": "重庆市,重庆市,南岸区", "qjsy": "无", "wcxxdd": "无", "sfly": "请选择",
                  "wcrq": time1.strftime('%Y-%m-%d %H:%M:%S'), "qjlx": "市内1.5小时离返校",
                  "yjfxsj": time2.strftime('%Y-%m-%d %H:%M:%S'),
                  "beizhu": "", "timestamp": get_timestamp()}
    burp0_json = {
        "key": base64encode(json.dumps(req_params, ensure_ascii=False))}
    res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    results = json.loads(res.text)

    logger.debug(f'result:{results}')
    print(results)
    return results['status'] == 200