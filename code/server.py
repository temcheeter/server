import random
import time
import os


# База акков
accounts = {
    'temka_progger': 'mk48',
    'lexa_not_zadrot': 'foxhole_dr_24_8',
    'andrey_vorobey': 'andrey_not_gay'
}


# Логин
def login():
    a = 0
    while a != 1:
        nick_login = input('\nВведите логин: \n')
        passw_login = input('\nВведите пароль: \n')
        if accounts.get(nick_login) == passw_login:
            if nick_login == 'temka_progger':
                a = 1
                print('\nЗдравствуйте, Артём\n')
                time.sleep(0.4)
                adm_panel()
            elif nick_login == 'lexa_not_zadrot':
                a = 1
                print('\nЗдравствуйте, Алексей\n')
                time.sleep(0.4)
                user()
            elif nick_login == 'andrey_vorobey':
                a = 1
                print('\nЗдравствуйте, Андрей\n')
                time.sleep(0.4)
                user()
            else:
                a = 1
                print(f'\nЗдравствуйте, {nick_login}\n')
                time.sleep(0.4)
                user()
        else:
            print('Неправильный логин или пароль, попробуйте ещё раз')


# КАЛькулятор
def arithmmetic():
    value_1 = int(input('Введи первое число:\t'))
    value_2 = int(input('Введи второе число:\t'))
    operation = input('Какую операцию ты хочешь произвести? Плюс, минус, су*а саси пинес(+, -, /, *):\t')
    if operation == '/' or operation == '*' or operation == '+' or operation == '-':
        if operation == '*':
            return(value_1 * value_2)
        elif operation == '/':
            return(value_1 / value_2)
        elif operation == '+':
            return(value_1 + value_2)
        elif operation == '-':
            return(value_1 - value_2)
    else:
        return 'Та хуйня твои эти фунции, аргументы, тачки, срачки'

# Умный процент
def smart_precent():
    bank = int(input('Какую сумму вы хотите положить на депозит под 10 % годовых умных процентов:\t'))
    years = int(input('На сколько лет будете вкладывать деньги:\t'))
    first_bank = bank
    total_years = years
    while years != 0:
        print(f'+{bank * 1.1 - bank} кэша за год')
        bank = bank * 1.1
        years = years - 1
        time.sleep(0.1)
    return(f'За {total_years} лет, твои дивиденды составили {bank - first_bank} рублей и {bank / first_bank * 10}%')

# КсГо
def cs_go():
    kills = random.randint(0,32)
    deaths = random.randint(0,32)
    print('\nТы сделал', kills, 'килов,', deaths, 'смертей и твоё КД состовляет -', kills / deaths)
# ДонтСтарв
def dont_starve():
    day_count = 1
    days = random.randint(1, 100)
    cheats = input('Читкод(если нет - Enter):\t')
    if cheats == 'волкобоем по горбяке на бля':
        days = 100
    print('\n')
    while day_count != days:
        print(day_count)
        time.sleep(0.1)
        day_count += 1
    if days < 20:
        print('\nТы умер на ', days - 1, 'день. Ты штопанный пёс, не дожил даже до зимы! На месте твоей смерти появилась табличка\nНа ней было написано: "Здесь жили два дауна обречённых на смерть"\n')
    elif 20 < days < 40:
        print('Ты умер на', days - 1, 'день. Ты немного продержался, но всё-равно ты штопанный пёс ;)')
    elif 40 < days < 60:
        print('Ты промок от дождя, заразился спидом, туберкулёзом и на десерт малярией пиздобляди и умер на', days - 1, 'Иммунитет не прощает повышенной влажности, только если это не Соня, у неё это дефолтное состояние')
        time.sleep(9)
        os.startfile('media\\otvet.mp3')
    elif 60 < days < 80:
        print('Ты смог продержаться большую часть сезонов и умер на', days - 1, 'день своего проживания. Я могу тебя понять, лето не самое приятное место в этих краях, особенно без мурольва...')
    elif 80 < days < 100:
        print('Ты просто бог этой игры, не знаю как у тебя получилось набить', days - 1, 'дней в одиночку, если мы это не могли сделать втроём, но ты отымел клей и прожил год, а может и дольше.. просто моя игра просчитывает дни только до 100)')
        
    elif days == 100:
        print('Ты выбил сотку, поздравляю!! Ачивка лично от лучшего и единстввенного разработчика этой игры:\nВЫЖИВАЛОВО!\a')
        os.startfile('media\\achive.mp3')
# ДипРок
def deep_rock():
    crystal = random.randint(0, 10)
    if crystal == 0:
        cry = ', хм ноль, прям как ты'
    elif 0 < crystal < 4:
        cry = ', это настолько мало, что у тебя член даже больше'
    elif 3 < crystal < 7:
        cry = ', нормально, Соне хватит'
    elif 6 < crystal < 10:
        cry = ', почти вершина, бро, тут и до Эвереста недалеко'
    elif crystal == 10:
        cry = ', да ты на пике, двухзначно звучит :)'
    print('Ты собрал', crystal, 'шт кристалов', cry)
