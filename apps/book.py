import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():
    st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
    )
    query_params = st.experimental_get_query_params()
    tabs = ["Candlestick", "About", "Contact"]
    if "tab" in query_params:
        active_tab = query_params["tab"][0]
    else:
        active_tab = "Candlestick"

    if active_tab not in tabs:
        st.experimental_set_query_params(tab="Home")
        active_tab = "Home"

    li_items = "".join(
        f"""
        <li class="nav-item">
            <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
        </li>
        """
        for t in tabs
    )
    tabs_html = f"""
        <ul class="nav nav-tabs">
        {li_items}
        </ul>
    """

    st.markdown(tabs_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if active_tab == "Candlestick":
        components.iframe("""https://www.youtube.com/embed/GL2richiyHY?list=PLQsE4sifO3TSjzEsLHlbbbtIz_2aXMSwJ""" , scrolling = True , height = 500) 
        #st.video('https://www.youtube.com/watch?v=UzVN_1YLL7Y&list=PLQsE4sifO3TRXGt7tooqnEjzcAavP2ls9&index=1')
        
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
        col0, col1= st.columns(2)
        with col0:
            st.markdown(text1, unsafe_allow_html=True)
        with col1:
            image = Image.open('images/nenNhat.jpg')
            st.image(image, width=500)
        text2 = "<p>Hình vẽ bên trên thể hiện một mô hình nến Nhật tiêu chuẩn, mỗi một cây nến biểu thị cho mức độ dao động giá trong một phiên giao dịch. Một cây <strong>nến xanh</strong> được hình thành khi mức <em>giá đóng cửa</em> <strong>cao hơn</strong> mức <em>giá mở cửa</em> của phiên giao dịch đó. \
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
        
    elif active_tab == "About":
        st.write("This page was created as a hacky demo of tabs")
    elif active_tab == "Contact":
        st.write("If you'd like to contact me, then please don't.")
    else:
        st.error("Something has gone terribly wrong.")