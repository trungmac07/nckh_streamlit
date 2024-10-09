import base64
import streamlit as st

diary_data = {
    "2024-10-09": {
        "event": "Hôm nay, trong buổi thuyết trình nhóm, tôi không chuẩn bị kỹ lưỡng nội dung và khi đến lượt mình trình bày, tôi đã ấp úng và không truyền đạt được ý chính. Điều này khiến buổi thuyết trình không đạt được hiệu quả cao.",
        "emotion": "Tôi cảm thấy khá xấu hổ và lo lắng khi nhận ra rằng sự chuẩn bị của mình không đầy đủ. Tôi cũng có chút tự ti về khả năng giao tiếp của mình.",
        "flaw": "Thiếu sự chuẩn bị và chưa luyện tập thuyết trình trước. Không kiểm soát được cảm xúc khi đứng trước đám đông.",
        "lesson": "Cần dành nhiều thời gian hơn để chuẩn bị và rèn luyện kỹ năng thuyết trình. Trước khi lên trình bày, nên luyện tập với bạn bè hoặc trước gương để kiểm soát tốt hơn.",
        "improvement_plan": "Trong tương lai, tôi sẽ đặt lịch dành ít nhất 2 tiếng để chuẩn bị và thực hành trước mỗi buổi thuyết trình. Đồng thời, tôi sẽ tham gia các hoạt động giúp tăng cường kỹ năng giao tiếp như thảo luận nhóm."
    },
    "2024-10-10": {
        "event": "Tôi đã cãi nhau với một người bạn vì những bất đồng nhỏ. Thay vì bình tĩnh giải quyết vấn đề, tôi đã nổi giận và nói những lời không hay.",
        "emotion": "Sau khi cãi nhau, tôi cảm thấy rất hối hận và nhận ra rằng mình đã để cảm xúc lấn át lý trí.",
        "flaw": "Không kiềm chế được cảm xúc và thiếu khả năng giao tiếp trong tình huống căng thẳng.",
        "lesson": "Mỗi khi gặp bất đồng, thay vì phản ứng ngay lập tức, tôi cần giữ bình tĩnh và lắng nghe ý kiến của đối phương một cách cẩn thận.",
        "improvement_plan": "Tôi sẽ học cách kiểm soát cảm xúc tốt hơn bằng cách thực hành thiền và tham gia các lớp học kỹ năng giao tiếp. Tôi cũng sẽ nhắn tin xin lỗi bạn và hẹn gặp mặt để giải quyết vấn đề."
    },
    "2024-10-11": {
        "event": "Hôm nay, tôi lãng phí gần hết một buổi sáng chỉ để lướt mạng xã hội và không làm được việc gì hiệu quả.",
        "emotion": "Tôi cảm thấy thất vọng về bản thân vì đã không quản lý thời gian tốt và để lỡ những công việc quan trọng.",
        "flaw": "Thiếu kỷ luật và dễ bị phân tâm bởi những việc vô bổ.",
        "lesson": "Cần có kế hoạch sử dụng thời gian cụ thể và biết nói 'không' với những điều làm mất tập trung.",
        "improvement_plan": "Tôi sẽ thiết lập thời gian cụ thể cho việc kiểm tra mạng xã hội và giới hạn mỗi ngày chỉ 30 phút. Ngoài ra, tôi sẽ lên danh sách công việc cần làm và cam kết hoàn thành từng nhiệm vụ trong ngày."
    },
    "2024-10-12": {
        "event": "Trong buổi làm việc nhóm, tôi không chủ động đóng góp ý kiến và chỉ ngồi nghe người khác thảo luận.",
        "emotion": "Tôi cảm thấy mình lạc lõng và thiếu tự tin khi không dám nêu ra quan điểm cá nhân.",
        "flaw": "Thiếu sự tự tin và chủ động trong giao tiếp, khiến tôi không có tiếng nói trong nhóm.",
        "lesson": "Tôi cần cải thiện khả năng giao tiếp và học cách chủ động chia sẻ suy nghĩ của mình, ngay cả khi lo lắng bị đánh giá.",
        "improvement_plan": "Tôi sẽ tham gia thêm các buổi học về phát triển kỹ năng giao tiếp và học cách đưa ra ý kiến một cách rõ ràng. Tôi cũng sẽ luyện tập nêu quan điểm với nhóm nhỏ để làm quen với việc bày tỏ ý kiến."
    },
    "2024-10-13": {
        "event": "Tôi đã thức khuya để xem phim, khiến sáng hôm sau khó dậy sớm và làm ảnh hưởng đến công việc.",
        "emotion": "Tôi cảm thấy mệt mỏi và tiếc nuối vì đã không biết giữ gìn sức khỏe, ảnh hưởng đến chất lượng làm việc.",
        "flaw": "Thiếu sự kiên định và kỷ luật trong việc duy trì thói quen sinh hoạt lành mạnh.",
        "lesson": "Việc giữ gìn sức khỏe quan trọng hơn rất nhiều so với các thú vui tạm thời. Cần biết ưu tiên cho giấc ngủ và năng lượng.",
        "improvement_plan": "Tôi sẽ lên lịch ngủ cố định, đặt báo thức nhắc nhở giờ đi ngủ và không để điện thoại hoặc thiết bị giải trí trong phòng ngủ."
    },
    "2024-10-14": {
        "event": "Tôi đã không thực hiện đúng kế hoạch học tập, thay vào đó dành thời gian xem video và chơi game.",
        "emotion": "Tôi cảm thấy áp lực khi nhận ra rằng mình đã lãng phí thời gian và không tiến bộ trong việc học.",
        "flaw": "Thiếu kỷ luật và dễ bị phân tâm bởi các hoạt động giải trí.",
        "lesson": "Việc trì hoãn sẽ khiến áp lực tăng cao và ảnh hưởng đến kết quả học tập. Cần đặt ra mục tiêu và kế hoạch cụ thể hơn.",
        "improvement_plan": "Tôi sẽ chia nhỏ các nhiệm vụ học tập để dễ dàng thực hiện, đồng thời đặt ra phần thưởng khi hoàn thành để tự khuyến khích bản thân."
    },
    "2024-10-15": {
        "event": "Hôm nay, tôi có một cuộc trò chuyện không tốt với một đồng nghiệp. Tôi đã vô tình dùng từ ngữ không phù hợp khiến họ cảm thấy bị xúc phạm.",
        "emotion": "Tôi cảm thấy rất hối hận vì đã không chú ý đến cách giao tiếp và khiến người khác cảm thấy không thoải mái.",
        "flaw": "Thiếu cẩn trọng trong cách dùng từ và giao tiếp, chưa đủ nhạy cảm với cảm xúc của người khác.",
        "lesson": "Cần lắng nghe kỹ trước khi đưa ra nhận xét và luôn lựa chọn từ ngữ phù hợp khi giao tiếp, đặc biệt trong môi trường công việc.",
        "improvement_plan": "Tôi sẽ xin lỗi đồng nghiệp và nhờ họ chia sẻ cảm nhận. Đồng thời, tôi sẽ tìm hiểu thêm về kỹ năng giao tiếp chuyên nghiệp và học cách đồng cảm hơn với người khác."
    }
}


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
                             "🎬 Tài nguyên", 
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
        <div style='background-color: #FFFACD; padding: 10px; border-radius: 10px; color: black; font-size: 20px; line-height: 1.5' >
            • <b>Cải thiện kết quả học tập:</b> Khi học sinh biết nhìn nhận và sửa chữa lỗi lầm, họ sẽ cải thiện hiệu quả học tập và đạt được thành tích cao hơn.<br>
            • <b>Tăng cường sự tự tin:</b> Khi có khả năng tự phê bình và điều chỉnh, học sinh sẽ tự tin hơn trong việc đối mặt với các thử thách mới.<br>
            • <b>Xây dựng kỹ năng xã hội:</b> Khả năng tự phê bình giúp học sinh hòa đồng hơn, dễ dàng lắng nghe và tiếp thu ý kiến từ người khác.
        </div>
        """, unsafe_allow_html=True)

def tai_nguyen():
    st.markdown("<h2 style='color: #FFFFF0;'>Tài Nguyên</h2>", unsafe_allow_html=True)

    # Submenu selection
    resource = st.selectbox("Chọn tài nguyên bạn muốn xem:", 
                             ["TÀI LIỆU KHOA HỌC", 
                              "PODCAST “LÀM THẾ NÀO ĐỂ TỰ PHÊ BÌNH KHI LÀM VIỆC NHÓM?”", 
                              "BỘ CÔNG CỤ TỰ KIỂM", 
                              "VIDEO BÁO CÁO TỰ PHÊ BÌNH"])

    # TÀI LIỆU KHOA HỌC
    if resource == "TÀI LIỆU KHOA HỌC":
        st.markdown("<h3 style='color: #FFFFE0; margin: 30px 0px'>📚 TÀI LIỆU KHOA HỌC</h3>", unsafe_allow_html=True)
        links = [
            ("Text Anxiety in Adolescents: The Role of Self-Criticism and Acceptance and Mindfulness Skills", "https://www.cambridge.org/core/journals/spanish-journal-of-psychology/article/abs/text-anxiety-in-adolescents-the-role-of-selfcriticism-and-acceptance-and-mindfulness-skills/F0B720E018D0A891050899676ADC6430"),
            ("Self-Criticism Scale", "https://www.researchgate.net/publication/377149610_Self-Criticism_Scale"),
            ("Self-criticizing and self-criticism: How do I stop the cycle?", "https://thriveworks.com/help-with/self-improvement/self-criticism/"),
            ("Self-Criticism", "https://www.sciencedirect.com/topics/psychology/self-criticism")
        ]

        for text, url in links:
            st.markdown(f'<a href="{url}" style="text-decoration: none; color: #FFFFF0; font-weight: bold; font-size:20px; line-height: 1"><u>{text}</u></a>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)  # Adding space between links

    # PODCAST
    elif resource == "PODCAST “LÀM THẾ NÀO ĐỂ TỰ PHÊ BÌNH KHI LÀM VIỆC NHÓM?”":
        st.markdown("<h3 style='color: #FFFFE0;'>🎙️ PODCAST “LÀM THẾ NÀO ĐỂ TỰ PHÊ BÌNH KHI LÀM VIỆC NHÓM?”</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=XTjwW8npbm8")  

    # BỘ CÔNG CỤ TỰ KIỂM
    elif resource == "BỘ CÔNG CỤ TỰ KIỂM":
        st.markdown("<h3 style='color: #FFFFE0;'>🛠️ BỘ CÔNG CỤ TỰ KIỂM RÈN LUYỆN KỸ NĂNG TỰ PHÊ BÌNH TRONG LÀM VIỆC NHÓM</h3>", unsafe_allow_html=True)
    
        cols1 = st.columns(2)  
        
        with cols1[0]:
            st.image("resources/tools/work1.png", use_column_width=True)  
            
        with cols1[1]:
            st.image("resources/tools/work2.png", use_column_width=True)  
        
        cols2 = st.columns(2)
        with cols2[0]:
            st.image("resources/tools/work3.png", use_column_width=True)  
            
        with cols2[1]:
            st.image("resources/tools/work4.png", use_column_width=True)  

    # VIDEO BÁO CÁO TỰ PHÊ BÌNH
    elif resource == "VIDEO BÁO CÁO TỰ PHÊ BÌNH":
        st.markdown("<h3 style='color: #FFFFE0;'>📹 VIDEO BÁO CÁO TỰ PHÊ BÌNH</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=xSEyk3rFp3g") 
        

def dien_dan():
    st.markdown("<h2 style='color: #FFFFF0;'>Diễn Đàn Thảo Luận</h2>", unsafe_allow_html=True)

    # Danh sách để lưu trữ các tin nhắn
    chat_history = [
        ("Nam Đẹp Trai", "Chào bạn, mình thấy bạn mới tham gia diễn đàn. Bạn đã bao giờ thực hành tự phê bình chưa?"),
        ("My Mít Ướt", "Chào bạn! Mình mới bắt đầu tìm hiểu. Mình từng nghe về khái niệm này trong một buổi hướng nghiệp ở trường, nhưng vẫn chưa thực sự biết cách thực hiện. Bạn có thể chia sẻ quá trình tự phê bình của bạn được không?"),
        ("Nam Đẹp Trai", "Tất nhiên rồi! Tự phê bình không chỉ là nhận ra lỗi sai mà còn là cơ hội để mình tự phản ánh, học hỏi và phát triển. Quá trình này bắt đầu với việc mình nhận ra rằng không phải lúc nào mình cũng hoàn hảo. Hồi mình học cấp 2, mình thường hay bỏ qua những khuyết điểm nhỏ vì nghĩ rằng không quan trọng. Nhưng dần dần, khi những lỗi nhỏ tích tụ lại, mình nhận ra chúng có thể cản trở sự phát triển của mình."),
        ("My Mít Ướt", "Nghe có vẻ thách thức thật. Khi bạn nhận ra những lỗi đó, bạn có cảm thấy mất tự tin không?"),
        ("Nam Đẹp Trai", "Đúng, ban đầu mình cảm thấy như vậy. Lúc nhận ra mình đã không làm tốt trong một số việc, mình khá tự ti và có phần trách móc bản thân. Nhưng rồi mình học cách thay đổi góc nhìn. Mình không coi những lỗi lầm là điều gì đó khiến mình yếu kém, mà là cơ hội để mình học hỏi và cải thiện. Ví dụ, khi nhận ra mình chưa giao tiếp tốt trong nhóm, mình bắt đầu tìm cách lắng nghe nhiều hơn và trình bày ý kiến một cách rõ ràng."),
        ("My Mít Ướt", "Vậy là bạn sử dụng những điểm yếu để thay đổi và phát triển bản thân?"),
        ("Nam Đẹp Trai", "Đúng vậy. Mình thấy quan trọng nhất trong tự phê bình là không để nó kéo bạn xuống mà phải biết cách sử dụng nó để nâng bạn lên. Hãy tự hỏi, \"Mình đã làm sai gì?\", nhưng sau đó phải tiếp tục với câu hỏi, \"Mình có thể làm gì để cải thiện điều này?\" Quá trình đó không dễ dàng, nhưng nó thực sự giúp mình trưởng thành."),
        ("My Mít Ướt", "Nghe thật thú vị! Bạn có lời khuyên nào cho người mới như mình không?"),
        ("Nam Đẹp Trai", "Nếu bạn mới bắt đầu, hãy bắt đầu từ những điều nhỏ. Bạn có thể viết nhật ký, mỗi ngày dành vài phút tự hỏi bản thân về những điều bạn có thể cải thiện, nhưng đừng chỉ tập trung vào sai lầm. Hãy tự hỏi cả về những gì bạn đã làm tốt. Điều này giúp bạn không chỉ nhận ra khuyết điểm mà còn trân trọng những nỗ lực của mình. Và quan trọng là, hãy kiên nhẫn với bản thân!"),
        ("My Mít Ướt", "Cảm ơn bạn nhiều! Mình sẽ thử cách đó. Mình đã có chút lo lắng khi nghĩ đến việc phê bình bản thân, nhưng giờ mình cảm thấy lạc quan hơn."),
        ("Nam Đẹp Trai", "Đừng lo lắng quá! Ai cũng có lúc mắc sai lầm. Quan trọng là bạn biết nhìn nhận và cố gắng cải thiện. Chúc bạn thành công trong hành trình này!"),
        ("My Mít Ướt", "Cảm ơn bạn! Mình sẽ cố gắng.")]

    # Hiển thị các tin nhắn với hiệu ứng bong bóng
    for sender, message in chat_history:
        if sender == "Nam Đẹp Trai":
            st.markdown(f"""
                <div style='text-align: left; margin: 10px;'>
                    <div style='background-color: #1E90FF; font-size: 20px; color: white; padding: 10px; border-radius: 15px; max-width: 70%; display: inline-block;'>
                        <b>{sender}:</b> {message}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style='text-align: right; margin: 10px;'>
                    <div style='background-color: #32CD32; font-size: 20px; color: white; padding: 10px; border-radius: 15px; max-width: 70%; display: inline-block;'>
                        <b>{sender}:</b> {message}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Khung nhập tin nhắn
    user_message = st.text_area("Nhập ý kiến của bạn tại đây...", height=100, placeholder="Viết tin nhắn của bạn ở đây...", key="user_input")

    # Nút gửi tin nhắn
    if st.button("Gửi"):
        if user_message:
            # Thêm tin nhắn mới vào danh sách
            chat_history.append(("Nam Đẹp Trai", user_message))
            st.success("Tin nhắn của bạn đã được gửi!")
            #st.experimental_rerun()  # Tải lại trang để cập nhật tin nhắn mới
        else:
            st.warning("Vui lòng nhập tin nhắn trước khi gửi.")

    # CSS cho nút
    st.markdown("""
    <style>
    .stButton > button {
        background-color: #1E90FF;  /* Màu nền nút */
        color: white;  /* Màu chữ */
        border: none;  /* Không có viền */
        border-radius: 5px;  /* Bo tròn góc */
        padding: 10px 20px;  /* Khoảng cách trong nút */
        font-size: 16px;  /* Kích thước chữ */
        cursor: pointer;  /* Con trỏ khi di chuột qua */
    }
    </style>
    """, unsafe_allow_html=True)



