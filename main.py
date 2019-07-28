import requests
import post_content as pc
#停止SSL報錯
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def makecookie(account):
    post_cookies = 'BAHAENUR={};BAHAID={};__cfduid={};BAHARUNE={};BAHANICK={};MB_BAHANICK={};ckFORUM_bsn={};MB_BAHAID={};ckAndroidAccount={};BAHAFLT={};MB_BAHARUNE={};BAHALV={};'.format(
        account.cookies['BAHAENUR'],
        account.cookies['BAHAID'],
        account.cookies['__cfduid'],
        account.cookies['BAHARUNE'],
        account.cookies['BAHANICK'],
        account.cookies['MB_BAHANICK'],
        '60076',
        account.cookies['MB_BAHAID'],
        account.cookies['BAHAID'],
        account.cookies['BAHAFLT'],
        account.cookies['MB_BAHARUNE'],
        account.cookies['BAHALV']
    )
    return post_cookies
def _post(baseLogin):
    post_page = baseLogin.get('https://api.gamer.com.tw/mobile_app/forum/v2/post1.php?type=1&bsn=60076')
    post_page = post_page.json()
    print('[-----發文資訊如下-----]')
    print('[發文]板塊：'+post_page['board_title'])
    post_pwd = post_page['pwd']
    post_code = post_page['code']
    post_subboards = post_page['subboards']
    baseLogin.headers.update({
        'cookie':makecookie(baseLogin)+'ckFROUM_MPOST='+post_pwd
    })
    data = pc.combine(post_code,post_pwd,post_subboards)
    r = baseLogin.post('https://api.gamer.com.tw/mobile_app/forum/v2/post2.php',data = data)
    print(r.text)
    print('[AC]發布成功！快去手機看看吧！')
def _getInfo(data):
    baseLogin = requests.session()
    baseLogin.headers.update(
        {
        'user-agent': 'Bahadroid (https://www.gamer.com.tw/)',
        'x-bahamut-app-instanceid': 'cc2zQIfDpg4',
        'x-bahamut-app-android': 'tw.com.gamer.android.activecenter',
        'x-bahamut-app-version': '251',
        'content-type': 'application/x-www-form-urlencoded',
        'content-length': '44',
        'accept-encoding': 'gzip',
        'cookie': 'ckAPP_VCODE=7045'
        },
    )

    account = baseLogin.post('https://api.gamer.com.tw/mobile_app/user/v3/do_login.php',data=data,verify=False)
    account_f = account.json()
    print('[Info]Login success!')
    print('[Info]您好：{}'.format(account_f['nickname']))
    print('[-----勇者資訊如下-----]')
    print('[Info]等級：{}'.format(account_f['lv']))
    print('[Info]ＧＰ：{}'.format(account_f['gp']))
    print('[Info]巴幣：{}'.format(account_f['gold']))
    baseLogin.headers.update({
        'cookie':makecookie(account)
    })
    baseLogin.headers = {
        'user-agent': 'Bahadroid (https://www.gamer.com.tw/)',
        'x-bahamut-app-instanceid': 'cc2zQIfDpg4',
        'x-bahamut-app-android': 'tw.com.gamer.android.activecenter',
        'x-bahamut-app-version': '251',
        'accept-encoding': 'gzip'
    }

    _post(baseLogin)
if __name__ == "__main__":
    data = {
        'uid':input('輸入帳號：'),
        'passwd':input('輸入密碼：'),
        'vcode':'7045'
    }
    _getInfo(data)