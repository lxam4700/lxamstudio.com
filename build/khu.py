#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cấu trúc portfolio theo khu.

Mỗi khu = 1 trang hub (du-an-<khu>.html) liệt kê các dự án trong khu.
Mỗi dự án = 1 trang riêng (du-an-<slug>.html) do duan.py dựng.

Chạy được ngay khi mỗi dự án có đủ: ảnh bìa + 6-8 ảnh nội dung + 4 dòng thông tin
(khách / năm / vai trò / sản phẩm dùng để làm gì).
"""

KHU = {
    "event": {
        "ten": "Event &amp; Kích hoạt thương hiệu",
        "slug": "event",
        "mo_ta": ("Visual 3D dựng cho sự kiện: phối cảnh gian hàng, hạng mục thi công, "
                  "hình chiếu và vật phẩm trưng bày — dựng trước để duyệt, rồi mới thi công thật."),
        "du_an": [
            {"slug": "chivas-15", "ten": "Chivas 15",
             "nguon": r"D:\SQUARE EC\18. CHIVAS 15\Output",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "chivas-18", "ten": "Chivas 18",
             "nguon": r"D:\SQUARE EC\20. CHIVAS 18\Output",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "ps-krypton-launching-stunt", "ten": "PS Krypton · Launching Stunt",
             "nguon": r"D:\SQUARE EC\10.[024103] PS Krypton Launching Stunt\Output\Dot Win",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "trien-lam-axe", "ten": "Triển lãm Axe",
             "nguon": r"D:\DESIGN\PHOTOGRAPHY\Kỷ niệm AXE\Triển lãm Axe",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
        ],
    },
    "automotive": {
        "ten": "Automotive",
        "slug": "automotive",
        "mo_ta": "Dựng và render xe ở chuẩn quảng cáo — sơn, phản chiếu, kính, bối cảnh.",
        "du_an": [
            {"slug": "mclaren-765lt", "ten": "McLaren 765LT · Horizon", "anh": []},
            {"slug": "porsche-911-turbo-s", "ten": "Porsche 911 Turbo S", "anh": []},
            {"slug": "mercedes-g-tvc", "ten": "Mercedes G · TVC", "anh": []},
            {"slug": "aston-martin-dbx", "ten": "Aston Martin DBX", "anh": []},
            {"slug": "volvo-s90-recharge", "ten": "Volvo S90 · Recharge", "anh": []},
        ],
    },
    "jewelry": {
        "ten": "Jewelry Branding",
        "slug": "jewelry",
        "mo_ta": ("Key visual và bộ hình chiến dịch cho thương hiệu trang sức: khúc xạ đá quý, "
                  "phản chiếu kim loại và ánh sáng macro ở cự ly rất gần."),
        "du_an": [
            {"slug": "nhan-kim-cuong", "ten": "Nhẫn kim cương · Key visual",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "day-chuyen-mat-day", "ten": "Dây chuyền & mặt dây",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "dong-ho-cao-cap", "ten": "Đồng hồ cao cấp",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "bo-suu-tap-lookbook", "ten": "Bộ sưu tập · Lookbook 3D",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
            {"slug": "da-mau-che-tac", "ten": "Đá màu & chế tác",
             "khach": None, "nam": None, "vai_tro": None, "dung_de": None, "anh": []},
        ],
    },
    "san-pham": {
        "ten": "Sản phẩm &amp; Kỹ thuật",
        "slug": "san-pham",
        "mo_ta": "Dựng hình hard-surface, phối cảnh lắp ráp, cắt lớp cấu tạo và animation kỹ thuật.",
        "du_an": [
            # hai dự án này đã có trang đầy đủ
            {"slug": "vplas", "ten": "Thiết bị VPLAS · Exploded", "da_co_trang": True, "anh": []},
            {"slug": "jhm-masonry-hanger", "ten": "JHM Masonry Hanger · TVC", "da_co_trang": True, "anh": []},
            {"slug": "engine", "ten": "Engine · Động cơ", "anh": []},
            {"slug": "khoa-cua-thong-minh", "ten": "Khoá cửa thông minh", "anh": []},
            {"slug": "z113", "ten": "Z113 · Dàn phóng phản lực", "anh": []},
            {"slug": "insta360-gimbal", "ten": "Insta360 · Pocket Gimbal", "hoc_vien": "Lộc", "anh": []},
        ],
    },
}


def thieu(d):
    """Dự án còn thiếu gì trước khi dựng được trang."""
    ra = []
    if not d.get("anh"):
        ra.append("ảnh")
    if "da_co_trang" not in d:
        for k, nhan in (("khach", "khách"), ("nam", "năm"),
                        ("vai_tro", "vai trò"), ("dung_de", "dùng để")):
            if k in d and d[k] is None:
                ra.append(nhan)
    return ra


if __name__ == "__main__":
    print("%-34s %-12s %s" % ("DU AN", "KHU", "CON THIEU"))
    print("-" * 78)
    for k in KHU.values():
        for d in k["du_an"]:
            t = thieu(d)
            print("%-34s %-12s %s" % (d["ten"][:34], k["slug"],
                                      ", ".join(t) if t else "DU — dung duoc"))
