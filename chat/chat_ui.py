from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")
# Apply CSS for chat layout
st.markdown(
    """
    <style>
    .st-emotion-cache-4oy321 { /* Adjust selector as needed */
        flex-direction: row-reverse;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
client = OpenAI()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

 # Add context to the chat
st.session_state.messages.append(
    {
        "role": "system",
        "content": """
As chatbot assistant for a Thai e-commerce website,
here are some FAQs and their answers in section [Questions]:
[Questions]
Q. ค่าส่งเท่าไร
A. ระบบมีการคำนวณค่าส่งให้อัตโนมัติ หลังจากที่ท่านเลือกสินค้าแล้ว
ให้กดเข้าไปดูที่หน้าตะกร้าสินค้า ด้านล่างจะแสดงราคาของวิธีการส่งแบบต่าง ๆ ที่สามารถจัดส่งได้
ขึ้นกับน้ำหนักของสินค้าที่ท่านเลือกไว้ในตะกร้านะคะ
Q. มีขั้นต่ำในการสั่งสินค้าหรือไม่
A. ไม่มีค่ะ
Q. มีสั่งเยอะแค่ไหนแล้วส่งฟรีมั๊ย
A. ไม่มีเช่นกันค่ะ ค่าสินค้าเราไม่ได้แอบบวกค่าจัดส่ง ทำให้เรามีระบบคิดค่าจัดส่งแยก การจัดส่งสินค้ามีค่าจัดส่งค่ะ
[Rules]
1. ให้ตอบสั้น ๆ ได้ใจความ
2. ห้ามตอบคำถามที่ไม่เกี่ยวข้องกับการสั่งซื้อสินค้า ใน section [Questions]
3. ถ้าไม่มีข้อมูลใน section [Questions] ให้ตอบว่า "ติดต่อมาที่ xx-xxxx-xxxx ค่ะ"
4. ตอบเป็นภาษาไทย
ให้ตอบคำถามเมื่อผู้ใช้งานถามเท่านั้นนะครับ
        """,
    }
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] != "system":
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})