# [Mini Project] Hệ thống Quản lý kho

## 1. Mục tiêu

- Khai báo và sử dụng biến đơn, kiểu dữ liệu cơ bản (`int`, `str`).
- Sử dụng toán tử số học và toán tử so sánh.
- Kiểm soát luồng chương trình bằng `if / elif / else`.
- Ứng dụng vòng lặp `while` / `for` và lệnh điều hướng `break` / `continue` để xây dựng menu tương tác liên tục.
- Xử lý ràng buộc và xác thực dữ liệu đầu vào (validation).

## 2. Mô tả bài toán

Cửa hàng công nghệ cần một phần mềm console nhỏ gọn để thủ kho quản lý hàng hóa hằng ngày. Ở giai đoạn này hệ thống **chưa dùng cơ sở dữ liệu hay cấu trúc dữ liệu phức tạp**, mà quản lý trực tiếp **3 mặt hàng cố định bằng 3 biến độc lập**: Laptop, Điện thoại (Phone), Máy tính bảng (Tablet). Số lượng tồn kho luôn là số nguyên `>= 0`.

| Phần | Yêu cầu |
|---|---|
| I - Khởi tạo | 3 biến tồn kho kiểu `int`, giá trị ban đầu là `0` |
| II - Menu | `while True` hiển thị menu 5 lựa chọn; `if / elif / else` bắt lựa chọn; nhập sai (VD: 6) thì báo lỗi và lặp lại menu; chọn 5 thì `break` |
| III - Nhập / Xuất | Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet), nhập số lượng; nhập kho `+=`, xuất kho `-=`; **xuất quá tồn kho** thì in `Không đủ hàng` và hủy giao dịch |
| IV - Ràng buộc | Mỗi lần nhập **số lượng** phải có vòng `while` lồng bên trong; số `< 0` thì in `Số lượng không hợp lệ, vui lòng nhập lại!` và hỏi lại đến khi `>= 0` |
| V - Hiển thị | **(1) Báo cáo:** in số lượng 3 mặt hàng + vẽ biểu đồ dấu `*` bằng vòng `for` (VD: `Laptop (5): *****`). **(4) Cảnh báo:** các `if` **độc lập**, mặt hàng nào `< 10` thì in `[CẢNH BÁO] Mặt hàng ... sắp hết (Chỉ còn ... sản phẩm)` |

## 3. Phân tích và thiết kế

### Thiết kế dữ liệu

| Biến | Kiểu | Ý nghĩa |
|---|---|---|
| `laptop_stock`, `phone_stock`, `tablet_stock` | `int` | Tồn kho 3 mặt hàng, khởi tạo `0` |
| `low_stock_limit` | `int` | Ngưỡng cảnh báo = 10 |
| `choice` | `str` | Lựa chọn menu (`"1"` → `"5"`) |
| `product_choice` | `str` | Mặt hàng (`"1"` → `"3"`) |
| `quantity_text` → `quantity` | `str` → `int` | Số lượng nhập/xuất, kiểm tra trước khi ép kiểu |
| `product_name`, `current_stock` | `str`, `int` | Tên và tồn kho hiện tại của mặt hàng đã chọn (dùng để in thông báo, so sánh khi xuất) |

Lựa chọn menu và mặt hàng được giữ ở dạng **chuỗi** và so sánh với `"1"`, `"2"`… Nhờ vậy khi người dùng gõ chữ (`abc`), chương trình chỉ rơi vào nhánh `else` báo lỗi, **không bị crash** vì lỗi `ValueError` của `int()`.

### Luồng chương trình (Pseudocode)

