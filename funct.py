def check_password(data):
    if data["password"] == data["psw_repeat"]:
        return True
    return False

def get_data(data):
    end_data_list = []
    for post in data:
        end_data_list.append( {
               "uid":post.uid,
               "short_desc":post.short_desc,
               "full_desc":post.full_desc,
               "type_ad":post.type_ad,
               "type_bust":post.type_bust,
               "type_LBZ":post.type_LBZ,
               "server":post.server,
               "fights_count":post.fights_count,
               "win_rait": post.win_rait,
               "raiting": post.raiting,
               "wn8": post.wn8,
               "count": post.count,
               "price": post.price,
               "trader_id": post.trader_id, })

    return end_data_list
def create_page_log(type):
    page = {'account':False,
            'bust':False,
            'klan':False,
            'bonus_kod':False,
            'lbz':False,
            'other':False,
            'farm':False,}
    if type =='account':
        page['account']= True
    elif type =='bust':
        page['bust']=True
    elif type =='klan':
        page['klan']=True
    elif type =='bonus_kod':
        page['bonus_kod']=True
    elif type =='lbz':
        page['lbz']=True
    elif type =='other':
        page['other']=True
    elif type =='farm':
        page['farm']=True
    return page