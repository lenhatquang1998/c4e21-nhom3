from mongoengine import *
# import mlab

# mlab.connect()

class Food(Document):
    ten_mon = StringField()
    chu_de = StringField()
    nguyen_lieu = ListField()
    link_anh = StringField()
    cach_lam = ListField(DictField())
    link_san_pham = StringField()


# new_food = Food(
#     link_san_pham = "https://znews-photo-td.zadn.vn/w660/Uploaded/Ohunoaa/2017_01_17/g.jpg",
#     chu_de = "couple",
#     ten_mon = "gà phô mai hàn quốc không cần lò nướng",
#     nguyen_lieu = ["1 kg thịt ức gà", "1/2 chén ớt bột (của Việt Nam hay Hàn Quốc đều được)", "1 muỗng canh nước tương (xì dầu)", "3 muỗng canh dầu mè", "3 muỗng canh dầu mè", "1/2 muỗng cà phê hạt tiêu đen", "1/3 chén siro dâu", "1 củ tỏi lớn", "2 muỗng cà phê gừng băm nhuyễn",
#     "450 gram phô mai mozzarella", "30 ml nước lọc", "1 cây hành bao ro/20 gram hành lá"],
#     link_anh = "",
#     cach_lam = [
#         {
#             "mo_ta": "Rửa sạch thịt ức gà, trụng nhanh thịt qua nước sôi để loại bỏ chất bẩn, để ráo.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Xắt thịt gà thành miếng vừa ăn.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Cắt phô mai thành miếng vừa ăn.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Ướp thịt gà với gừng băm nhuyễn, tỏi đập dập, hành lá xắt vụn, ít muối, bột ngọt. Đặt thịt đã ướp vào ngăn mát tủ lạnh ít nhất 30 phút cho ngấm gia vị.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Lần lượt cho ớt bột, tương ớt, nước tương, dầu mè, hạt tiêu đen, xi-rô dâu, tỏi, gừng vào tô, trộn đều. Cho hỗn hợp gia vị vào thịt gà, để 30 phút cho thịt gà ngấm gia vị. ",
#             "link": "",
#         },
#         {
#             "mo_ta": "Làm nóng chảo dầu (nên dùng chảo không dính), cho thịt gà vừa ướp vào, xào chín - khoảng 10 phút.Lúc này thịt gà chưa cạn hết nước.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Khi thịt gà chín, bạn trải đều phô mai lên thịt gà, đậy nắp lại và vặn nhỏ lửa. Khoảng 5-7 phút sau, phô mai sẽ chảy và phủ đều một lớp trên thịt gà. Dùng khi còn nóng. ",
#             "link": "",
#         },
       
#     ]
# )

# new_food.save()