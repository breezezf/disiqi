import streamlit as st
from PIL import Image

page = st.sidebar.radio('首页', ['兴趣推荐', '图片改色', '智慧词典','留言板块'])

def page1():
    '''兴趣推荐'''
    with open('编程猫的梦想.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["电影推荐","游戏推荐","音乐推荐","书籍推荐","习题集推荐"])
    with tab1:
        st.write(':blue[电影推荐]')
        st.write(':red[(备注：排名仅为入站顺序)]')        
        st.write('(-----如有推荐请留言)')
        st.write('1. 《阿甘正传》',)
        st.image('屏幕截图 2024-02-20 170259.png')
        st.write('2. 《肖申克的救赎》',)
        st.image('屏幕截图 2024-02-20 171309.png')
        st.write('3. 《哈利波特与死亡圣器》')
        st.image('屏幕截图 2024-02-20 174938.png')
        st.write('4. 《异界》')
        st.image('异界.png')
        st.write('5. 《千星之城》')
        st.image('千星之城.png')
        st.write('6. 《星际穿越》')
        st.image('星际穿越.png')
    with tab2:
        st.write(':blue[游戏推荐]')
        st.write(':red[提示：游戏属于个人喜好，不爱请别伤害]')
        st.write('1. 原神')
        st.image('原神图片.png')
        st.write('2. 崩坏:星穹铁道')
        st.image('崩坏星穹铁道.png')
        st.write('3. 我的世界')
        st.image('我的世界.png')
        st.write('(如有推荐请留言)')
    with tab3:
        st.write(':blue[音乐推荐]')
        st.write('1. shadow of the sun')
        st.write('(如有推荐请留言)')
    with tab4:
        st.write(':blue[书籍推荐]')
        st.write(':grey[站主认为以下每本都是经典，如有可能建议都读读]')
        st.write('《天才在左，疯子在右》')
        st.image('天才在左疯子在右图片.png')
        st.write('《苏菲的世界》')
        st.image('苏菲的世界.png')
        st.write('《理想国》')
        st.image('理想国.png')
        st.write('《中国哲学简史》')
        st.image('中国哲学简史.png')
        st.write('《人生的智慧》')
        st.image('人生的智慧.png')
        st.write('《当尼采哭泣》')
        st.image('当尼采哭泣.png')
        st.write('《沉思录》')
        st.image('沉思录.png')
        st.write('(如有推荐请留言)')
    with tab5:
        st.write(':blue[习题集推荐]')
        st.write('《五年模拟，三年高考》')
        st.write('[示例图片为语文]')
        st.image('五年模拟三年高考-语文.png')
        st.write('(如有推荐请留言)')

def page2():
    '''图片改色'''
    st.write(":sunglasses:图片改色:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    if uploaded_file:
        # 获取图片文件的名称，类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)

        tab1,tab2,tab3,tab4 = st.tabs(["原色","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 2, 0, 1))

def page3():
    '''智慧词典'''
    pass
def page4():
    '''留言区'''
    pass

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
            img_array[x, y] = (r, g, b)
    return img

if page == '兴趣推荐':
    page1()
elif page == '图片改色':
    page2()
elif page == '智慧词典':
    page3()
elif page == '留言区':
    page4()