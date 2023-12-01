class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def from_string(cls, s):
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)
    def __str__(self):
        return f"{self.ten} - Vu khi: {self.vu_khi} - Mau sac: {self.mau_sac}"

infor_str = "Do - Kiem - Do"

sieu_nhan_A = SieuNhan.from_string(infor_str)

print(sieu_nhan_A)




