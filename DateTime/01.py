'''
    datetime:
        - datetime : d/m/y h:m:s

        - date : d/m/y

        - time : h:m:s: ms
            + time(): hiển thị số giây từ 1 / 1/ 1970 đến hiện tại
            + localtime(): chuyển đối số giây từ 1/1/1970 thành một struct thời gian chứ thông tin 
            cục bộ như ngày, tháng, năm, giờ, phút, giây
                . tm_year: lấy năm hiện tại
                . tm_mon: lấy tháng hiện tại
                . tm_mday: lấy ngày hiện tại
                . tm_min: lấy phúc hiện tại
                . tm_sec: lấy giây hiện tại
                . tm_wday: lấy ngày (thứ) trong tuần
                . tm_yday: số ngày đã trôi qua trong năm hiện tại
            + ctime([sec])
        - timedelta: day hr min sec (sự khác biệt giữa 2 ngày)
        - tzinfo: thông tin múi giờ (chuẩn múi giờ GMT giờ luân đôn)
'''

import time
import datetime

# local time
lc = time.localtime()
print(lc)
print(lc.tm_mday)

# time
t = time.time()
print(t)


# datetime.now()
now = datetime.dateime.now()
print(now)