```
laptop_stock ← 0; phone_stock ← 0; tablet_stock ← 0
LẶP MÃI (while True):
    IN menu; NHẬP choice
    NẾU choice == "1":                      // Báo cáo tồn kho
        IN số lượng 3 mặt hàng
        Với mỗi mặt hàng: LẶP (for) số_lượng lần → IN "*" (không xuống dòng)
    NGƯỢC LẠI NẾU choice == "2" HOẶC "3":   // Nhập / Xuất kho
        LẶP: NHẬP product_choice → nếu là 1/2/3 thì thoát, ngược lại báo lỗi
        LẶP (while lồng bên trong):          // Phần IV
            NHẬP quantity_text
            NẾU là số âm → IN "Số lượng không hợp lệ, vui lòng nhập lại!"; hỏi lại
            NẾU không phải số nguyên → báo lỗi; hỏi lại
            quantity ← int(quantity_text); thoát
        NẾU nhập kho → biến_tương_ứng += quantity
        NẾU xuất kho:
            NẾU quantity > tồn kho → IN "Không đủ hàng", HỦY giao dịch (continue)
            biến_tương_ứng -= quantity
    NGƯỢC LẠI NẾU choice == "4":            // Cảnh báo tồn kho thấp
        NẾU laptop_stock < 10 → IN cảnh báo Laptop      (if độc lập)
        NẾU phone_stock  < 10 → IN cảnh báo Điện thoại  (if độc lập)
        NẾU tablet_stock < 10 → IN cảnh báo Máy tính bảng (if độc lập)
        NẾU không có cảnh báo nào → IN "Tất cả mặt hàng đều đủ"
    NGƯỢC LẠI NẾU choice == "5": IN lời chào; THOÁT (break)
    NGƯỢC LẠI: IN "Lựa chọn không hợp lệ"
```

### Các điểm kỹ thuật chính

- **Vì sao cảnh báo dùng các `if` độc lập mà không dùng `if / elif`?** Với `elif`, khi Laptop đã sắp hết thì Python **bỏ qua** việc kiểm tra Điện thoại và Máy tính bảng. Dùng 3 `if` riêng thì **mọi mặt hàng** đều được kiểm tra và có thể in nhiều cảnh báo cùng lúc.
- **Ràng buộc xuất kho:** điều kiện hủy là `quantity > current_stock` (lớn hơn **hẳn**). Xuất đúng bằng số đang tồn vẫn hợp lệ và tồn kho về 0.
- **Hủy giao dịch** dùng `continue`: bỏ qua phần trừ kho, quay lại đầu vòng `while True` để hiện lại menu.
- **Kiểm tra số âm trước khi ép kiểu:** `"-5".isdigit()` là `False` (dấu `-` không phải chữ số), nên code kiểm tra riêng dạng `"-" + chữ số` để in **đúng** thông báo của đề; chữ hoặc số lẻ thì báo cần nhập số nguyên.
- **Biểu đồ:** mỗi mặt hàng một vòng `for unit in range(stock)` in `"*"` với `end=""`, sau đó `print()` để xuống dòng. Tồn kho 0 thì vòng `for` không chạy lần nào, nên biểu đồ để trống.
- Không dùng list / dict theo đúng yêu cầu "biến độc lập". Mỗi mặt hàng được xử lý bằng một nhánh `if / elif / else` theo `product_choice`.

## 4. Mã nguồn

File: [`quan_ly_kho.py`](quan_ly_kho.py)

