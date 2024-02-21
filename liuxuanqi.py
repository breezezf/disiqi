'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典',
                                    '我的学习心得交流', '我的留言区'])

# 电影推荐
mag_movie = ':blue[电影推荐]'
movie_1 = ':red[《哈利波特》]'
zynr_1 = ':orange[主要内容]'
movie_hl = '''


                《哈利·波特》系列电影，是由美国华纳兄弟娱乐公司将JK罗琳所著的同名系列小说改拍成的八部电影，由
            丹尼尔·雷德克里夫、鲁伯特·格林特、艾玛·沃特森等主演的剧情片 。
                \n讲述的是年轻的巫师学生哈利·波特在霍格沃茨魔法学校前后六年的学习生活和冒险故事;第七部讲述的
            是哈利·波特在第二次巫界大战中被迫逃亡在外寻找魂器并消灭伏地魔的故事。
            '''
movie_2 = ':red[《长安三万里》]'
zynr_2 = ':orange[主要内容]'
movie_caswl = '''


                《长安三万里》以盛唐为背景，讲述安史之乱后，整个长安因战争而陷入混乱，身处局势之中的高适回忆
            起自己与李白的过往。剧情简介安史之乱后数年，吐蕃大军入侵西南，大唐节度使高适交战不利。长安岌岌可
            危。困守孤城的高适向监军太监回忆起自己与李白的一生往事。
                《长安三万里》塑造了大唐诗人的群像，在李白、高适、杜甫之外，还有贺知章、王维、王昌龄、郭子仪、
            岑参、张旭、哥舒翰......诗人们的集体登场，宛如历史天空中的群星闪耀在观众眼前。
            '''
bxwp_1 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 游戏推荐
mag_game = ':blue[游戏推荐]'
game_1 = ':red[我的世界]'
game_2 = ':red[王者荣耀]'
jdtc = ':orange[经典台词]'
game_wzry = '''


                一个人可以被毁灭，但绝不会被打败 ——————凯
                \n人生就是不停地比拼，你赢了别人就输了，别人赢了你就输了。——————狄仁杰
                \n决定了内心的正道，便毫无动摇。——————关羽
                \n天地与我并生,万物与我为宜。——————庄周
                \n雄鹰不及暴风者也，狼群不应长夜畏惧。——————成吉思汗
                '''
game_3 = ':red[和平精英]'
bxwp_2 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 书籍推荐
mag_book = ':blue[书籍推荐]'
book_1 = ':red[《钢铁是怎样炼成的》]'
zynr_3 = ':orange[主要内容]'
book_gtszylcd = '''


                    《钢铁是怎样炼成的》是苏联作家尼古拉·奥斯特洛夫斯基于1934年创作的一部现实主义小说，被誉
                为是社会主义文学的代表作之一。该小说主要讲述了主人公保尔·柯察金的成长历程，以及他如何在革命的
                熔炉中，逐步锻炼成为一位坚强的无产阶级战士。
                    \n小说的主旨是探讨人类社会发展与科技进步之间的关系。作者通过描写柯察金的成长经历，表现了革
                命斗争的艰辛与意义，强调了人的精神力量和意志力的伟大。同时，小说中也详细阐述了科技在社会发展中
                的重要作用，并对科技的发展进行了深入的思考和分析。
                '''
book_2 = ':red[《明朝那些事儿》]'
zynr_4 = ':orange[主要内容]'
book_mcnxs = '''


                历史小说《明朝那些事儿》主要讲述的是从1344年到1644年这三百年间关于明朝的一些故事。以史料为基
            础，以年代和具体人物为主线，并加入了小说的笔法，语言幽默风趣。对明朝十七帝和其他王公权贵和小人物的
            命运进行全景展示，尤其对官场政治、战争、帝王心术着墨最多，并加入对当时政治经济制度、人伦道德的演
            义。
            '''
book_3 = ':red[《上下五千年》]'
zynr_5 = ':orange[主要内容]'
book_sxwqn = '''


                主要内容:以时间为经，以事件和人物为纬，穿针引线，纵横交纵，从盘古开天辟地的传说开始，将中华
            上下五千年历史文化的精髓，展现，为读者提供了了解历史的捷径。清晰地勾勒出历史事件的来龙去脉和历史
            人物的真伪辩恶。
            '''
