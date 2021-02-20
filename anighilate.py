from flask import Flask, request
import vk_api, json, random, time

app = Flask(__name__)

appname = "botannihilator"
id = 
confirmation = "" #server answer
error_manager = #someone who gets messages about all erorrs
admin = 264056124 #someone who runs killing bad guys
annihilation_code = 33290 #any code to start programm
gaysubs = []

try:
    vk = vk_api.VkApi(token = '')
    vka = vk_api.VkApi(token = '')
    vka._auth_token()
    vk._auth_token()
except:
    #vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':'[1] Ошибка авторизации в VK API! [1]'})
    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
    logs.write(str('[' + time.ctime() + ']' + '[1] Ошибка авторизации в VK API! [1]' + '[' + time.ctime() + ']' + '\n'))
    logs.close()

vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':'Запуск!'})
members1 = vk.method('groups.getMembers', {'group_id':id, 'offset':0})
count1 = len(members1["items"])
logs1 = open("/home/" + appname + "/mysite/logs1.txt", "w", encoding='utf-8', errors='ignore')
logs1.write(str('[' + time.ctime() + ']' + '[1] ' + str(count1) + ' [1]' + '[' + time.ctime() + ']' + '\n'))
logs1.close()

try:
    with open("/home/" + appname + "/mysite/gaysubs.txt", "r", encoding='utf-8', errors='ignore') as read_file:
        for line in read_file:
            gaysubs.append(line.strip('\n'))
except:
    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
    logs.write(str('[' + time.ctime() + ']' + '[2] Ошибка открытия файла с запретными подписками! [2]' + '[' + time.ctime() + ']' + '\n'))
    logs.close()

def ban(group_id, owner_id):
    vk.method('groups.ban', {'group_id':group_id, 'owner_id':owner_id})

@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.data)
    if(data["type"] == "confirmation"):
        return confirmation
    elif(data["type"] == "group_join"):
        for group in gaysubs:
            member = vk.method('groups.isMember', {'group_id':group, 'user_id':data["object"]["user_id"]})
            if(member == 1):
                try:
                    ban(id, data['object']['user_id'])
                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                    logs.write(str('[' + time.ctime() + ']' + '[BAN] ' + str(data['object']['user_id']) + ' [BAN]' + '[' + time.ctime() + ']' + '\n'))
                    logs.close()
                except:
                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                    logs.write(str('[' + time.ctime() + ']' + '[3] Ошибка в процессе бана пользователя! (Администратор/уже в бане) [3]' + '[' + time.ctime() + ']' + '\n'))
                    logs.close()
                break
        return "ok"
    elif(data["type"] == "message_new"):
        if(data["object"]["user_id"] == admin):
            if(data["object"]["body"] == str(annihilation_code)):
                a = 0
                response = vk.method('groups.getById', {'group_id':id, 'fields':'members_count'})
                temp_count = response[0]['members_count']//1000
                temp_out = response[0]['members_count'] - (1000 * temp_count)
                vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':str(str(response[0]['members_count']) + ':' + str(temp_count) + ':' + str(temp_out))})
                for i in range(1, temp_count+1):
                    temp_offset = -1000 + i * 1000
                    vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':str(temp_offset)})
                    members = vk.method('groups.getMembers', {'group_id':id, 'offset':temp_offset})
                    for sub in members["items"]:
                        for group in gaysubs:
                            logs = open("/home/" + appname + "/mysite/logs2.txt", "a", encoding='utf-8', errors='ignore')
                            logs.write(str('[' + time.ctime() + ']' + str(group) + '[' + time.ctime() + ']' + '\n'))
                            logs.close()
                            member = vk.method('groups.isMember', {'group_id':str(group), 'user_id':sub})
                            if(member == 1):
                                try:
                                    ban(id, sub)
                                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                                    logs.write(str('[' + time.ctime() + ']' + '[BAN] ' + str(sub) + ' [BAN]' + '[' + time.ctime() + ']' + '\n'))
                                except Exception as err:
                                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                                    logs.write(str('[' + time.ctime() + ']' + '[3] ' + str(err) + ' [3]' + '[' + time.ctime() + ']' + '\n'))
                                break
                        a = a+1
                        logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                        logs.write(str('[' + time.ctime() + ']' + '[COUNT] ' + str(a) + ' [COUNT]' + '[' + time.ctime() + ']' + '\n'))
                        logs.close()
                    vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':'Первая партия банов готова!'})
                    logs.close()
                if(temp_out != 0):
                    members = vk.method('groups.getMembers', {'group_id':id, 'offset':temp_offset, 'count':temp_out})
                    for sub in members["items"]:
                        for group in gaysubs:
                            member = vk.method('groups.isMember', {'group_id':group, 'user_id':sub})
                            if(member == 1):
                                try:
                                    ban(id, sub)
                                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                                    logs.write(str('[' + time.ctime() + ']' + '[BAN] ' + str(sub) + ' [BAN]' + '[' + time.ctime() + ']' + '\n'))
                                except Exception as err:
                                    logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                                    logs.write(str('[' + time.ctime() + ']' + '[3] ' + str(err) + ' [3]' + '[' + time.ctime() + ']' + '\n'))
                                break
                        a = a+1
                        logs = open("/home/" + appname + "/mysite/logs.txt", "a", encoding='utf-8', errors='ignore')
                        logs.write(str('[' + time.ctime() + ']' + '[COUNT] ' + str(a) + ' [COUNT]' + '[' + time.ctime() + ']' + '\n'))
                        logs.close()
                    vka.method('messages.send', {'user_id':error_manager,'random_id':random.randint(0, 2147483647), 'message':'Вторая партия банов готова!'})
                    logs.close()
        return "ok"

if __name__ == "__main__":
    app.run()