```python
"""[Mini Project] Hệ thống Quản lý kho - cửa hàng công nghệ."""

# =====================================================================
# PHẦN I - KHỞI TẠO HỆ THỐNG
# =====================================================================
laptop_stock = 0      # số lượng tồn kho Laptop (int, >= 0)
phone_stock = 0       # số lượng tồn kho Điện thoại (int, >= 0)
tablet_stock = 0      # số lượng tồn kho Máy tính bảng (int, >= 0)

low_stock_limit = 10  # dưới 10 sản phẩm thì cảnh báo sắp hết
line_width = 45

# =====================================================================
# PHẦN II - MENU ĐIỀU HƯỚNG (vòng lặp vô hạn)
# =====================================================================
while True:
    print("\n" + "=" * line_width)
    print(f"{'HỆ THỐNG QUẢN LÝ KHO':^{line_width}}")
    print("=" * line_width)
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    choice = input("Chọn chức năng (1-5): ").strip()

    # -----------------------------------------------------------------
    # PHẦN V - Lựa chọn 1: Xem báo cáo tồn kho + vẽ biểu đồ dấu *
    # -----------------------------------------------------------------
    if choice == "1":
        print("\n--- BÁO CÁO TỒN KHO ---")
        print(f"Laptop        : {laptop_stock} sản phẩm")
        print(f"Điện thoại    : {phone_stock} sản phẩm")
        print(f"Máy tính bảng : {tablet_stock} sản phẩm")

        print("\n--- BIỂU ĐỒ TỒN KHO ---")
        print(f"Laptop ({laptop_stock}): ", end="")
        for unit in range(laptop_stock):
            print("*", end="")
        print()

        print(f"Điện thoại ({phone_stock}): ", end="")
        for unit in range(phone_stock):
            print("*", end="")
        print()

        print(f"Máy tính bảng ({tablet_stock}): ", end="")
        for unit in range(tablet_stock):
            print("*", end="")
        print()

    # -----------------------------------------------------------------
    # PHẦN III - Lựa chọn 2 (Nhập kho) và 3 (Xuất kho)
    # -----------------------------------------------------------------
    elif choice == "2" or choice == "3":
        action_name = "nhập" if choice == "2" else "xuất"

        # Chọn mặt hàng: hỏi lại cho đến khi chọn đúng 1, 2 hoặc 3
        while True:
            product_choice = input(f"Chọn mặt hàng cần {action_name} (1-Laptop, 2-Phone, 3-Tablet): ").strip()
            if product_choice == "1" or product_choice == "2" or product_choice == "3":
                break
            print("Mặt hàng không hợp lệ, vui lòng chọn 1, 2 hoặc 3!")

        if product_choice == "1":
            product_name = "Laptop"
            current_stock = laptop_stock
        elif product_choice == "2":
            product_name = "Điện thoại"
            current_stock = phone_stock
        else:
            product_name = "Máy tính bảng"
            current_stock = tablet_stock

        # PHẦN IV - Ràng buộc: vòng lặp while lồng bên trong kiểm tra số lượng
        while True:
            quantity_text = input(f"Nhập số lượng {product_name} cần {action_name}: ").strip()
            is_negative = quantity_text.startswith("-") and quantity_text[1:].isdigit()

            if is_negative:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
                continue
            if not quantity_text.isdigit():
                # chặn chữ, số lẻ, ô trống -> chương trình không bị crash
                print("Vui lòng nhập một số nguyên (VD: 5)!")
                continue

            quantity = int(quantity_text)
            break   # số lượng hợp lệ (>= 0)

        if choice == "2":
            # Nhập kho: cộng dồn vào biến tương ứng
            if product_choice == "1":
                laptop_stock += quantity
            elif product_choice == "2":
                phone_stock += quantity
            else:
                tablet_stock += quantity
            print(f"Đã nhập {quantity} {product_name}. Tồn kho mới: {current_stock + quantity}")
        else:
            # Xuất kho: không được xuất quá số lượng đang tồn
            if quantity > current_stock:
                print(f"Không đủ hàng (tồn kho {product_name} hiện có: {current_stock}). Giao dịch đã bị hủy.")
                continue   # hủy giao dịch, quay lại menu

            if product_choice == "1":
                laptop_stock -= quantity
            elif product_choice == "2":
                phone_stock -= quantity
            else:
                tablet_stock -= quantity
            print(f"Đã xuất {quantity} {product_name}. Tồn kho còn lại: {current_stock - quantity}")

    # -----------------------------------------------------------------
    # PHẦN V - Lựa chọn 4: Cảnh báo tồn kho thấp (các if độc lập)
    # -----------------------------------------------------------------
    elif choice == "4":
        print("\n--- KIỂM TRA TỒN KHO THẤP ---")
        has_warning = False

        if laptop_stock < low_stock_limit:
            print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop_stock} sản phẩm)")
            has_warning = True
        if phone_stock < low_stock_limit:
            print(f"[CẢNH BÁO] Mặt hàng Điện thoại sắp hết (Chỉ còn {phone_stock} sản phẩm)")
            has_warning = True
        if tablet_stock < low_stock_limit:
            print(f"[CẢNH BÁO] Mặt hàng Máy tính bảng sắp hết (Chỉ còn {tablet_stock} sản phẩm)")
            has_warning = True

        if not has_warning:
            print(f"Tất cả mặt hàng đều còn từ {low_stock_limit} sản phẩm trở lên.")

    # -----------------------------------------------------------------
    # Lựa chọn 5: Thoát chương trình
    # -----------------------------------------------------------------
    elif choice == "5":
        print("Đã thoát chương trình. Hẹn gặp lại!")
        break

    # -----------------------------------------------------------------
    # Nhập sai lựa chọn menu
    # -----------------------------------------------------------------
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!")
```