bxwp_3 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 习题集推荐
mag_exersice = ':blue[习题集推荐]'
exersice = ':red[《三年中考五年模拟》]'
bxwp_4 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 音乐推荐
mag_music = ':blue[音乐推荐]'
bxwp_5 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

# 图片推荐
mag_picture = ':blue[图片推荐]'
bxwp_6 = ':red[注意：本文仅个人喜好，不喜勿喷，谢谢配合！]'

def page_1():
    '''我的兴趣推荐'''
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["电影推荐", "游戏推荐", "书籍推荐",
                                             "习题集推荐", "音乐推荐", "图片推荐"])
    with tab1:
        st.write(mag_movie)
        st.write(movie_1)
        st.write(zynr_1)
        st.write(movie_hl)
        st.image('hl.jpg')
        st.image('fdm.jpg')
        st.write(movie_2)
        st.write(zynr_2)
        st.write(movie_caswl)
        st.image('caswlone.jpg')
        st.image('caswltwo.jpg')
        st.write(bxwp_1)
    with tab2:
        st.write(mag_game)
        st.write(game_1)
        st.image('wdsj.jpg')
        st.write(game_2)
        st.write(jdtc)
        st.write(game_wzry)
        st.write(game_3)
        st.image('hpjyone.jpg')
        st.image('hpjytwo.jpg')
        st.write(bxwp_2)
    with tab3:
        st.write(mag_book)
        st.write(book_1)
        st.write(zynr_3)
        st.write(book_gtszylcd)
        st.write(book_2)
        st.write(zynr_4)
        st.write(book_mcnxs)
        st.image('mcnxs.jpg')
        st.write(book_3)
        st.write(zynr_5)
        st.write(book_sxwqn)
        st.write(bxwp_3)
    with tab4:
        st.write(mag_exersice)
        st.write(exersice)
        st.image('wnzlsnmn.jpg')
        st.write(bxwp_4)
    with tab5:
        st.write(mag_music)
        with open('编程猫的梦想.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
        with open('Beijing_Bass.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
        with open('Last_Stop.mp3', 'rb') as f:
            mymp3 = f.read()
            st.audio(mymp3, format='audio/mp3', start_time=0)
        st.write(bxwp_5)
    with tab6:
        st.write(mag_picture)
        st.image('dog.jpg')
        st.image('dragon.jpg')
        st.image('hx.jpg')
        st.image('kr.jpg')
        st.image('xk.jpg')
        st.write(bxwp_6)
        
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("图片分享", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1,tab2,tab3,tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page_3():
    '''我的智能词典'''
    pass

def page_4():
    '''我的学习心得交流'''
    # 素材
    sc_1 = '''    
    
                古书有云:“学如逆水行舟，不进则退。”我也深有体会，它自然成为我的个人格言。学习如天上
            的云，一不小心就会然自己的知识被大地吸干，努力的成绩可都被别人来去了，自己却成为一无所有。
                \n“书中自有黄金屋，书中自有彦如玉。”在我的生活中，书是我的好朋友，床边、书桌、椅子，都
            有它的存在。在有空的时候看一看书，然紧张的大脑放松一下。在书的海洋遨游，然你受益匪浅。我
            平时爱在中午看一些散文，晚上看含有深刻道理的，体会、分析、感受、领悟其深刻的道理。
                \n“人的天才只是火花，要想使它成熊熊火焰，那就只有学习!学习。”它是我的助跑线，它让我知道:
            只有学习才能让人的天才成熊熊火焰，就算人没有天才，但有了学习就是有成功之路。
                \n讲到学习方法，我想用六个字来概括:“严格、严肃、严密。”这种科学的学习方法，除了向别人学
            习之外，更重要的是靠自己有意识的刻苦锻炼。如果你只会向别人学习，自己却不意识的刻苦锻炼，就
            如一颗没发芽的种子，只想快快长大，自己不主动在生活中锻炼，只会长得矮小。
                \n“复习是学习之母。”复习也是我的学习生活中最重要的一部分，也是我的学习方法之一。“学习后
            复习，让知识更巩固。”是我课后的名言，也是我的课后行动，因常言道“温故知新”。
                \n让我们赶快行动起来，找到自己的学习方法，感受学习的快乐，体验学习的幸福，领悟学习的道
            理吧!'''
    bxwp_7 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'

    sc_2 = '''

    
                对于学习，我们应该去适应它，而不是让它来适应我们。那我们应该怎样去适应学习呢?我觉得我们应
            该做到以下三点:
            \n
            一、学得平衡
                \n学习，首先要做到的就是平衡。不能说你喜欢这一学科，就一味地学习这一学科，而放弃其它学科。
            但也不能因为你这一学科较弱而总学习这一学科，自己较强的学科却不去学习。这些都是不平衡的现象，到
            最后只会是两手空空。我们应该做到科科必学，科科平衡。当然，如果自己的弱势学科实在是补不上，可以
            采取“扬长避短”的学习方法，让自己的优收起势字科学得更好，以弥补自己的不足。
            \n
            二、学得透彻 
                \n学习，就是要有敢问敢钻研的精神。我是一个提倡“不懂就问”的学习方法的人。要想学得透彻，不光
            上课要认真听，课后还要找出不懂的地方问老师，与同学探讨，力求把每一个不懂的地方都弄懂，每一个知
            识点都学懂。不能将不懂的知识都藏起来，要记住把不懂的知识变成为自己的知识，是一件有利于自己的事。
            \n
            三、学得有趣 
                \n当你把所有的知识都学懂之后，你会发现，原来那一道道如拦路虎般的练习题都变成了笑脸在向你招
            手。学得有趣就是要在学得透彻的基础上更进一步。把做练习题变得像做游戏一样有趣，那你的学习之旅就
            会变得既轻松又愉快了。
                \n学习是一件困难而又轻松的事，只要你掌握一定的学习方法与态度，就能化难为易，轻松学习。
            '''
    bxwp_8 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'
    
    sc_3 = '''
    
    
                成功没有捷径，只有靠自己的努力和付出才能取得胜利。在学习的路程上，有着许多困难和挫折，有人没
            有勇气度过，从而浑浑噩噩度过一生，有人则披荆斩棘，尝到了胜利的果实。
                \n爱因斯坦说过:“我认为，对一切来说，只有热爱才是最好的教师，它远远超过责任感。”只有对学习产
            生兴趣，才能更认真的学习。比如某些同学，根据自己的喜好来学习，弱科放在一旁不管，结果偏科很严重。
            要想办法对自己薄弱的科目产生兴趣，并学习它。老师经常对我们说“科要多练，文科要多读”。我们应该多读
            写，“知之为知之，不知为不知，是知也”，遇到不会的题目，千万不要不懂装懂。
                \n“预则立，不预则废”每次课前都要先预习下，下节课学习的内容，不但能使我们的自主学习能力有很大
            的提高，还能排除对老师的依赖。如果不课前预习，就会比别人慢一拍，造成课堂学习上“手忙脚乱”的窘相。
                \n“温故而知新”当老师讲完课之后，我们应该做到即时复习，巩固学过的知识，记忆得更牢固。我们也可
            以试试为自己制定一个学习计划，但不要天马行空，纸上谈兵，否则到头来还是竹篮打水一-一场空。
                \n学习方法因人而异，各不相同，愿同学们找到适合自己的学习方法，在学习生涯中绘上精彩的一笔!
            '''
    bxwp_9 = ':red[注意：本文仅供参考，不喜勿喷，谢谢配合！]'

    tab1,tab2,tab3 = st.tabs(["学习心得1", "学习心得2", "学习心得3"])
    with tab1:
        st.write(sc_1)
        st.write(bxwp_7)
    with tab2:
        st.write(sc_2)
        st.write(bxwp_8)
    with tab3:
        st.write(sc_3)
        st.write(bxwp_9)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img
    
def page_5():
    '''我的留言区'''
    pass
    
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的学习心得交流':
    page_4()
elif page == '我的留言区':
    page_5()


