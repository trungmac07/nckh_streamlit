import streamlit as st

st.set_page_config(page_title="Web Tự Phê Bình")

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.imgur.com/b7cSlV2.jpg");
            background-size: cover;
            background-position: center;
            color: black; /* Đặt màu chữ mặc định cho toàn bộ trang */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {{
        color: white; /* Màu chữ trắng cho sidebar */
    }}
    .sidebar h1, .sidebar h2, .sidebar h3, .sidebar h4, .sidebar h5, .sidebar h6, .sidebar p {{
        color: white; /* Đảm bảo tất cả các tiêu đề và đoạn văn trong sidebar đều là trắng */
    }}
    .stSidebar > div:first-child {{
        padding-top: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📋 Menu Điều Hướng")
menu = st.sidebar.selectbox("Chọn mục bạn muốn xem", 
                            ["🏠 Trang chủ", "📚 Tri thức về tự phê bình", 
                             "📂 Tài nguyên", "🎬 Video Clips", 
                             "💬 Diễn đàn", "📝 Nhật ký cá nhân"])

def trang_chu():
    st.markdown("<h1 style='text-align: center; color: black;'>Chào Mừng Bạn</h1>", unsafe_allow_html=True)
    st.write("""
        <div style='text-align: center; font-size: 25px; color: black;'>
        Website này giúp bạn chia sẻ và tìm hiểu về tự phê bình cá nhân.<br>
        Bạn có thể viết nhật ký, chia sẻ và thảo luận với cộng đồng.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .caption {
            color: black;
            font-size: 25px;
            text-align: center;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
        <div class="center">
            <img src="https://i.imgur.com/4K8PmfB.jpg" alt="Tự phê bình là hành trình tự khám phá">
            <p class="caption">Tự phê bình là hành trình tự khám phá</p>
        </div>
    """, unsafe_allow_html=True)

def tri_thuc():
    st.markdown("<h2 style='color: black;'>Tri thức về Tự Phê Bình</h2>", unsafe_allow_html=True)
    st.write("Tìm hiểu về những bài viết và tài liệu giúp nâng cao nhận thức về tự phê bình.")
    st.text_area(" ", placeholder="Viết chia sẻ của bạn tại đây...", height=200)

def tai_nguyen():
    st.markdown("<h2 style='color: black;'>Tài Nguyên</h2>", unsafe_allow_html=True)
    st.write("Tài liệu và công cụ giúp quá trình tự phê bình của bạn hiệu quả hơn.")
    st.file_uploader(" ", type=["pdf", "docx"])

def video_clips():
    st.markdown("<h2 style='color: black;'>Video và Postcard về Tự Phê Bình</h2>", unsafe_allow_html=True)
    st.write("Các video giúp bạn nâng cao quá trình tự phê bình.")

def dien_dan():
    st.markdown("<h2 style='color: black;'>Diễn Đàn Thảo Luận</h2>", unsafe_allow_html=True)
    st.text_area(" ", placeholder="Nhập ý kiến tại đây...")

def nhat_ky():
    st.markdown("<h2 style='color: black;'>Nhật Ký Tự Phê Bình Cá Nhân</h2>", unsafe_allow_html=True)
    diary_entry = st.text_area(" ", placeholder="Viết nhật ký của bạn...", height=200)
    
    st.markdown(
    """
    <style>
    .stButton > button {
        color: white;
        border: none; 
        border-radius: 5px;  
        padding: 10px 20px;  
        font-size: 16px; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    if st.button("💾 Lưu Nhật Ký"):
        with open("diary.txt", "a") as f:
            f.write(diary_entry + "\n---\n")
        st.success("Nhật ký của bạn đã được lưu thành công!")

if menu == "🏠 Trang chủ":
    trang_chu()
elif menu == "📚 Tri thức về tự phê bình":
    tri_thuc()
elif menu == "📂 Tài nguyên":
    tai_nguyen()
elif menu == "🎬 Video Clips":
    video_clips()
elif menu == "💬 Diễn đàn":
    dien_dan()
elif menu == "📝 Nhật ký cá nhân":
    nhat_ky()