## 5. Kết quả chạy thử

**Menu chính:**

```
=============================================
            HỆ THỐNG QUẢN LÝ KHO             
=============================================
1. Xem báo cáo tồn kho
2. Nhập kho
3. Xuất kho
4. Cảnh báo hàng tồn kho thấp
5. Thoát chương trình
```

**Nhập sai menu, nhập kho có số lượng âm (Phần II + IV):**

```
Chọn chức năng (1-5): 6
Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!

Chọn chức năng (1-5): abc
Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5!

Chọn chức năng (1-5): 2
Chọn mặt hàng cần nhập (1-Laptop, 2-Phone, 3-Tablet): 1
Nhập số lượng Laptop cần nhập: -5
Số lượng không hợp lệ, vui lòng nhập lại!
Nhập số lượng Laptop cần nhập: 12
Đã nhập 12 Laptop. Tồn kho mới: 12
```

**Chọn sai mặt hàng (hỏi lại đến khi chọn đúng):**

```
Chọn chức năng (1-5): 2
Chọn mặt hàng cần nhập (1-Laptop, 2-Phone, 3-Tablet): 4
Mặt hàng không hợp lệ, vui lòng chọn 1, 2 hoặc 3!
Chọn mặt hàng cần nhập (1-Laptop, 2-Phone, 3-Tablet): abc
Mặt hàng không hợp lệ, vui lòng chọn 1, 2 hoặc 3!
Chọn mặt hàng cần nhập (1-Laptop, 2-Phone, 3-Tablet): 3
Nhập số lượng Máy tính bảng cần nhập: 3
Đã nhập 3 Máy tính bảng. Tồn kho mới: 3
```

**Báo cáo tồn kho + biểu đồ (Phần V):**

```
Chọn chức năng (1-5): 1

--- BÁO CÁO TỒN KHO ---
Laptop        : 12 sản phẩm
Điện thoại    : 5 sản phẩm
Máy tính bảng : 3 sản phẩm

--- BIỂU ĐỒ TỒN KHO ---
Laptop (12): ************
Điện thoại (5): *****
Máy tính bảng (3): ***
```

**Xuất kho quá số lượng tồn → "Không đủ hàng" (Phần III):**

```
Chọn chức năng (1-5): 3
Chọn mặt hàng cần xuất (1-Laptop, 2-Phone, 3-Tablet): 3
Nhập số lượng Máy tính bảng cần xuất: 5
Không đủ hàng (tồn kho Máy tính bảng hiện có: 3). Giao dịch đã bị hủy.

Chọn chức năng (1-5): 3
Chọn mặt hàng cần xuất (1-Laptop, 2-Phone, 3-Tablet): 2
Nhập số lượng Điện thoại cần xuất: abc
Vui lòng nhập một số nguyên (VD: 5)!
Nhập số lượng Điện thoại cần xuất: 10
Không đủ hàng (tồn kho Điện thoại hiện có: 5). Giao dịch đã bị hủy.
```

