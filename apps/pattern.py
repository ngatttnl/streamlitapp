import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():
    
    tabs = ["Double Top & Double Bottom", "Others"]
    active_tab = st.selectbox("Select a topic", tabs)
    #active_tab = "Doji"
    if active_tab == "Double Top & Double Bottom":
        text = """<h3>1. Mô hình hai đỉnh và hai đáy Double Top & Double Bottom</h3>
            <p>Mẫu 2 đỉnh hoặc 2 đáy dễ nhận ra và một trong những mẫu hình biểu đồ phân tích kỹ thuật đáng tin cậy nhất, là 1 trong những công cụ yêu thích của nhiều trader kỹ thuật.
            Mô hình được hình thành sau một xu hướng bền vững khi giá kiểm định ở ngưỡng hỗ trợ hoặc kháng cự tương tự hai lần mà không có đột phá. Mô hình này báo hiệu sự bắt đầu của sự đảo chiều xu hướng trong trung và dài hạn.</p>
            <p>Mô hình hai đỉnh Double Top thường xuất hiện trong một xu hướng tăng mạnh:
            Khi đạt đỉnh thứ 1, giá có xu hướng đảo chiều, tại vùng đảo chiều này sẽ hình thành đáy trung tâm.
            Nhưng giá không tiếp tục lao xuống mà quay trở về xu hướng tăng trước đó và tạo thành đỉnh thứ hai.
            Mô hình giá 2 đỉnh thể hiện sự từ chối tăng giá không phải 1 lần mà là 2 lần để tạo ra một đỉnh mới cao hơn so với đỉnh cũ. Đây chính là dấu hiệu cho thấy sự đảo chiều và dự báo một xu hướng giảm giá mạnh sắp diễn ra.</p>
            """
        st.markdown(text, unsafe_allow_html=True)
         
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")
        with col2:
            image = Image.open('images/doubletop.jpeg')
            st.image(image, use_column_width='always')
        with col3:
            st.write("")

        text2 = """<h3>2. Mô hình đầu và vai Head and Shoulder và mô hình đầu và vai ngược Inverse Head and Shoulder</h3>
            <p>Đầu và Vai là một mẫu biểu đồ đảo chiều cho thấy xu hướng có khả năng đảo chiều khi nó đã hoàn thành, từ xu hướng tăng sang xu hướng giảm. Đầu và vai được đặc trưng bởi ba đỉnh:</p>
            - Đỉnh giữa là đỉnh cao nhất (đầu)
            <br>- 2 đỉnh 2 bên thấp hơn hoặc gần bằng (vai). Mức thấp giữa các đỉnh này được kết nối với một đường xu hướng (đường viền cổ) thể hiện mức hỗ trợ chính để xem mức phá vỡ và sự đảo chiều xu hướng.
            <br>Mô hình đầu vai được hình thành và xác nhận khi mức hỗ trợ chính tại đường viền cổ bị phá vỡ.
            <p>Tương tự nhưng theo hướng ngược lại cho mẫu hình giá <strong> đầu và vai ngược Inverse Head and Shoulder</strong>! Đường viền cổ trong mẫu hình đầu vai ngược là một mức kháng cự để theo dõi cho một breakout cao hơn.</p>
        """
        st.markdown(text2, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            image = Image.open('images/headshoulder.jpg')
            st.image(image, use_column_width='always')
        with col3:
            st.write("")
        
        text3 = """<h3>3. Mô hình 3 đỉnh (Triple Top) và 3 đáy (Triple Bottom)</h3>
            <p>Ba đỉnh và ba đáy là các mẫu đảo chiều mà không phổ biến như đầu và vai hoặc hai đỉnh hoặc hai đáy. Nhưng, chúng hoạt động theo một cách tương tự và có thể là một tín hiệu giao dịch mạnh mẽ cho một sự đảo chiều xu hướng.
            </p><p>Các mẫu hình được hình thành khi giá kiểm định ở khoảng ngưỡng hỗ trợ hoặc kháng cự ba lần và không thể vượt qua được.
            <br>Mô hình 3 đỉnh có nhìn giống như 3 ngọn núi có đỉnh ngang nhau, với 2 đáy tạm thời. Đường thẳng qua 3 đỉnh gọi là đường kháng cự và đường nối 2 đáy được gọi là đường neckline (đường viền cổ) – đây cũng đóng vai trò là đường hỗ trợ.
            <br> Mô hình 3 đỉnh thường là dấu hiệu của sự đảo chiều xu hướng từ <strong>tăng sang giảm</strong>.
            </p>
        """
        st.markdown(text3, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            image = Image.open('images/triptop.jpg')
            st.image(image, use_column_width='always')
        with col2:
            image = Image.open('images/triptop2.jpg')
            st.image(image, use_column_width='always')
        text4 = """
            <p>Mô hình 3 đáy, ngược lại, thường là dấu hiệu của sự đảo chiều xu hướng từ <strong>giảm sang tăng</strong>.</p>
        """
        st.markdown(text4, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col2:
            image = Image.open('images/tripbottom.jpg')
            st.image(image, use_column_width='always')
        with col3:
            st.write("")
    
    else:
        st.error("Something has gone terribly wrong.")