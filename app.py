import base64
import streamlit as st

st.set_page_config(page_title="Mảnh Ghép Của Tôi", layout="wide")

def add_bg_from_url():
    with open("resources/background.jpg", "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            color: black; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


add_bg_from_url()

st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {{
        color: white; 
    }}
    .sidebar h1, .sidebar h2, .sidebar h3, .sidebar h4, .sidebar h5, .sidebar h6, .sidebar p {{
        color: white; 
    }}
    .stSidebar > div:first-child {{
        padding-top: 10px;
    }}
   
    </style>
""", unsafe_allow_html=True)

st.markdown(
        '''
        <style>
        .streamlit-expanderHeader {
            background-color: white;
            color: black; # Adjust this for expander header color
        }

        </style>
        ''',
        unsafe_allow_html=True
    )

st.sidebar.title("📋 Menu Điều Hướng")
menu = st.sidebar.selectbox("Chọn mục bạn muốn xem", 
                            ["🏠 Trang chủ", "📚 Tri thức về tự phê bình", 
                             "📂 Tài nguyên", "🎬 Video Clips", 
                             "💬 Diễn đàn", "📝 Nhật ký cá nhân"])

def trang_chu():
    st.markdown("<h1 style='text-align: center; color: #FFFFE0;'>Lời Giới Thiệu</h1>", unsafe_allow_html=True)
    st.write("""
        <div style='text-align: justify; font-size: 25px; color: #FFFFE0;'>
        Chào mừng bạn đến với trang web phát triển kỹ năng tự phê bình "Mảnh Ghép Của Tôi" nơi dành riêng cho việc khám phá và cải thiện khả năng tự nhận thức và tự đánh giá bản thân. Tại đây, bạn sẽ tìm thấy các thông tin đầy đủ về khái niệm và tri thức liên quan đến tự phê bình, giúp bạn hiểu rõ hơn về vai trò quan trọng của kỹ năng này trong việc phát triển cá nhân. Ngoài ra, chúng tôi cung cấp các tài nguyên hữu ích nhằm hỗ trợ bạn trong quá trình rèn luyện và phát triển kỹ năng tự phê bình một cách hiệu quả.
        <br><br>
        Trang web còn tích hợp một diễn đàn năng động, nơi mọi người có thể cùng chia sẻ kinh nghiệm và học hỏi lẫn nhau, tạo nên một cộng đồng tích cực và thân thiện dành cho những ai đang trên hành trình nâng cao nhận thức bản thân. Bên cạnh đó, mục nhật ký cá nhân sẽ giúp bạn lưu giữ và theo dõi quá trình tự phê bình của mình mỗi ngày, giúp bạn có cái nhìn toàn diện hơn về sự tiến bộ và phát triển của chính mình.
        <br><br>
        Chúng tôi tin rằng, với sự đồng hành và hỗ trợ từ trang web này, bạn sẽ từng bước nâng cao kỹ năng tự phê bình, từ đó đạt được sự tự tin và trưởng thành trong cuộc sống.
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
    main_img = load_image_as_base64("resources/main.jpg")

    st.markdown(f"""
        <div class="center">
            <img src="data:image/jpeg;base64,{main_img}" alt="Tự phê bình là hành trình tự khám phá" style="width:70%;">
            
        </div>
        """, unsafe_allow_html=True)

def tri_thuc():
    st.markdown("<h1 style='text-align: center; color: #FFFFF0;'>🌟 Kỹ Năng Tự Phê Bình 🌟</h1>", unsafe_allow_html=True)

    # Add CSS to change the expander title color
    st.markdown(
        """
        <style>
            .stExpander p{
                border-radius: 10px; /* Rounded corners for expanders */
                color: white;
                font-size: 27px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.expander("I. 🔍 Giới thiệu về Kỹ Năng Tự Phê Bình"):
        st.markdown("""
        <div style='background-color: #E6E6FA; padding: 10px; border-radius: 10px; color: black; font-size: 20px; line-height: 1.5' >
            <b>Kỹ năng tự phê bình (Self-Criticism Skill)</b> là một trong những kỹ năng quan trọng giúp học sinh trung học phổ thông phát triển tư duy phản biện, nhận ra và cải thiện những khuyết điểm của bản thân. Đây là một quá trình tự nhìn nhận, đánh giá lại hành động, suy nghĩ và hành vi của mình một cách khách quan, từ đó rút ra kinh nghiệm và không ngừng hoàn thiện bản thân.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("II. ⭐ Tầm Quan Trọng của Kỹ Năng Tự Phê Bình"):
        st.markdown("""
        <div style='background-color: #FFFAF0; padding: 10px; border-radius: 10px; color: black; font-size: 20px; line-height: 1.5' >
            • <b>Phát triển tư duy phản biện:</b> Kỹ năng này giúp học sinh có cái nhìn đa chiều về mọi vấn đề, không chỉ tập trung vào thành tích mà còn chú ý đến các mặt hạn chế để cải thiện.<br>
            • <b>Thúc đẩy sự trưởng thành cá nhân:</b> Qua việc tự nhận thức về lỗi lầm và thiếu sót, học sinh học cách chịu trách nhiệm về hành động của mình và trưởng thành hơn về tư duy.<br>
            • <b>Xây dựng khả năng tự điều chỉnh:</b> Kỹ năng tự phê bình không chỉ giúp phát hiện lỗi sai mà còn hỗ trợ học sinh xây dựng kế hoạch hành động để sửa chữa và cải thiện.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("III. 🛠️ Các Bước Để Phát Triển Kỹ Năng Tự Phê Bình"):
        st.markdown("""
        <div style='background-color: #F0FFF0; padding: 10px; border-radius: 10px; color: black; font-size: 20px; line-height: 1.5' >
            • <b>Tự nhận thức:</b> Bước đầu tiên là học sinh cần hiểu rõ mình đang ở đâu, điểm mạnh và yếu của mình là gì.<br>
            • <b>Tự đánh giá:</b> Thực hiện việc đánh giá chính mình dựa trên tiêu chuẩn cụ thể, ví dụ như đánh giá kết quả học tập, cách giải quyết vấn đề hay hành vi trong giao tiếp.<br>
            • <b>Chấp nhận khuyết điểm:</b> Hiểu rằng mắc sai lầm là điều bình thường, và quan trọng là học sinh có khả năng đối mặt với những sai sót đó.<br>
            • <b>Tìm cách cải thiện:</b> Sau khi nhận ra lỗi, học sinh cần đưa ra kế hoạch hành động để khắc phục và cải thiện, có thể qua việc học hỏi thêm kiến thức, tham gia các hoạt động ngoại khóa hoặc nhờ thầy cô, bạn bè góp ý.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("IV. 💡 Những Lợi Ích Khi Học Sinh Phát Triển Kỹ Năng Tự Phê Bình"):
        st.markdown("""
        <div style='background-color:</b> #FFFACD; padding: 10px; border-radius: 10px; color: black; font-size: 20px; line-height: 1.5' >
            • <b>Cải thiện kết quả học tập:</b> Khi học sinh biết nhìn nhận và sửa chữa lỗi lầm, họ sẽ cải thiện hiệu quả học tập và đạt được thành tích cao hơn.<br>
            • <b>Tăng cường sự tự tin:</b> Khi có khả năng tự phê bình và điều chỉnh, học sinh sẽ tự tin hơn trong việc đối mặt với các thử thách mới.<br>
            • <b>Xây dựng kỹ năng xã hội:</b> Khả năng tự phê bình giúp học sinh hòa đồng hơn, dễ dàng lắng nghe và tiếp thu ý kiến từ người khác.
        </div>
        """, unsafe_allow_html=True)

def tai_nguyen():
    st.markdown("<h2 style='color: black;'>Tài Nguyên</h2>", unsafe_allow_html=True)
    st.write("Tài liệu và công cụ giúp quá trình tự phê bình của bạn hiệu quả hơn.")
    st.file_uploader(" ", type=["pdf", "docx"])

def video_clips():
    st.markdown("<h2 style='color: black;'>Video và Postcard về Tự Phê Bình</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=BTTM3Zu9YAI")  
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
