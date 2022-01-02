import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():
    
    tabs = ["Candlestick", "Marubozu & Spinning", "Hammer & Inverted Hammer", "Hanging-man & Shooting star", "Doji & Long-Legged Doji", "Dragonfly & Gravestone Doji"]
    active_tab = st.selectbox("Select a topic", tabs)
    #active_tab = "Doji"
    if active_tab == "Candlestick":
        text = "<h3>Giới thiệu về nến Nhật</h3>\
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
        st.markdown(text1, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        with col2:
            image = Image.open('images/nenNhat.jpg')
            st.image(image, use_column_width='always')
        with col3:
            st.write("")

        text2 = "<p>Hình vẽ trên thể hiện một mô hình nến Nhật tiêu chuẩn, mỗi một cây nến biểu thị cho mức độ dao động giá trong một phiên giao dịch. Một cây <strong>nến xanh</strong> được hình thành khi mức <em>giá đóng cửa</em> <strong>cao hơn</strong> mức <em>giá mở cửa</em> của phiên giao dịch đó. \
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
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        with col2:
            image = Image.open('images/inverted-hammer.jpg')
            st.video("https://www.youtube.com/watch?v=C9p19zOgrlo&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=2")
        with col3:
            st.write("")
        
        #components.iframe("""https://www.youtube.com/embed/C9p19zOgrlo?list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ""" , scrolling = True , height = 500) 
    
    elif active_tab == "Marubozu & Spinning":
        text = "<h3>Nến cường lực Marubozu</h3>\
            <p><strong>Nến Marubozu</strong> có tên gọi khác là nến cường lực. Đặc điểm của nó là thân nến rất dài giá mở cửa và giá đóng cửa cách xa nhau và không có bóng nến trên hoặc dưới, hoặc nếu có bóng nến trên hoặc dưới thì cũng không đáng kể. \
            Điều đó đồng nghĩa với việc giá cao nhất và giá thấp nhất trùng với giá mở cửa và giá đóng cửa của cây nến.</p>\
            <p><strong>Nến Marubozu</strong> thể hiện lực mua và bán rất mạnh, thường xuất hiện khi giá tăng hoặc giảm giá mạnh hoặc khi lực mua hoặc bán tăng đột biến. Điều này cho thấy trong quá trình mua bán không có sự do dự của nhà đầu tư khi mua hoặc bán. \
            Khi 3 cây nến Marubozu cùng màu xuất hiện liên tiếp chúng báo hiệu thị trường trong xu hướng tăng (nến xanh) hoặc giảm giá rất mạnh (nến đỏ). Khi ba cây nến Marubozu xanh hoặc đỏ xuất hiện liên tiếp nhau chúng tạo thành một hình mẫu người ta gọi là ba người lính trắng (nến xanh) hoặc 3 con quạ đen (nến đỏ) \
            <p><strong>Nến Marubozu</strong> thường hay xuất hiện trên đồ thị giá khi có thông tin bất ngờ xuất hiện làm xuất hiện một lực cầu (tin cực tốt) hoặc lực cung (tin cực xấu) xuất hiện trên thị trường sẽ làm cho giá đóng cửa ở mức giá cao nhất hoặc thấp nhất trong ngày.</p>"
        st.markdown(text, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        with col2:
            image = Image.open('images/marubozu.jpg')
            st.image(image, use_column_width=True, caption="Nến cường lực Marubozu")
        with col3:
            st.write("")

        text1 = "<div class='row'><h3>Nến con quay Spinning top</h3>\
            <p><strong>Nến spinning top</strong> hay còn gọi là <strong>nến con quay</strong> vì hình dáng của nó. Đặc điểm dễ nhận biết của nến spinning top là bóng trên và dưới rất dài, thân nến ngắn do chênh lệch giữa giá mở cửa và giá đóng cửa không cao.\
            Trong phiên giao dịch có lúc lực cầu và cung mạnh đẩy giá nên mức cao (bóng trên) và ép giá xuống thấp (bóng dưới).\
            Điều này chứng tỏ rằng cả người mua và bán đều không thể chiếm thế thượng phong và kết quả là một sự bế tắc thể hiện ở việc giá mở cửa và giá đóng cửa chênh lệch nhau rất thấp.</p>\
            <p>Nến spinning top là một mẫu nến trung lập thể hiện sự lưỡng lự của người bán và người mua và xu hướng giá của nó <strong>không cho dấu hiệu đảo chiều</strong>.\
            Tuy nhiên, nếu cây nến spinning top xuất hiện ở <strong>cuối chu kỳ tăng hoặc giảm</strong> có thể báo hiệu xu hướng <strong>sắp đảo chiều nhưng nó không rõ ràng</strong>.\
            Do đó, cần phải xem xét các cây nến xung quanh nó xem nó có tạo thành một tổ hợp nến đảo chiều hay không \
            hoặc kết hợp với các chỉ báo khác để phán đoán một cách chính xác đường đi sắp tới của giá.</p>" 
            
        st.markdown(text1, unsafe_allow_html=True)
       
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        with col2:
            image = Image.open('images/spinning.jpg')
            st.image(image, use_column_width=True, caption="Nến con quay Spinning top") 
            st.video("https://www.youtube.com/watch?v=RVunoQBwHng&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=2")
        with col3:
            st.write("")
        
        #components.iframe("""https://www.youtube.com/embed/RVunoQBwHng?list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ""" , scrolling = True , height = 500) 
    elif active_tab == "Hammer & Inverted Hammer":
        text1 = "<h3>Nến búa Hammer</h3>\
        <p>Nến hammer là một trong những mẫu nến đảo chiều quan trọng, thường xuất hiện ở đáy của <strong>một xu hướng giảm giá</strong>. \
        Nó có thể là nến xanh hay đỏ nhưng nó đều có đặc điểm chung là thân nến nhỏ và bóng dưới rất dài thường gấp hơn 2 lần độ dài thân nến.</p>\
        <p>Trong mẫu nến hammer bóng dưới càng dài, bóng trên càng ngắn, thân của nến càng nhỏ càng có ý nghĩa <strong>tăng giá</strong>. Mặc dù thân của nến hammer có thể màu xanh hay đỏ, mức độ tăng giá sẽ đáng kể hơn nếu thân của hammer màu xanh. \
        <ul><li>Nếu thân của nến búa hammer màu xanh nó mang ý nghĩa rõ ràng rằng thị trường bị bán tháo gần như suốt phiên và sau đó bật tăng trở lại và lúc đóng cửa với giá cao nhất trong phiên. \
        Đó gần như là dấu hiệu của sự tăng giá. </li><li>Nếu thân của hammer màu đỏ, nó thể hiện rằng giá đóng cửa thấp hơn mức giá mở cửa hàm ý rằng <strong>mức độ tăng giá yếu hơn</strong>.</li></p>"
            
        st.markdown(text1, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")

        with col2:
            image = Image.open('images/hammer.jpg')
            st.image(image, caption="Nến búa Hammer", use_column_width='always') 
        with col3:
            st.write("")

        text2 = "<div class='row'><h3>Nến búa ngược Inverted Hammer</h3>\
            <p>Nến Inverted hammer hay còn gọi là <strong>Nến búa ngược</strong>, là một mẫu hình nến đảo chiều xuất hiện ở đáy của <strong>một xu hướng giảm</strong>. Về hình dạng nó ngược lại với nến Hammer với đầu búa nằm ở dưới và bóng trên rất dài.</p> \
            <p>Đặc điểm của nến búa ngược là <strong>thân nến nhỏ</strong>, bóng dưới không có hoặc nhỏ, bóng trên rất dài thường gấp 2 lần chiều dài thân nến. \
            Mẫu hình này thường xuất hiện ở <strong>đáy của một xu hướng giảm giá</strong> và là cảnh báo về khả năng <strong>giá có khả năng đảo chiều tăng trở lại</strong>.</p> \
            <p>Mẫu hình này không phải là dấu hiệu chắc chắn của một sự đảo chiều mà ta cần phải kết hợp thêm với các cây nến tạo thành một tổ hợp nến đảo chiều \
            hoặc kết hợp với một số chỉ báo kỹ thuật khác như các đường xu hướng, MA, MACD, Bollinger band…, để xác nhận về khả năng đảo chiều của giá.</p> \
        "
            
        st.markdown(text2, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,6,1])

        with col1:
            st.write("")

        with col2:
            image = Image.open('images/inverted-hammer.jpg')
            st.image(image, caption="Nến búa ngược Inverted Hammer", use_column_width='always')    
            st.video("https://www.youtube.com/watch?v=5eFblK8iTJ8&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=3")
        with col3:
            st.write("")
        
    elif active_tab == "Hanging-man & Shooting star":
        text1 = "<h3>Nến người treo cổ Hangingman</h3>\
            <p>Nến hanging man hay còn gọi là nến “người treo cổ” là một mẫu hình nến đảo chiều hữu ích trong đồ thị hình nến.\
            Nhìn về hình thức thì mẫu nến hanging man không khác gì với mẫu nến hammer nhưng điểm khác biệt duy nhất là vị trí xuất hiện của nó trên đồ thị giá. \
            Nến&nbsp;<strong>hanging man</strong>&nbsp;thường xuất hiện ở đỉnh của một xu hướng tăng giá. \
            Hay nói cách khác khi nến hammer xuất hiện ở đỉnh của một xu hướng tăng thì gọi là nến Hanging Man. Đây là mẫu hình nến báo hiệu giá sắp quay đầu giảm.</p> \
            <p>Nếu thân của Hanging man màu đỏ, nó thể hiện rằng giá đóng cửa không thể trở lại mức giá mở cửa. Điều đó hàm ý khả năng giá sắp quay đầu giảm. \
            Tuy nhiên điều quan trọng là bạn phải đợi sự xác nhận của Hanging man vì trong bối cảnh thị trường đã thể hiện hết khả năng tăng giá thì hanging man xuất hiện. \
            Vào phiên thị trường mở cửa ở gần giá cao rồi bị bán tháo, sau đó phục hồi đóng cửa ở gần mức giá cao hoặc ở mức giá cao nhất. \
            Sức mạnh này không phải là kiểu hành động giá để bạn nghĩ rằng Hanging man có thể là đỉnh đảo chiều. \
            Nhưng kiểu hành động này chỉ ra rằng thị trường đã bắt đầu hành động bán tháo, nó đã trở lên dễ bị tấn công tiếp khi chúng ta không kịp đề phòng. \
            Tín hiệu xác nhận có thể là một cây nến giảm tiếp theo có khoảng trống giảm giá (Giữa phần thân nến phiên xuất hiện hanging man với giá mở cửa kế tiếp) \
            hoặc có thể là phiên giảm giá với giá đóng cửa thấp hơn phiên đóng cửa của cây nến hanging man ngày hôm trước.</p>"
            
        st.markdown(text1, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            image = Image.open('images/hanging_man.jpg')
            st.image(image, caption="Nến người treo cổ Hanging-man", use_column_width='always')
        with col2:
            image = Image.open('images/hanging_man2.jpg')
            st.image(image, caption="Ví dụ minh họa cho nến người treo cổ Hanging-man", use_column_width='always') 
        
        text2 = """<div class='row'><h3>Nến sao băng Shooting star</h3>\
            <p>Nến Shooting star hay còn gọi là nến "sao băng" là một mẫu hình nến đảo chiều thường xuất hiện ở đỉnh của một xu hướng tăng. \
            Nến Shooting star về hình thức giống hệt mô hình nến búa ngược inverted hammer. Mẫu hình shooting star gửi một thông điệp cảnh báo <strong>một đỉnh sắp xảy ra</strong>, \
            như tên gọi của nó là <strong>một sao băng</strong>. Nó thường không phải là một tín hiệu đảo chiều chính như mẫu hình Evening star. Nến sao băng Shooting star có một thân nhỏ nằm ở đáy trong phạm vi của phiên với một bóng trên dài. \
            Giống như đối với tất cả các ngôi sao, màu của thân nến không phải là quan trọng có thể xanh hoặc đỏ.</p>\
            <p>Mẫu hình nến Shooting star là một cảnh báo đỉnh sắp xảy ra, tuy nhiên nó không phải là một chỉ báo chắc chắn về một sự đảo chiều của giá. Để có thêm thông tin về sự đảo chiều cần phải kết hợp với các mẫu hình nến hoặc các chỉ báo khác để ra quyết định chính xác.</p>
        """
            
        st.markdown(text2, unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            image = Image.open('images/shooting.jpg')
            st.image(image, caption="Nến sao băng Shooting star", use_column_width='always')
        with col2:
            image = Image.open('images/shooting2.jpg')
            st.image(image, caption="Minh họa Nến sao băng xuất hiện ở đỉnh của 1 xu hướng", use_column_width='always')    
          
        #st.video("https://www.youtube.com/watch?v=5eFblK8iTJ8&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=3")
    elif active_tab == "Doji & Long-Legged Doji":
        text1 = """<h3>Nến Doji</h3>
            <p>Nến Doji là một mẫu hình nến đặc biệt trong đồ thị hình nến candlesticks. Nó không có thân nến và chỉ có bóng nến trên dưới. 
            Nến Doji hình thành khi giá đóng cửa và giá mở cửa của chứng khoán bằng nhau hoặc xấp xỉ nhau. Độ dài của bóng trên và bóng dưới có thể khác nhau. 
            Trên biểu đồ hình nến Doji có hình dạng như một “dấu cộng” hoặc “chữ thập” rất dễ nhận ra.</p> 
            <p>Doji thể hiện sự lưỡng lự, thiếu quyết đoán hoặc giằng co giữa người mua và người bán.
            Giá di chuyển trên và dưới mức mở cửa trong phiên, nhưng đóng cửa ở hoặc gần mức mở. Kết quả là cung cầu cân bằng nhau không bên nào giành được ưu thế và một bước ngoặt mới có thể đang hình thành.</p>
            <p>Nến Doji thường xuất hiện trên đồ thị giá của chứng khoán và do đó được coi là một dấu hiệu nghỉ ngơi tạm thời hướng di chuyển của giá.</p>
            <p>Sự liên quan của một&nbsp; Doji phụ thuộc vào xu hướng trước hoặc nến trước. Sau một xu hướng tăng hoặc sau một cây nến xanh dài, một cây nến Doji xuất hiện báo hiệu rằng áp lực mua đang bắt đầu suy yếu.
            Sau một xu hướng giảm, hoặc sau một cây nến đỏ dài, nến Doji xuất hiện báo hiệu rằng áp lực bán đang bắt đầu giảm. Doji chỉ ra rằng các lực lượng cung và cầu đang trở nên cân bằng hơn và một sự thay đổi trong xu hướng có thể gần kề.\
            Doji một mình là không đủ để đánh dấu một sự đảo ngược, do đó ta cần phải dựa vào các cây nến xung quanh và xác nhận thêm từ các chỉ báo phân tích kỹ thuật khác để xác nhận.</p>
        """
        st.markdown(text1, unsafe_allow_html=True)  
        col1, col2, col3 = st.columns([1,3,1])
        with col1:
            st.write("")

        with col2:
            image = Image.open('images/doji.jpg')
            st.image(image, caption="Nến Doji", use_column_width='always') 
        with col3:
            st.write("")
        
        text2 = """<div class='row'><h3>Nến Doji chân dài Long-Legged Doji</h3>
            <p>Nến Doji chân dài được hình thành khi giá mở cửa và giá đóng cửa bằng nhau. Một Doji chân dài, thường được gọi là nến “Người kéo xe” giống như một Doji, 
            tuy nhiên bóng trên và dưới dài hơn nhiều so với hình dạng <strong>Doji thông thường</strong>.</p>
            <p>Nến Doji chân dài có đặc điểm của một Doji, thể hiện sự do dự thiếu quả quyết của nhà đầu tư trong phiên giao dịch. 
            Nhìn vào cây nến Doji chân dài ta có thể thấy sau khi mở cửa, có lúc người mua hay người bán đẩy giá lên cao hay đẩy giá xuống thấp tương ứng với điểm cao nhất và thấp nhất của bóng nến trên và dưới. 
            Tuy nhiên trong phiên khớp lệnh đóng cửa, lực cung và lực cầu cân bằng đã đẩy giá về mức tương đương giá mở cửa.</p>
            <p>Chú ý rằng Nến Doji chân dài không phải là dấu hiệu đảo chiều chắc chắn vì nó thể hiện sự lưỡng lự của nhà đầu tư. 
            Doji chân dài thường xuất hiện trong một đợt tăng giá hay giảm giá đáng kể của thị trường. 
            Doji xuất hiện là một dấu hiệu cảnh báo cho sự suy giảm về cường độ của một xu hướng giảm giá hoặc tăng giá. 
            Nhà đầu tư nên cân nhắc khi ra quyết định mua bán khi cây nến Doji xuất hiện.</p>
            <p>Sau một xu hướng giảm dài, cây nến Doji A xuất hiện đánh dấu sự do dự của cung và cầu. Việc giảm bớt tỷ trọng cổ phiếu GE hoặc thoát hoàn toàn khỏi thị trường có thể là một hành động thông minh. 
            Các bạn có thể thấy sau một 2 phiên nghỉ ngơi và hồi phục nhẹ thị trường lại tiếp tục xu hướng downtrend của nó.</p>
        """        
        st.markdown(text2, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            st.write("")
        with col2:
            image = Image.open('images/longlegdoji.jpg')
            st.image(image, caption="Minh họa Nến Doji chân dài xuất hiện cổ phiếu General Electric", use_column_width='always')    
        with col3:
            st.write("") 
        #st.video("https://www.youtube.com/watch?v=5eFblK8iTJ8&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=3")
    elif active_tab == "Dragonfly & Gravestone Doji":
        text1 = """<h3>Nến Doji chuồn (Dragonfly Doji)</h3>\
            <p>Nến Doji chuồn chuồn (Dragonfly Doji) là một biến thể của một nến Doji thông thường. Đặc điểm dễ nhận thấy trên đồ thị giá là nến Doji chuồn chuồn có bóng dưới rất dài. 
            Bóng trên không có hoặc rất ngắn. Khác với Doji thường và Doji chân dài biểu thị sự do dự, lưỡng lự, thiếu quả quyết của NĐT hay có thể nói là sự cân bằng của cung cầu trong phiên. 
            Nến <strong>Doji chuồn chuồn</strong> là một mẫu hình nến đảo chiều tăng giá rất quan trọng trong việc phân tích kỹ thuật hình nến. Nó thường xuất hiện ở đáy của một xu hướng giảm giá.</p> 
            <p>Doji chuồn chuồn được hình thành khi giá mở cửa và giá đóng cửa ở gần mức cao nhất trong ngày, nó có thể có một chút bóng trên nhỏ nhưng quan trọng là bóng dưới rất dài. 
            Bóng dưới dài hàm ý rằng thị trường đã thử thách để tìm được điểm cân bằng giữa người mua và người bán. Trong phiên cung xuất hiện ép giá giảm sâu nhưng tại đây lực cầu xuất hiện đã đẩy giá tăng trở lại và đóng cửa gần hoặc bằng với mức giá mở cửa. 
            Như vậy mục đích ép giá xuống của nhà đầu cơ đã bị triệt tiêu ngay trong phiên giao dịch. Biểu đồ dưới đây là ví dụ cho nến Doji chuồn chuồn trong một xu thế giảm.</p>
            <p>Nhìn trên đồ thị ta thấy thị trường thử thách để tìm kiếm sự cân bằng giữa cung và cầu . Và cuối cùng cũng tìm được ngưỡng hỗ trợ mạnh ngay tại mức giá thấp nhất trong ngày, 
            sau khi người mua đã đẩy giá lên cao và đẩy giá đóng cửa xấp xỉ với giá mở cửa trong ngày.</p>
            <p>Nến Doji chuồn chuồn là mẫu đồ thị nến cực kỳ hữu dụng, nó giúp cho nhà đầu tư xác định được ngưỡng hỗ trợ cung cầu ngay trong phiên giao dịch. Sau một xu hướng giảm, 
            nến Doji chuồn chuồn xuất hiện là dấu hiệu cho nhà đầu tư biết rằng sự giảm giá đã xảy ra quá mức và khả năng cao trong ngắn hạn nó sẽ kết thúc.</p>
            <p>Để xác định dấu hiệu đảo chiều chắc chắn hơn NĐT nên kết hợp với các chỉ báo khác như Bollinger band, MA,MACD…. Để xác nhận xu hướng đảo chiều một cách chắc chắn hơn.</p>
            """
            
        st.markdown(text1, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            image = Image.open('images/dragon.jpg')
            st.image(image, caption="Nến Doji chuồn chuồn", use_column_width='always')
        with col2:
            image = Image.open('images/dragon2.jpg')
            st.image(image, caption="Ví dụ minh họa cho nến Doji chuồn chuồn", use_column_width='always') 
        
        text2 = """<div class='row'><h3>Nến Doji bia mộ (Gravestone Doji)</h3>\
            <p>Nến Doji bia mộ là một mẫu hình nến đảo chiều giảm giá thường xuất hiện tại đỉnh của một xu hướng tăng. 
            Nến Doji bia mộ được hình thành khi giá mở cửa thấp nhất trong ngày và giá đóng cửa về cùng hay xấp xỉ mức giá mở cửa. 
            Nến Doji bia mộ rất dễ nhận ra bởi bóng trên rất dài, bóng dưới rất ngắn hoặc không có.</p>
            <p>Bóng trên dài ngụ ý rằng thị trường đang thử thách tại vùng giá có lực cung lớn hay vùng kháng cự ngăn cản khả năng tăng giá. Vùng kháng cự được tìm thấy ngay tại mức giá cao nhất trong ngày giao dịch. 
            Tại đây lực cung mạnh mẽ đã ép giá giảm trở lại bằng hoặc gần bằng mức giá mở cửa. Sự kiểm soát của lực cầu đã bị loại bỏ bởi giá giảm trở lại về gần mức giá mở cửa ban đầu.</p>
            <p>Trong ví dụ dưới đây, ta thấy cây nến Doji bia mộ xuất hiện đánh dấu sự suy yếu của lực cầu thể hiện ở mức giá đóng cửa giảm trở lại về mức giá mở cửa. Tiếp theo là sự xuất hiện của một cây nến đỏ dài củng cố cho xu hướng giảm giá của thị trường.</p>
            <p>Doji bia mộ là 1 mẫu nến đảo chiều vô cùng hữu ích cho nhà đầu tư, nó giúp cho chúng ta thấy được lực cung của thị trường hay ngưỡng kháng cự. Sau 1 xu hướng tăng giá, Doji bia mộ có thể báo hiệu cho nhà đầu tư biết sự tăng giá này đã quá đà và tồn tại đã lâu, nhà đầu tư nên thoát ra ngoài để tránh rủi ro. 
            Nhưng chúng ta cũng nên sử dụng kết hợp với các chỉ báo thị trường khác để có thêm sự chắc chắn của những tín hiệu bán.</p>
        """        
        st.markdown(text2, unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            image = Image.open('images/grave.jpg')
            st.image(image, caption="Nến Doji bia mộ", use_column_width='always')
        with col2:
            image = Image.open('images/grave2.jpg')
            st.image(image, caption="Minh họa Nến Doji bia mộ xuất hiện ở đỉnh của 1 xu hướng tăng", use_column_width='always')    
          
        #st.video("https://www.youtube.com/watch?v=5eFblK8iTJ8&list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ&index=3")
        
    elif active_tab == "Contact":
        st.write("If you'd like to contact me, then please don't.")
    else:
        st.error("Something has gone terribly wrong.")