import datetime


def nhat_ky():
    st.markdown("<h2 style='color: #FFFFF0;'>Nhật Ký Tự Phê Bình Cá Nhân</h2>", unsafe_allow_html=True)

    # Hiển thị lịch chọn ngày
    selected_date = st.date_input("Chọn ngày để xem nhật ký:", datetime.datetime.now(), key='date_picker')

    # Kiểm tra nếu có dữ liệu cho ngày đã chọn
    date_key = selected_date.strftime("%Y-%m-%d")
    print(diary_data.keys())
    
    if date_key in diary_data.keys():
        # Hiển thị thông tin nhật ký cho ngày đã chọn
        st.subheader(f"Nhật Ký cho ngày {date_key}:")
        st.markdown(f"""
            <div style="background-color: #E0FFFF; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size:21px; line-height:1.75">
                <strong>Sự việc:</strong> {diary_data[date_key]['event']}
            </div>
            <div style="background-color: #E0FFFF; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size:21px; line-height:1.75">
                <strong>Cảm xúc:</strong> {diary_data[date_key]['emotion']}
            </div>
            <div style="background-color: #E0FFFF; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size:21px; line-height:1.75">
                <strong>Khuyết điểm:</strong> {diary_data[date_key]['flaw']}
            </div>
            <div style="background-color: #E0FFFF; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size:21px; line-height:1.75">
                <strong>Bài học rút ra:</strong> {diary_data[date_key]['lesson']}
            </div>
            <div style="background-color: #E0FFFF; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-size:21px; line-height:1.75">
                <strong>Kế hoạch cải thiện:</strong> {diary_data[date_key]['improvement_plan']}
            </div>

        """, unsafe_allow_html=True)
    else:
        st.warning("Không có dữ liệu cho ngày này.")

        # Phần nhập nhật ký mới
        st.markdown("### Nhập nhật ký cho ngày này:")
        
        # Tạo các input cho nhật ký
        
        st.markdown("""
            <style>
                .stTextInput {
                    color: white;  /* Màu chữ */
                    border: none;  /* Không có viền */
                    border-radius: 5px;  /* Bo tròn góc */
                    padding: 10px 20px;  /* Khoảng cách trong nút */
                    font-size: 25px;  /* Kích thước chữ */
                    cursor: pointer;  /* Con trỏ khi di chuột qua */
                }
            </style>
            """, unsafe_allow_html=True)
        new_event = st.text_input("Sự việc:", placeholder="Nhập sự việc xảy ra")
        new_emotion = st.text_input("Cảm xúc:", placeholder="Nhập cảm xúc của bạn")
        new_flaw = st.text_input("Khuyết điểm:", placeholder="Nhập khuyết điểm của bạn")
        new_lesson = st.text_input("Bài học rút ra:", placeholder="Nhập bài học của bạn")
        new_improvement_plan = st.text_input("Kế hoạch cải thiện:", placeholder="Nhập kế hoạch của bạn")

        # Nút lưu nhật ký với kiểu dáng
        st.markdown(
        """
        <style>
        .stButton > button {
            color: white;
            background-color: #1E90FF; /* Màu nền của nút */
            border: none; 
            border-radius: 5px;  
            padding: 10px 20px;  
            font-size: 16px; 
            cursor: pointer;
            transition: background-color 0.3s; /* Hiệu ứng khi di chuột */
        }
        .stButton > button:hover {
            background-color: #00BFFF; /* Màu nền khi di chuột */
        }
        </style>
        """,
        unsafe_allow_html=True
        )

        if st.button("💾 Lưu Nhật Ký"):
            # Lưu thông tin vào từ điển
            diary_data[date_key] = {
                "event": new_event or "Không có thông tin",
                "emotion": new_emotion or "Không có thông tin",
                "flaw": new_flaw or "Không có thông tin",
                "lesson": new_lesson or "Không có thông tin",
                "improvement_plan": new_improvement_plan or "Không có thông tin"
            }
            st.success("Nhật ký của bạn đã được lưu thành công!")


if menu == "🏠 Trang chủ":
    trang_chu()
elif menu == "📚 Tri thức về tự phê bình":
    tri_thuc()
elif menu == "🎬 Tài nguyên":
    tai_nguyen()
elif menu == "💬 Diễn đàn":
    dien_dan()
elif menu == "📝 Nhật ký cá nhân":
    nhat_ky()