**Xuất kho thành công** (lần chạy khác: nhập trước Laptop 20, Điện thoại 15, Máy tính bảng 10):

```
Chọn chức năng (1-5): 3
Chọn mặt hàng cần xuất (1-Laptop, 2-Phone, 3-Tablet): 1
Nhập số lượng Laptop cần xuất: 5
Đã xuất 5 Laptop. Tồn kho còn lại: 15

Chọn chức năng (1-5): 3
Chọn mặt hàng cần xuất (1-Laptop, 2-Phone, 3-Tablet): 2
Nhập số lượng Điện thoại cần xuất: 15
Đã xuất 15 Điện thoại. Tồn kho còn lại: 0
```

**Cảnh báo tồn kho thấp (các if độc lập, in nhiều cảnh báo cùng lúc):**

```
Chọn chức năng (1-5): 4

--- KIỂM TRA TỒN KHO THẤP ---
[CẢNH BÁO] Mặt hàng Điện thoại sắp hết (Chỉ còn 5 sản phẩm)
[CẢNH BÁO] Mặt hàng Máy tính bảng sắp hết (Chỉ còn 3 sản phẩm)
```

**Không có mặt hàng nào dưới 10** (lần chạy khác: Laptop 10, Điện thoại 25, Máy tính bảng 10):

```
Chọn chức năng (1-5): 4

--- KIỂM TRA TỒN KHO THẤP ---
Tất cả mặt hàng đều còn từ 10 sản phẩm trở lên.
```

**Thoát chương trình:**

```
Chọn chức năng (1-5): 5
Đã thoát chương trình. Hẹn gặp lại!
```

## 6. Bảng kiểm thử

| # | Kịch bản | Dữ liệu | Kết quả mong đợi | Kết quả |
|---|---|---|---|---|
| 1 | Báo cáo khi kho trống | Chọn 1 | 3 mặt hàng = 0, biểu đồ trống | ✅ |
| 2 | Nhập sai menu | `6`, `abc` | Báo lỗi, hiện lại menu, không crash | ✅ |
| 3 | Nhập kho số lượng âm | `-5` rồi `12` | Báo "Số lượng không hợp lệ...", hỏi lại; nhận 12 | ✅ |
| 4 | Chọn sai mặt hàng | `4`, `abc` | Báo lỗi, hỏi lại đến khi chọn 1/2/3 | ✅ |
| 5 | Số lượng không phải số | `abc` | Báo cần nhập số nguyên, hỏi lại | ✅ |
| 6 | Xuất quá tồn kho | Tablet tồn 3, xuất 5 | "Không đủ hàng", tồn kho giữ nguyên | ✅ |
| 7 | Xuất thành công | Laptop 20, xuất 5 | Còn 15 | ✅ |
| 8 | Xuất đúng bằng tồn kho | Phone 15, xuất 15 | Còn 0 (hợp lệ) | ✅ |
| 9 | Cảnh báo nhiều mặt hàng | Phone 5, Tablet 3 | 2 dòng cảnh báo | ✅ |
| 10 | Không mặt hàng nào < 10 | 10 / 25 / 10 | "Tất cả mặt hàng đều còn từ 10 sản phẩm trở lên." | ✅ |
| 11 | Biểu đồ | Laptop 12 | `Laptop (12): ************` | ✅ |
| 12 | Thoát | Chọn 5 | In lời chào, kết thúc | ✅ |

## 7. Báo cáo

- [Báo cáo dạng PDF](bao-cao-mini-project-quan-ly-kho.pdf)
- [Báo cáo dạng Word (DOCX)](bao-cao-mini-project-quan-ly-kho.docx)