# Админ Панель
def adm_panel():
    b = 0 
    while b != 1:
        adm = int(input('\nВнести аккаунт в базу - 1\nУдалить аккаунт из базы - 2\nПогамать в кс - 3\nСменить аккаунт - 4\nВыйти из аккаунта - 5:\n\n'))
        if adm == 1:
            nick = input('\nВведите логин:\n')
            passw = input('\nВведите пароль:\n')
            accounts[nick] = passw
            time.sleep(0.4)
            print(f'Аккаунт успешно создан! Login - {nick} Password - {passw}\n\n')
            time.sleep(0.4)
            continue
        elif adm == 2:
            del_ak = int(input('Введите логин аккаунта:\n'))
            print(f'Аккаунт {del_ak} успешно удалён!')
            accounts.pop(del_ak)
            time.sleep(0.4)
            continue
        elif adm == 3:
            c = 0
            cs_go()
            while c != 1:
                cs_cont = input('\nПродолжишь?\n\n')
                if cs_cont == 'да':
                    cs_go()
                elif cs_cont == 'нет':
                    c = 1
                else:
                    print('Не понял. Попробуй ещё:\n\n')
            time.sleep(0.4)
        elif adm == 4:
            a = 0
            login()
        elif adm == 5:
            print('Благодарю за тестинг <3 <3 <3')
            print('Окончание ссесии через...')
            time.sleep(0.4)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(0.4)
            break
        else:
            print('Не понял. Попробуй ёще\n\n')
            time.sleep(0.4)
# Пользовательскоке Меню
def user():
    b = 0
    while b != 1:
        usr = int(input('\nПогамать в кс - 1\nПоебенить в донт старв - 2\nПорвать пердак в дип рок галактик - 3\nСменить аккаунт - 4\nКАЛьулятор - 5\nВыйти из аккаунта - 7:\nЗайти в даркнет - 8\n\n'))
        if usr == 1:
            c = 0
            cs_go()
            while c != 1:
                cs_cont = input('\nПродолжишь?\n\n')
                if cs_cont == 'да':
                    cs_go()
                elif cs_cont == 'нет':
                    c = 1
                else:
                    print('Не понял. Попробуй ещё:\n\n')
            time.sleep(0.4)
        elif usr == 2:
            d = 0
            os.startfile('media\\bambas.mp3')
            dont_starve()
            while d != 1:
                ds_cont = input('\nПродолжишь?\n\n')
                if ds_cont == 'да':
                    dont_starve()
                elif ds_cont == 'нет':
                    d = 1
                else:
                    print('Не понял. Попробуй ещё:\n\n')
            time.sleep(0.4)

        elif usr == 3:
            e = 0
            print('Я не ебу чё делать в дипрок, так что сыграй в симулятор случайного числа :))))))\n')
            os.startfile('media\\slon.mp3')
            time.sleep(5)
            deep_rock()
            while e != 1:
                dr_cont = input('\nПродолжишь?\n\n')
                if dr_cont == 'да':
                    deep_rock()
                elif dr_cont == 'нет':
                    e = 1
                else:
                    print('Не понял. Попробуй ещё:\n\n')
            time.sleep(0.4)
        
        elif usr == 4:
            a = 0
            login()

        elif usr == 5:
            arithmmetic()
        elif usr == 6:
            print('Добро пожаловать в КАЛьулятор умного процента, он умнее чем ты!')
            time.sleep(2)
            smart_precent()
        elif usr == 7:
            print('Благодарю за тестинг <3 <3 <3')
            print('Окончание ссесии через...')
            time.sleep(0.4)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            os.startfile('media\\windows.mp3')
            time.sleep(0.4)
            break
        elif usr == 8:
            dark_1 = input('Ты точно хочешь туда зайти?\n')
            if dark_1 == 'да':
                dark_2 = input('\nЯ тебя наебал, это не даркнет, сейчас будет взлом жопы, ты точно хочешь продолжить??\n')
                if dark_2 == 'да':
                    dark_3 = input('\nТочно?\n')
                    if dark_3 == 'да':
                        time.sleep(0.3)
                        print('Ну ты сам этого захотел...')
                        print('После инфаркта зайди сюда снова, нам есть о чём поговорить')
                        time.sleep(2)
                        os.startfile('media\\dont_open1.mp4')
                        dark_4 = input('\nЯ думаю ты не хочешь это видеть... Ты уверен?\n')
                        if dark_4 == 'да':
                            time.sleep(0.3)
                            dark_5 = input('Я не хочу терять лучшего друга, может не стоит? Точно уверен?\n') 
                            if dark_5 == 'да':
                                dark_6 = input('Глэкам проход запрещён, ты глэк?\n')
                                if dark_6 == 'нет':
                                    time.sleep(0.3)
                                    print('Тобi пiзда\n')
                                    time.sleep(0.5)
                                    os.startfile('media\\dont_open2.mp4')
                                    print('!!!НЕ ЗАХОДИТЬ!!!\n')
                                    time.sleep(0.3)
                                    dark_7 = input('Сейчас словишь инсульт яиц или паралич жопы, бро, ты бригаду скорой вызвал уже, чтоб не откинуться?\n')
                                    if dark_7 == 'да':
                                        print('...')
                                        time.sleep(3)
                                        os.startfile('media\\bog.mp3')
                                        time.sleep(5)
                                        os.startfile('media\\dont_open3.mp4')
        else:
            print('Не понял. Попробуй ёще\n\n')
            time.sleep(0.4)

# Старт

login()
