## Giới thiệu

Tên dự án: Histogram Equalization - Cân bằng mức xám
Phiên bản: 1.0

Dự án Histogram Equalization là một dự án mã nguồn mở cung cấp một thư viện Python để thực hiện cân bằng biểu đồ cho hình ảnh. Thư viện này sử dụng phương pháp cân bằng biểu đồ toàn cục để phân bố lại các giá trị cường độ pixel trong hình ảnh sao cho chúng được phân phối đồng đều hơn. Điều này có thể cải thiện độ tương phản của hình ảnh, làm cho các chi tiết nhỏ hơn dễ nhìn thấy hơn và làm cho hình ảnh trông tổng thể sáng hơn hoặc tối hơn.

Các tính năng chính của dự án bao gồm:
- Hỗ trợ cân bằng biểu đồ toàn cục cho hình ảnh xám.
- Cung cấp một số tùy chọn để điều chỉnh kết quả cân bằng biểu đồ.
- Được viết bằng Python và được tối ưu hóa để sử dụng hiệu quả.

## Hướng dẫn sử dụng

### Yêu cầu hệ thống
* Window, Linux, MacOs
* Python  version >= 3.9, opencv-python version 4.8.0, matplotlib version 3.7.1, seaborn version 0.12.2, pandas version 1.5.3, numpy version 1.23.5, tkinter version 8.6
### Cách cài đặt

1. git clone https://github.com/lastonton/Histogram_Equallization_Tkinter_SourceCode.git
2. Tạo thư mục histogram và images trong folder đã clone về
3. Cài đặt các thư viên đã nêu ở yêu cầu hệ thống qua câu lệnh pip install
- https://www.python.org/downloads/ (Python dowload)
- pip install opencv-python==4.8.0
- pip install matplotlib==3.7.1
- pip install pandas==1.5.3
- pip install seaborn==0.12.2
- pip install numpy==1.23.5
- pip install tkinter==8.6


### Cách chạy

1. Mở file app.py trong IDLE hoăc Visual Studio Code
2. Chọn Run -> Starting Debugging hoặc F5 để khởi chạy ứng dụng

### Cách sử dụng

1. Khởi động ứng dụng
2. Nhấn chọn Select Image và chọn hình ảnh để thực hiện cân bằng mức xám
3. Nhấn chọn Run và hình ảnh đã được xử lý sẽ xuất hiện ở ô bên phải hàng trên
4. Nhấn chọn Export Histogram để xuất biểu đồ trước và sau khi thực hiện xử lý cân bằng mức xám (hình biểu đồ được lưu trong folder histogram)
5. Kéo thanh Slider bên dưới hình đã qua xử lý để chọn mức sáng phù hợp với nhu cầu
6. Nhấn chọn Save Images để lưu lại hình ảnh đã được xử lý vào thư mục images.
