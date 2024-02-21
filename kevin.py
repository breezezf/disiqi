'''我的主页
下载 （注意版本）streamlit 1.28.2
运行后在输出中复制python -m“streamlit run ···.py”到终端按回车
如果终端无法输入，按Ctrl+C'''
import streamlit as st
from PIL import Image
page=st.sidebar.radio("饮料游戏",["关于我们","推荐游戏","轻功能-图片改色","词典","评论留言"])
def page_1():
    st.write("DrinkGame饮料游戏")
    st.write("一片游戏创作者自由耕耘的天地！")
def page_2():
    st.write("《DrinkDO饮料大作战2》")
    st.write("有事无事，来场试试！")
    st.write("https://shequ.codemao.cn/work/212942827")
def page_3():
    st.write(":sunglasses:轻功能-图片改色:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(["原图","处理效果1","效果2","效果3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
def img_change(img,rc,gc,bc):
    '''为page_3提供图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
if page=="关于我们":
    '''关于我们'''
    page_1()
elif page=="推荐游戏":
    '''推荐游戏'''
    page_2()
elif page=="轻功能-图片改色":
    '''轻功能-图片改色'''
    page_3()
elif page=="词典":
    '''词典'''
    pass
elif page=="评论留言":
    '''评论留言'''
    pass