import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():
    
    tabs = ["Candlestick", "Marubozu_Spinning", "Hammer"]
    active_tab = st.selectbox("Select a topic", tabs)
    
    if active_tab == "Candlestick":
        text = "<div class='row'><h3>Giới thiệu về nến Nhật</h3>\
            <p>Mô hình nến Nhật candlesticks là một phương pháp phân tích kỹ thuật được người Nhật phát minh vào những năm 1600. Sau này được Steven Nison phát triển và phổ biến phương pháp phân tích này trên toàn thế giới, được ứng dụng rộng rãi trong phân tích kỹ thuật ngày nay.</p> \
            <p>Để hiểu về đồ thị nến Nhật, trước tiên ta bắt đầu từ các mức giá giao dịch. Mức giá là sự thể hiện mối liên hệ giữa người mua và người bán. Đó là giá trị mà tại đó một người muốn mua và một người muốn bán. Việc mua bán dựa trên sự mong đợi của họ vào biến động giá cả trong tương lai. \
            Nếu họ mong đợi trong tương lai giá sẽ tăng thì họ sẽ sẵn sàng mua vào và ngược lại họ sẽ bán ra.</p>\
            <p>Trong thực tế trong giao dịch chứng khoán thì thời gian có thể là 1 phút, 1 giờ, 1 ngày, 1 tuần hay 1 tháng,... tùy theo người sử dụng đồ thị chọn thời gian phân tích là phút, giờ, ngày, tuần hay tháng. Ví dụ, nếu người sử dụng chọn <strong>đồ thị ngày</strong> thì các mức giá được giao dịch trong 1 ngày sẽ tạo thành một cây nến Nhật. \
            Người ta thường gọi chúng với cái tên là <strong>nến giờ, nến ngày, nến tuần, nến tháng</strong>.</p>\
            <h3>Cấu tạo của một cây nến Nhật</h3>\
            <p>Trong mô hình nến Nhật các mức giá trong phiên giao dịch có ý nghĩa quan trọng tạo thành một cây nến Nhật.\
            Có 4 mức giá &nbsp;mà chúng ta cần quan tâm đó là:</p>"
        text1 = "<ul>\
            <li><strong>Giá mở cửa (open)</strong>: là mức giá khớp lệnh đầu tiên trong phiên giao dịch. Trên sàn HOSE, giá mở cửa là mức giá khớp lệnh trong phiên khớp lệnh định kỳ ATO xác định giá mở cửa. Trên sàn HNX, UPCOM là mức giá khớp lệnh đầu tiên trong ngày.</li>\
            <li><strong>Giá đóng cửa (close)</strong>: là mức giá giao dịch mua, bán cuối cùng trong phiên giao dịch (ATC) đó là phiên khớp lệnh định kỳ xác định giá đóng cửa. Đây là mức giá có ý nghĩa quan trọng nhất và được sử dụng nhiều nhất trong phân tích kỹ thuật.</li>\
            <li><strong>Giá cao nhất</strong>: là mức giá khớp lệnh cao nhất trong phiên giao dịch</li>\
            <li><strong>Giá thấp nhất</strong>: là mức giá khớp lệnh thấp nhất trong phiên giao dịch</li>\
            </ul>"
        st.markdown(text, unsafe_allow_html=True)
        col0, col1= st.columns([1, 1])
        with col0:
            st.markdown(text1, unsafe_allow_html=True)
        with col1:
            image = Image.open('images/nenNhat.jpg')
            st.image(image, use_column_width='always')
        text2 = "<p>Hình vẽ bên thể hiện một mô hình nến Nhật tiêu chuẩn, mỗi một cây nến biểu thị cho mức độ dao động giá trong một phiên giao dịch. Một cây <strong>nến xanh</strong> được hình thành khi mức <em>giá đóng cửa</em> <strong>cao hơn</strong> mức <em>giá mở cửa</em> của phiên giao dịch đó. \
            Ngược lại, một cây <strong>nến đỏ</strong> được hình thành khi có <em>giá đóng cửa</em> <strong>thấp hơn</strong> <em> giá mở cửa</em>.</p>\
            <p>Một cây nến tiêu chuẩn bao gồm 3 thành phần:</p><ul>\
            <li>Bóng trên (hay còn gọi là râu trên)</li>\
            <li>Thân nến (chỗ phình to)</li>\
            <li>Bóng dưới (hay còn gọi là râu dưới)</li></ul>\
            <p>Trong một cây <strong>nến xanh</strong> khoảng cách giữa giá đóng cửa và mức giá cao nhất trong phiên sẽ tạo thành bóng trên và khoảng cách giữa giá mở cửa và mức giá thấp nhất trong phiên giao dịch sẽ tạo thành bóng dưới.<br>\
            Trong một cây <strong>nến đỏ</strong>, khoảng cách giữa giá mở cửa và mức giá cao nhất sẽ tạo thành bóng trên và khoảng cách giữa giá đóng cửa mức giá thấp nhất sẽ tạo thành bóng dưới.<br>\
            Thân nến được hình thành trong phạm vi mức giá mở cửa và mức giá đóng cửa của phiên giao dịch. Nếu giá đóng cửa và giá mở cửa cách xa nhau sẽ tạo thành một thân nến lớn và ngược lại sẽ tạo thành một thân nến nhỏ.</p>\
            <h3>Ý nghĩa của mô hình nến Nhật</h3>\
            <p>Nhìn vào đồ thị hình nến Nhật Bản ta có thể biết được giá cổ phiếu ngày hôm đó có giá mở cửa, đóng cửa, cao nhất, thấp nhất là bao nhiêu. \
            Đối với cổ phiếu chỉ có giá đóng cửa như các cổ phiếu nằm trên sàn chứng khoán Hà nội (HNX) không có phiên khớp lệnh định kỳ xác định giá mở cửa thì ta lấy mức giá khớp lệnh đầu tiên làm giá mở cửa, \
            hoặc sàn UPCOM không có phiên giao dịch khớp lệnh định kỳ nào thì giá mở cửa là mức giá khớp lệnh đầu tiên và giá đóng cửa là mức giá bình quân của tất cả các mức giá trong phiên giao dịch làm giá đóng cửa. \
            Đây là những đặc điểm hết sức quan trọng mà chúng ta phải biết để vận dụng vào việc phân tích các mẫu hình nến đảo chiều sau này.</p>\
            Nguồn: tham khảo từ website <a href='https://chungkhoanviet.net'>Chứng khoán Việt</div>"
        st.markdown(text2, unsafe_allow_html=True)
        st.write("")
        st.video("https://www.youtube.com/watch?v=C9p19zOgrlo&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=2")
        #components.iframe("""https://www.youtube.com/embed/C9p19zOgrlo?list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ""" , scrolling = True , height = 500) 
    
    elif active_tab == "Marubozu_Spinning":
        text = "<div class='row'><h3>Nến cường lực Marubozu</h3>\
            <p><strong>Nến Marubozu</strong> có tên gọi khác là nến cường lực. Đặc điểm của nó là thân nến rất dài giá mở cửa và giá đóng cửa cách xa nhau và không có bóng nến trên hoặc dưới, hoặc nếu có bóng nến trên hoặc dưới thì cũng không đáng kể. \
            Điều đó đồng nghĩa với việc giá cao nhất và giá thấp nhất trùng với giá mở cửa và giá đóng cửa của cây nến.</p>\
            <p><strong>Nến Marubozu</strong> thể hiện lực mua và bán rất mạnh, thường xuất hiện khi giá tăng hoặc giảm giá mạnh hoặc khi lực mua hoặc bán tăng đột biến. Điều này cho thấy trong quá trình mua bán không có sự do dự của nhà đầu tư khi mua hoặc bán. \
            Khi 3 cây nến Marubozu cùng màu xuất hiện liên tiếp chúng báo hiệu thị trường trong xu hướng tăng (nến xanh) hoặc giảm giá rất mạnh (nến đỏ). Khi ba cây nến Marubozu xanh hoặc đỏ xuất hiện liên tiếp nhau chúng tạo thành một hình mẫu người ta gọi là ba người lính trắng (nến xanh) hoặc 3 con quạ đen (nến đỏ) \
            <p><strong>Nến Marubozu</strong> thường hay xuất hiện trên đồ thị giá khi có thông tin bất ngờ xuất hiện làm xuất hiện một lực cầu (tin cực tốt) hoặc lực cung (tin cực xấu) xuất hiện trên thị trường sẽ làm cho giá đóng cửa ở mức giá cao nhất hoặc thấp nhất trong ngày.</p>"
        col0, col1= st.columns([1, 1])
        with col0:
            st.markdown(text, unsafe_allow_html=True)
        with col1:
            st.header("")
            st.header("")
            image = Image.open('images/marubozu.jpg')
            st.image(image, caption="Nến cường lực Marubozu", use_column_width='always')
        text1 = "<div class='row'><h3>Nến con quay Spinning top</h3>\
            <p><strong>Nến spinning top</strong> hay còn gọi là <strong>nến con quay</strong> vì hình dáng của nó. Đặc điểm dễ nhận biết của nến spinning top là bóng trên và dưới rất dài, thân nến ngắn do chênh lệch giữa giá mở cửa và giá đóng cửa không cao.\
            Trong phiên giao dịch có lúc lực cầu và cung mạnh đẩy giá nên mức cao (bóng trên) và ép giá xuống thấp (bóng dưới).\
            Điều này chứng tỏ rằng cả người mua và bán đều không thể chiếm thế thượng phong và kết quả là một sự bế tắc thể hiện ở việc giá mở cửa và giá đóng cửa chênh lệch nhau rất thấp.</p>\
            <p>Nến spinning top là một mẫu nến trung lập thể hiện sự lưỡng lự của người bán và người mua và xu hướng giá của nó <strong>không cho dấu hiệu đảo chiều</strong>.\
            Tuy nhiên, nếu cây nến spinning top xuất hiện ở <strong>cuối chu kỳ tăng hoặc giảm</strong> có thể báo hiệu xu hướng <strong>sắp đảo chiều nhưng nó không rõ ràng</strong>.\
            Do đó, cần phải xem xét các cây nến xung quanh nó xem nó có tạo thành một tổ hợp nến đảo chiều hay không \
            hoặc kết hợp với các chỉ báo khác để phán đoán một cách chính xác đường đi sắp tới của giá.</p>" 
            
        col0, col1= st.columns([1, 1])
        with col0:
            st.markdown(text1, unsafe_allow_html=True)
        with col1:
            st.header("")
            st.header("")
            image = Image.open('images/spinning.jpg')
            st.image(image, caption="Nến con quay Spinning top", use_column_width='always') 
        st.video("https://www.youtube.com/watch?v=RVunoQBwHng&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=2")
        #components.iframe("""https://www.youtube.com/embed/RVunoQBwHng?list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ""" , scrolling = True , height = 500) 
    elif active_tab == "Hammer":
        text1 = "<div class='row'><h3>Nến búa Hammer</h3>\
        <p>Nến hammer là một trong những mẫu nến đảo chiều quan trọng, thường xuất hiện ở đáy của <strong>một xu hướng giảm giá</strong>. \
        Nó có thể là nến xanh hay đỏ nhưng nó đều có đặc điểm chung là thân nến nhỏ và bóng dưới rất dài thường gấp hơn 2 lần độ dài thân nến.</p>\
        <p>Trong mẫu nến hammer bóng dưới càng dài, bóng trên càng ngắn, thân của nến càng nhỏ càng có ý nghĩa <strong>tăng giá</strong>. Mặc dù thân của nến hammer có thể màu xanh hay đỏ, mức độ tăng giá sẽ đáng kể hơn nếu thân của hammer màu xanh. \
        <ul><li>Nếu thân của nến búa hammer màu xanh nó mang ý nghĩa rõ ràng rằng thị trường bị bán tháo gần như suốt phiên và sau đó bật tăng trở lại và lúc đóng cửa với giá cao nhất trong phiên. \
        Đó gần như là dấu hiệu của sự tăng giá. </li><li>Nếu thân của hammer màu đỏ, nó thể hiện rằng giá đóng cửa thấp hơn mức giá mở cửa hàm ý rằng <strong>mức độ tăng giá yếu hơn</strong>.</li></p>"
            
        col0, col1= st.columns([1, 1])
        with col0:
            st.markdown(text1, unsafe_allow_html=True)
        with col1:
            st.header("")
            st.header("")
            image = Image.open('images/hammer.jpg')
            st.image(image, caption="Nến búa Hammer", use_column_width='always')  

        text2 = "<div class='row'><h3>Nến búa ngược Inverted Hammer</h3>\
            <p>Nến Inverted hammer hay còn gọi là <strong>Nến búa ngược</strong>, là một mẫu hình nến đảo chiều xuất hiện ở đáy của <strong>một xu hướng giảm</strong>. Về hình dạng nó ngược lại với nến Hammer với đầu búa nằm ở dưới và bóng trên rất dài.</p> \
            <p>Đặc điểm của nến búa ngược là <strong>thân nến nhỏ</strong>, bóng dưới không có hoặc nhỏ, bóng trên rất dài thường gấp 2 lần chiều dài thân nến. \
            Mẫu hình này thường xuất hiện ở <strong>đáy của một xu hướng giảm giá</strong> và là cảnh báo về khả năng <strong>giá có khả năng đảo chiều tăng trở lại</strong>.</p> \
            <p>Mẫu hình này không phải là dấu hiệu chắc chắn của một sự đảo chiều mà ta cần phải kết hợp thêm với các cây nến tạo thành một tổ hợp nến đảo chiều \
            hoặc kết hợp với một số chỉ báo kỹ thuật khác như các đường xu hướng, MA, MACD, Bollinger band…, để xác nhận về khả năng đảo chiều của giá.</p> \
        "
            
        col0, col1= st.columns([1, 1])
        with col0:
            st.markdown(text2, unsafe_allow_html=True)
        with col1:
            st.header("")
            st.header("")
            image = Image.open('images/inverted-hammer.jpg')
            st.image(image, caption="Nến búa ngược Inverted Hammer", use_column_width='always')    
        st.video("https://www.youtube.com/watch?v=5eFblK8iTJ8&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=3")
        
    elif active_tab == "Contact":
        st.write("If you'd like to contact me, then please don't.")
    else:
        st.error("Something has gone terribly wrong.")