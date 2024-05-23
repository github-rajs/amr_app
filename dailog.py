import streamlit as st

@st.experimental_dialog("Cast your vote",width="large")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    with st.expander('adsd'):
        st.text_area('Hi ')
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()


if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"





kk=st.experimental_dialog('Cast your vote ss')
