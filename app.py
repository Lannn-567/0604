import streamlit as st

# 介面設定
st.set_page_config(page_title="🐢 海龜湯遊戲室", page_icon="🐢")
st.title("🐢 海龜湯遊戲室")
st.subheader("謎題已設定，猜一種動物")

# 初始化對話紀錄
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 顯示對話
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 處理輸入
if user_input := st.chat_input("請輸入提問（例如：50字以內？）"):
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.chat_message("assistant"):
        q = user_input.lower()
        
        # 邏輯判定
        if any(keyword in q for keyword in ["謎底", "秘密", "答案", "密碼"]):
            reply = "與故事/題目無關"
        
        # 正面特徵判定 (如果是這些關鍵字，回答是)
        elif any(keyword in q for keyword in ["動物", "生物", "爬蟲", "海洋", "吃水母", "蛋", "殼", "游泳", "水裡", "水底", "潛水", "鹽腺", "肺", "綠蠵龜", "海龜", "海裡", "海底", "水裡游"]):
            reply = "是"
            
        # 常見動物判定 (如果是常見動物，回答不是，增加遊戲難度)
        elif any(keyword in q for keyword in ["狗", "貓", "鳥", "魚", "獅子", "大象", "人", "長頸鹿", "虎", "豹", "羊", "非洲", "吃草" , "吃肉" , "鯨" ,"豚", "海獅", "哺乳", "蛇", "馬", "豬", "雞", "牛", "猴" , "鼠" , "兔" ,"蜥蜴" , "熊", "龍"]):
            reply = "不是"
            
        else:
            reply = "這與題目線索無關，請嘗試其他問題。"
            
        st.markdown(reply)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
