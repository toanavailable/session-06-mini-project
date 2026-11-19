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
