from bs4 import BeautifulSoup
import streamlit as st
import importlib
import requests
import asyncio


base = 'https://www.acmicpc.net/problem/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com'
}

name_list = ["bigwave100" , "HwangInseok" , "jungsb0415" , "yjs2673", "hwlee", "kyuhyung", "wjm9765", "hyeonsang010716", "pinkgorae", "xxxiv-34"] 

name_module_map = {
    "bigwave100": "bigwave100.main",
    "HwangInseok": "HwangInseok.main",
    "jungsb0415": "jungsb0415.main",
    "yjs2673": "yjs2673.main",
    "hwlee": "hwlee.main",
    "kyuhyung": "kyuhyung.main",
    "wjm9765": "wjm9765.main",
    "hyeonsang010716": "hyeonsang010716.main",
    "pinkgorae": "pinkgorae.main",
    "xxxiv-34": "xxxiv_34.main",
}

def get_data(num):
    url = base + str(num)

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        problem_description = soup.select('#problem_description > p')
        problem_ul = soup.select('#problem_description > ul')
        input_description = soup.select('#problem_input > p')
        output_description = soup.select('#problem_output > p')
        sample_input = soup.select_one('#sampleinput1').text.strip()
        sample_output = soup.select_one('#sampleoutput1').text.strip()
        sample_i = soup.select("pre[id^=sample-input]")
        sample_o = soup.select("pre[id^=sample-output]")

        content = ""

        for description in problem_description:
            content += description.text.strip() + '\n\n' 

        for ul in problem_ul:
            content += ul.text.strip() + '\n\n' 

        content += "IN" + '\n'

        for in_description in input_description:

            content += in_description.text.strip() + '\n\n'

        content += "OUT" + '\n'

        for out_description in output_description:
            content += out_description.text.strip() + '\n\n'

        inputs = []

        outputs = []

        for i in range(len(sample_i)):
            inputs.append(sample_i[i].text.strip())
            outputs.append(sample_o[i].text.strip())

        return True , content , inputs , outputs

    else:
        return False , None , None , None


# ----- Main -----



st.set_page_config(page_title="알고리즘 프로젝트", page_icon="💬")

class Basic:

    def __init__(self):

        if "name" not in st.session_state:
            st.session_state["name"] = None

        if "session_disable" not in st.session_state:
            st.session_state["session_disable"] = True

        if "session_id_input_disable" not in st.session_state:
            st.session_state["session_id_input_disable"] = False
        
        if "problem_numbers" not in st.session_state:
            st.session_state["problem_numbers"] = None
            

    def session_enable(self):
        st.session_state["session_disable"] = False
        st.session_state["session_id_input_disable"] = True
        return

    def session_disable(self):
        st.session_state["session_disable"] = True
        st.session_state["session_id_input_disable"] = False
        return
        
    async def main(self):

        st.sidebar.divider()

        st.session_state["name"] = st.sidebar.selectbox("이름 선택", name_list , disabled=st.session_state["session_id_input_disable"])

        if st.session_state["name"]: 
            session_start = st.sidebar.button(
                "세션 시작",
                disabled=st.session_state["session_id_input_disable"],
                on_click=self.session_enable,
            )

            if session_start:
                name = st.session_state["name"]
                st.sidebar.info(f"{name}님 세션을 시작합니다.")

        else: 
            st.sidebar.warning("이름을 선택해주세요.")

        st.session_state["problem_numbers"] = st.chat_input(
            placeholder="문제 번호를 입력하세요.",
            disabled=st.session_state["session_disable"],
        )


        if st.session_state["problem_numbers"]:

            if st.session_state["name"] in name_module_map:
            
            
                user_module = importlib.import_module(name_module_map[st.session_state["name"]])
                
                solve = getattr(user_module, "solve")

                _, _, inputs, outputs = get_data(st.session_state["problem_numbers"])

                results = solve(inputs)
                st.write(f"## 문제: {st.session_state["problem_numbers"]}")
                st.chat_message("ai").write(outputs)
                st.chat_message("human").write(results)
            else:
                st.error("등록되지 않은 사용자입니다.")

            
                


if __name__ == "__main__":
    obj = Basic()
    asyncio.run(obj.main())