import os
import requests



cookies = {
    'qgqp_b_id': 'fa53fd3ad7eb8a13d75b11161280c247',
    'websitepoptg_show_time': '1702474216572',
    'EMFUND1': 'null',
    'EMFUND2': 'null',
    'EMFUND3': 'null',
    'EMFUND4': 'null',
    'EMFUND5': 'null',
    'EMFUND6': 'null',
    'EMFUND7': 'null',
    'EMFUND8': 'null',
    'EMFUND0': 'null',
    'EMFUND9': f"12-13 21:54:38^@^#^{os.getenv('^%^u4E1C^%^u65B9^%^u7EA2^%^u533B^%^u7597^%^u5347^%^u7EA7^%^u80A1^%^u7968^%^u53D1^%^u8D77C^@^%^23^%^24015053')}",
    'websitepoptg_api_time': '1702814315967',
    'HAList': 'ty-1-603231-N^%^u7D22^%^u5B9D',
    'st_si': '98715156446841',
    'st_asi': 'delete',
    'st_pvi': '30703821769824',
    'st_sp': '2023-12-13^%^2021^%^3A30^%^3A16',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.baidu.com^%^2Flink',
    'st_sn': '7',
    'st_psi': '20231218195709934-111000300841-2442594431',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://data.eastmoney.com/zjlx/detail.html',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'sec-ch-ua': '^\\^Not_A',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
}

params = (
    ('cb', 'jQuery1123005572818619135278_1702900798396'),
    ('fid', 'f62'),
    ('po', '1'),
    ('pz', '50'),
    ('pn', '1'),
    ('np', '1'),
    ('fltt', '2'),
    ('invt', '2'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5'),
    ('fs', 'm^%^3A0^%^2Bt^%^3A6^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A13^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A80^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A2^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A23^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A7^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A3^%^2Bf^%^3A^!2'),
    ('fields', 'f12^%^2Cf14^%^2Cf2^%^2Cf3^%^2Cf62^%^2Cf184^%^2Cf66^%^2Cf69^%^2Cf72^%^2Cf75^%^2Cf78^%^2Cf81^%^2Cf84^%^2Cf87^%^2Cf204^%^2Cf205^%^2Cf124^%^2Cf1^%^2Cf13'),
)

response = requests.get('https://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery1123005572818619135278_1702900798396&fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m^%^3A0^%^2Bt^%^3A6^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A13^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A80^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A2^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A23^%^2Bf^%^3A^!2^%^2Cm^%^3A0^%^2Bt^%^3A7^%^2Bf^%^3A^!2^%^2Cm^%^3A1^%^2Bt^%^3A3^%^2Bf^%^3A^!2&fields=f12^%^2Cf14^%^2Cf2^%^2Cf3^%^2Cf62^%^2Cf184^%^2Cf66^%^2Cf69^%^2Cf72^%^2Cf75^%^2Cf78^%^2Cf81^%^2Cf84^%^2Cf87^%^2Cf204^%^2Cf205^%^2Cf124^%^2Cf1^%^2Cf13', headers=headers, cookies=cookies)
print(response)
print(response.text)