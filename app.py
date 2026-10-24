import streamlit as st

st.set_page_config(page_title="My webapp", page_icon="https://i.pinimg.com/736x/aa/8c/23/aa8c23121ad14dfdacc93dbf2e925a5c.jpg", layout="wide")

st.title("Nice to meet you on my webapp")

tab1, tab2 = st.tabs(["About me", "My tool"])

with tab1:
    st.header("Meeting the author")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.pinimg.com/736x/08/ed/f0/08edf05148b0129ff7ea7e8a431d5f6d.jpg", width=400)
    with col2:
        st.subheader("Hello!, I am a future Python Developer!")
        st.write("I study at small Acadamy IT Step. I make cool webapps and learn streamlit.")

        with st.container():
            st.info("Contacts for conecting")
            st.markdown("- GitHub: [My profile](https://github.com)")
            st.markdown("- E-Mail: ariana@itstep.org")

with tab2:
    st.info("In developing")