def combine(code,pwd,pb):
    title = input('[Info]輸入標題：')
    rtecontent = input('[Info]輸入內文：')
    _content_style = {
        'rtecontent':rtecontent,
        'nsubbsn':show_subboards(pb),
        'code':code,
        'native':'0',
        'subject':show_subject(),
        'bsn':'60076',
        'type':'1',
        'title':title,
        'pwd':pwd
    }
    return _content_style
def show_subboards(data):
    print('[Info]選擇子板')
    show_text = '[子板]'
    for item in data:
        show_text = show_text + '\n    ' + str('{:>2}').format(item['sn']) + '.' + item['title']
    print(show_text)
    return input('[選擇子板]編號：')
def show_subject():
    item = ['問題','情報','心得','討論','攻略','密技','閒聊','其他','空白']
    show_text = '[標題]'
    for i,it in enumerate(item):
        show_text = show_text + str(i+1) + '.' + it + '｜'
    print(show_text)
    return input('[選擇主題]編號：')