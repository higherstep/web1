'''
随便聊天喽~
注：先在设置里开启终端，运行后复制输出里的话（右键复制），
点击终端，在白空格后写python -m (复制在这里)
然后按下enter，即运行
表情网站：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
github官网:https://github.com
streamlit官网:https://streamlit.io
网易邮箱：https://mail.163.com/
制作の网站の网址：https://zwfy7py3iwxqczlvihxboa.streamlit.app/
'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典', '我的留言区', '我的不智慧词典'])
def page1():
    with open('八年五班《大香蕉》伴奏.MP3','rb') as f:
        mymp3=f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        st.image('bing_image_5.png')
        st.write('┗|｀O′|┛ 嗷~~')
        st.write('( ͡• ͜ʖ ͡• )')
        
def page2():
    st.write(':chicken::rooster:图片处:cat2:理工具:rooster::chicken:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg', 'mp3', 'mp4'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
        
def page3():
    '''我的智能词典'''
    st.write(':full_moon:智能词典:new_moon:')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#')
    word_dict={}
    for i in word_list:
        word_dict[i[1]]=[int(i[0]),i[2]]#单词：[计数， 中文]
    with open('check_out_times.txt', 'r',encoding='utf-8') as f:
        time_list=f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#')
        
    time_dict={}
    for i in time_list:
        time_dict[int(i[0])]=int(i[1])
             
    word=st.text_input('请输入你想查询的单词：')
    if word in word_dict:
        st.write(word_dict[word])
        n=word_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        with open('check_out_times.txt', 'w',encoding='utf-8') as f:
            message=''
            for k,v in time_dict.items():
                message += str(k)+'#'+str(v)+'n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数:',time_dict[n])
        
        if word=='python':
            st.code('''#恭喜你触发了彩damn，这是一行pythondamn码！
                    print("hello world!")''')
        if word=='winter':
            st.snow()
        if word=='birthday':
            st.balloons()
        if word=='title':
            st.title('ZHYI')
        if word=='victory':
            st.success('恭喜你恭喜你啦！')
        if word=='warn':
            st.warning('in_kun is coming!')
        if word=='error':
            st.error('外币八部')
        if word=='information':#提示
            st.info('呦西')
        if word=='wait':
            with st.spinner('WaItInG.......'):
                time.sleep(114514)
            st.success('恭喜你成功啦！')
            
def page4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split('#')
    for i in message_list:
        if i[1]=='ikun':
            with st.chat_message('🐔'):
                st.write(i[1],':',i[2])#1为姓名2为留的言
        elif i[1]=='小猫捞底':
            with st.chat_message('🐱'):
                st.write(i[1],':',i[2])#1为姓名2为留的言
                
    name=st.selectbox('我是...' , ['ikun','小猫捞底'])
    new_message=st.text_input('输入想要说的话:...')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in message_list:
                message += i[0]+'#'+i[1]+"#"+i[2]+'\n'
            message=message[:-1]
            f.write(message)
    
def img_change(img, rc, gc, bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def page5():
    '''我的智能词典'''
    st.write(':full_moon:不智能词典:new_moon:')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split('#')
    word_dict={}
    for i in word_list:
        word_dict[i[1]]=[int(i[0]),i[2]]#单词：[计数， 中文]
    with open('check_out_times.txt', 'r',encoding='utf-8') as f:
        time_list=f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#')
        
    time_dict={}
    for i in time_list:
        time_dict[int(i[0])]=int(i[1])
             
    word=st.text_input('请输入你想查询的单词：')
    if word in word_dict:
        with st.spinner('WaItInG.......'):
                time.sleep(114514)
            st.success('恭喜你成功啦！')
    elif:
        with st.spinner('WaItInG.......'):
                time.sleep(114514)
            st.success('恭喜你成功啦！')
            
    
if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '我的不智慧词典':
    page5()
